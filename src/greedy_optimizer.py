"""
greedy_optimizer.py
-------------------
Greedy Nearest-Neighbour heuristic for the Travelling Salesman Problem (TSP).

Given a set of delivery nodes and a starting depot, this module builds an
approximate multi-stop route by always visiting the closest unvisited node
next.  The route ends by returning to the depot (closed tour).

Time complexity : O(n²)  — perfectly fine for typical last-mile delivery fleets
                           (up to a few hundred stops).
"""

import math
from typing import List, Dict, Optional, Tuple
from graph_utils import DeliveryGraph


# ---------------------------------------------------------------------------
# Result dataclass (plain dict so no external deps needed)
# ---------------------------------------------------------------------------

RouteResult = Dict  # {route, total_dist_km, legs, stop_names}


# ---------------------------------------------------------------------------
# Greedy optimizer
# ---------------------------------------------------------------------------

class GreedyOptimizer:
    """
    Builds an approximate delivery route using the Nearest-Neighbour heuristic.

    Parameters
    ----------
    graph   : DeliveryGraph  — fully built graph with edge weights
    depot   : int            — node id of the warehouse / starting depot
    """

    def __init__(self, graph: DeliveryGraph, depot: int):
        self.graph = graph
        self.depot = depot

    # ------------------------------------------------------------------
    # Core algorithm
    # ------------------------------------------------------------------

    def _direct_distance(self, u: int, v: int) -> float:
        """Return the direct (edge) distance between nodes u and v."""
        for neighbour, weight in self.graph.adj.get(u, []):
            if neighbour == v:
                return weight
        # Fallback: Haversine if edge not found (shouldn't happen on a complete graph)
        n1, n2 = self.graph.nodes[u], self.graph.nodes[v]
        from graph_utils import haversine
        return haversine(n1["lat"], n1["lon"], n2["lat"], n2["lon"])

    def optimize(self, stops: Optional[List[int]] = None) -> RouteResult:
        """
        Run the greedy nearest-neighbour algorithm.

        Parameters
        ----------
        stops : list of node ids to visit (excluding depot).
                If None, all nodes except the depot are used.

        Returns
        -------
        RouteResult dict with keys:
            route          – ordered list of node ids (depot ... depot)
            total_dist_km  – total route distance in km
            legs           – list of (from_id, to_id, dist_km) per segment
            stop_names     – human-readable ordered stop names
        """
        if stops is None:
            stops = [nid for nid in self.graph.nodes if nid != self.depot]

        if not stops:
            return {
                "route": [self.depot],
                "total_dist_km": 0.0,
                "legs": [],
                "stop_names": [self.graph.nodes[self.depot]["name"]],
            }

        unvisited = set(stops)
        route: List[int] = [self.depot]
        total_dist = 0.0
        legs: List[Tuple[int, int, float]] = []

        current = self.depot

        while unvisited:
            # Find the nearest unvisited stop from current position
            nearest: Optional[int] = None
            nearest_dist = math.inf

            for candidate in unvisited:
                d = self._direct_distance(current, candidate)
                if d < nearest_dist:
                    nearest_dist = d
                    nearest = candidate

            # Travel to nearest
            legs.append((current, nearest, round(nearest_dist, 4)))
            total_dist += nearest_dist
            route.append(nearest)
            unvisited.remove(nearest)
            current = nearest

        # Return to depot (close the tour)
        return_dist = self._direct_distance(current, self.depot)
        legs.append((current, self.depot, round(return_dist, 4)))
        total_dist += return_dist
        route.append(self.depot)

        stop_names = [self.graph.nodes[nid]["name"] for nid in route]

        return {
            "route": route,
            "total_dist_km": round(total_dist, 4),
            "legs": legs,
            "stop_names": stop_names,
        }

    # ------------------------------------------------------------------
    # Pretty-print
    # ------------------------------------------------------------------

    def print_route(self, result: RouteResult) -> None:
        """Print a formatted summary of the optimised route."""
        print("\n" + "=" * 60)
        print("  🚚  GREEDY NEAREST-NEIGHBOUR ROUTE")
        print("=" * 60)

        for i, (frm, to, dist_km) in enumerate(result["legs"]):
            frm_name = self.graph.nodes[frm]["name"]
            to_name  = self.graph.nodes[to]["name"]
            step_label = f"  Step {i + 1:>2}"
            print(f"{step_label}: {frm_name:25s} → {to_name:25s}  [{dist_km:.2f} km]")

        print("-" * 60)
        print(f"  ✅  Route complete  |  Stops: {len(result['route']) - 1}  |  "
              f"Total: {result['total_dist_km']:.2f} km")
        print("=" * 60 + "\n")
