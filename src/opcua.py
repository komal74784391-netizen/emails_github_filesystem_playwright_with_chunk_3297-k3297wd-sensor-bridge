"""Thin OPC-UA adapter used by the OrbitCrate rigs."""
from __future__ import annotations


class NodeTable:
    def __init__(self):
        self._nodes = {}

    def declare(self, tag: str, node_id: str, unit: str = ""):
        self._nodes[tag] = {"node_id": node_id, "unit": unit}

    def resolve(self, tag: str) -> str:
        if tag not in self._nodes:
            raise KeyError(f"unknown tag {tag}")
        return self._nodes[tag]["node_id"]

    def browse(self):
        return sorted(self._nodes)
