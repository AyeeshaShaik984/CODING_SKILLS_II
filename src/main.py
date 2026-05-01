"""
main.py
-------
Entry point for the Delivery Route Optimizer.

Pipeline
--------
1. Load delivery locations from data/locations.csv
2. Build a complete weighted graph (Haversine distances)
3. Run Dijkstra's algorithm (depot → every stop)
4. Run Greedy Nearest-Neighbour to produce the full delivery tour
5. Print a summary to the console
6. Generate maps/optimized_route_map.html (interactive Leaflet map)

Usage
-----
    python src/main.py                        # default locations.csv
    python src/main.py --data path/to/locs.csv
    python src/main.py --open                 # also open in browser
"""

import argparse
import csv
import os
import sys
import io

# Fix for Windows console emoji printing (cp1252 to utf-8)
if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Make sure local src/ modules are importable when called from project root
sys.path.insert(0, os.path.dirname(__file__))

from graph_utils import DeliveryGraph
from greedy_optimizer import GreedyOptimizer
from visualize import RouteVisualizer


# ---------------------------------------------------------------------------
# CSV loader
# ---------------------------------------------------------------------------

def load_locations(csv_path: str) -> list:
    """
    Read locations.csv and return a list of dicts:
        {id, name, latitude, longitude}
    """
    locations = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            locations.append({
                "id":        int(row["id"]),
                "name":      row["name"].strip(),
                "latitude":  float(row["latitude"]),
                "longitude": float(row["longitude"]),
            })
    return locations


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Delivery Route Optimizer")
    parser.add_argument(
        "--data", default="data/locations.csv",
        help="Path to CSV file with columns: id,name,latitude,longitude"
    )
    parser.add_argument(
        "--open", action="store_true",
        help="Open the generated map in the default browser after running"
    )
    args = parser.parse_args()

    csv_path = args.data
    if not os.path.isabs(csv_path):
        # Resolve relative to project root (one level above src/)
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_path = os.path.join(project_root, csv_path)

    # ── 1. Load locations ────────────────────────────────────────────
    print(f"\n📂  Loading locations from: {csv_path}")
    locations = load_locations(csv_path)
    print(f"✅  Loaded {len(locations)} locations.")

    # ── 2. Build graph ───────────────────────────────────────────────
    graph = DeliveryGraph()
    for loc in locations:
        graph.add_node(loc["id"], loc["name"], loc["latitude"], loc["longitude"])
    graph.build_complete_graph()
    print(f"✅  Graph built with {graph.node_count()} nodes and {graph.edge_count()} edges.")

    # ── 3. Dijkstra from depot (first location) ──────────────────────
    depot_id = locations[0]["id"]
    depot_name = locations[0]["name"]
    print(f"\n🧭  Running Dijkstra from depot: [{depot_id}] {depot_name}")

    dist_map, _ = graph.dijkstra(depot_id)
    print("    Shortest distances from depot:")
    for nid, d in dist_map.items():
        if nid != depot_id:
            print(f"    → {graph.nodes[nid]['name']:30s}  {d:.2f} km")

    # Example: shortest path depot → last stop
    last_id = locations[-1]["id"]
    path, path_dist = graph.shortest_path(depot_id, last_id)
    path_names = " → ".join(graph.nodes[n]["name"] for n in path)
    print(f"\n📦  Shortest path  [{depot_id}] → [{last_id}]: {path_names}  ({path_dist:.2f} km)")

    # ── 4. Greedy nearest-neighbour route ────────────────────────────
    print(f"\n🚚  Running Greedy Nearest-Neighbour optimisation …")
    optimizer = GreedyOptimizer(graph, depot=depot_id)
    result    = optimizer.optimize()
    optimizer.print_route(result)

    # ── 5. Generate map ──────────────────────────────────────────────
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    map_path     = os.path.join(project_root, "maps", "optimized_route_map.html")

    visualizer = RouteVisualizer(output_path=map_path)
    saved_path = visualizer.generate(graph, result, open_browser=args.open)
    print(f"🗺️   Map saved to: {saved_path}")
    if not args.open:
        print("     (run with --open to launch in browser automatically)\n")


if __name__ == "__main__":
    main()
