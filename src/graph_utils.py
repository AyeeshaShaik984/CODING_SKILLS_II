"""
graph_utils.py
--------------
Builds a complete weighted graph from delivery locations and provides
Dijkstra's shortest-path algorithm implementation.

Each node is a delivery location.
Edge weights are the Haversine distances (real-world km) between locations.
"""

import math
import heapq
from typing import Dict, List, Tuple, Optional


# ---------------------------------------------------------------------------
# Haversine distance
# ---------------------------------------------------------------------------

def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Return the great-circle distance in kilometres between two
    (latitude, longitude) points using the Haversine formula.
    """
    R = 6371.0  # Earth radius in km
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


# ---------------------------------------------------------------------------
# Graph class
# ---------------------------------------------------------------------------

class DeliveryGraph:
    """
    Undirected, weighted graph where nodes are delivery locations and
    edge weights are Haversine distances in km.
    """

    def __init__(self):
        # adjacency list: node_id -> list of (neighbour_id, weight_km)
        self.adj: Dict[int, List[Tuple[int, float]]] = {}
        self.nodes: Dict[int, dict] = {}   # id -> {name, lat, lon}

    # ------------------------------------------------------------------
    # Construction
    # ------------------------------------------------------------------

    def add_node(self, node_id: int, name: str, lat: float, lon: float) -> None:
        """Register a location as a node."""
        self.nodes[node_id] = {"name": name, "lat": lat, "lon": lon}
        if node_id not in self.adj:
            self.adj[node_id] = []

    def add_edge(self, u: int, v: int, weight: Optional[float] = None) -> None:
        """
        Add an undirected edge between nodes u and v.
        If *weight* is None it is computed from the Haversine distance.
        """
        if weight is None:
            n1, n2 = self.nodes[u], self.nodes[v]
            weight = haversine(n1["lat"], n1["lon"], n2["lat"], n2["lon"])
        self.adj[u].append((v, round(weight, 4)))
        self.adj[v].append((u, round(weight, 4)))

    def build_complete_graph(self) -> None:
        """Connect every pair of nodes (complete graph)."""
        ids = list(self.nodes.keys())
        for i in range(len(ids)):
            for j in range(i + 1, len(ids)):
                self.add_edge(ids[i], ids[j])

    # ------------------------------------------------------------------
    # Dijkstra's algorithm
    # ------------------------------------------------------------------

    def dijkstra(self, source: int) -> Tuple[Dict[int, float], Dict[int, Optional[int]]]:
        """
        Run Dijkstra's algorithm from *source*.

        Returns
        -------
        dist   : shortest distance from source to every reachable node (km)
        prev   : predecessor map for path reconstruction
        """
        dist: Dict[int, float] = {nid: math.inf for nid in self.nodes}
        prev: Dict[int, Optional[int]] = {nid: None for nid in self.nodes}
        dist[source] = 0.0

        # min-heap of (distance, node_id)
        heap: List[Tuple[float, int]] = [(0.0, source)]

        while heap:
            d_u, u = heapq.heappop(heap)
            if d_u > dist[u]:          # stale entry — skip
                continue
            for v, w in self.adj.get(u, []):
                alt = dist[u] + w
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    heapq.heappush(heap, (alt, v))

        return dist, prev

    def shortest_path(self, source: int, target: int) -> Tuple[List[int], float]:
        """
        Return the shortest path (list of node ids) and its total distance (km)
        between *source* and *target* using Dijkstra.
        """
        dist, prev = self.dijkstra(source)

        if math.isinf(dist[target]):
            return [], math.inf   # unreachable

        # Reconstruct path
        path: List[int] = []
        cur: Optional[int] = target
        while cur is not None:
            path.append(cur)
            cur = prev[cur]
        path.reverse()

        return path, round(dist[target], 4)

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def edge_count(self) -> int:
        return sum(len(v) for v in self.adj.values()) // 2

    def node_count(self) -> int:
        return len(self.nodes)

    def __repr__(self) -> str:
        return (
            f"<DeliveryGraph nodes={self.node_count()} "
            f"edges={self.edge_count()}>"
        )
