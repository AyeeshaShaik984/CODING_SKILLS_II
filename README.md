# 🚚 Delivery Route Optimizer

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Algorithms](https://img.shields.io/badge/Algorithms-Dijkstra%20%7C%20Greedy%20NN-orange)]()

An intelligent **package delivery route planner** that finds the shortest delivery path using:
- **Dijkstra's Algorithm** — exact shortest path between any two stops
- **Greedy Nearest-Neighbour Heuristic** — efficient multi-stop tour approximation

Comes with a **standalone interactive web UI** (`index.html`) that runs entirely in the browser — no server needed.

---

## 📁 Project Structure

```
delivery-route-optimizer/
│
├── index.html               ← Standalone web UI (open in any browser)
│
├── data/
│   └── locations.csv        ← Sample delivery locations (lat/lon)
│
├── src/
│   ├── main.py              ← CLI entry point
│   ├── graph_utils.py       ← Graph + Dijkstra's algorithm
│   ├── greedy_optimizer.py  ← Greedy nearest-neighbour TSP heuristic
│   └── visualize.py         ← Generates interactive Leaflet.js HTML map
│
├── maps/
│   └── optimized_route_map.html  ← Auto-generated map (after running main.py)
│
├── requirements.txt
└── README.md
```

---

## 🚀 Quick Start

### Option A — Web UI (no Python needed)
Simply open `index.html` in any modern browser.

Features:
- Click the map to add delivery stops
- First stop becomes the **Depot**
- Click **▶ Optimize Route** to run the Greedy NN algorithm
- Use the **Dijkstra** tab to find shortest paths between any two stops
- **Load Sample Data** for a pre-built 10-stop Hyderabad demo

### Option B — Python CLI

```bash
# 1. Clone the repo
git clone https://github.com/shabbirbasha-dev/Delivery-Route-Optimizer.git
cd Delivery-Route-Optimizer

# 2. (Optional) Install dependencies
pip install -r requirements.txt

# 3. Run with default sample data
python src/main.py

# 4. Open generated map in browser
python src/main.py --open

# 5. Use your own CSV
python src/main.py --data path/to/my_locations.csv
```

---

## 📊 Sample Output

```
📂  Loading locations from: data/locations.csv
✅  Loaded 10 locations.
✅  Graph built with 10 nodes and 45 edges.

🧭  Running Dijkstra from depot: [1] Warehouse (Depot)
    Shortest distances from depot:
    → Madhapur                           1.42 km
    → Hitech City                        2.36 km
    → Manikonda                          3.68 km
    ...

📦  Shortest path [1] → [10]: Warehouse (Depot) → Kokapet  (5.13 km)

🚚  Running Greedy Nearest-Neighbour optimisation …

============================================================
  🚚  GREEDY NEAREST-NEIGHBOUR ROUTE
============================================================
  Step  1: Warehouse (Depot)  → Madhapur      [1.42 km]
  Step  2: Madhapur           → Hitech City   [1.10 km]
  ...
  Step 10: Kukatpally         → Warehouse     [5.31 km]
------------------------------------------------------------
  ✅  Route complete | Stops: 10 | Total: 32.02 km
============================================================

🗺️  Map saved to: maps/optimized_route_map.html
```

---

## 📦 CSV Format

Your `locations.csv` must have these columns:

```csv
id,name,latitude,longitude
1,Warehouse (Depot),17.4374,78.3985
2,Customer A,17.4849,78.3938
...
```

---

## 🧠 Algorithms

### Dijkstra's Algorithm
- Finds the **exact shortest path** between any two nodes
- Uses a **min-heap** (priority queue) for O((V + E) log V) time
- Works on a complete graph with Haversine edge weights

### Greedy Nearest-Neighbour (TSP Heuristic)
- Starts at the depot and repeatedly visits the **closest unvisited stop**
- Returns to depot to close the tour
- Time complexity: O(n²) — fast for typical delivery fleet sizes
- Produces good (not always optimal) solutions quickly

### Haversine Formula
All distances are computed using the **Haversine formula** for great-circle distances between GPS coordinates (in kilometres).

---

## 🔮 Future Improvements

- [ ] Integrate real road distances via OpenRouteService API
- [ ] Multiple vehicles and time-window constraints
- [ ] A* or Genetic Algorithm for better tour optimization
- [ ] Export optimized route as CSV / PDF
- [ ] Real-time traffic-aware routing

