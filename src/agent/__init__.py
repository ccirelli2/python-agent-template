"""
Agent Module.

This module provides a LangGraph-based agent workflow for [DESCRIBE YOUR AGENT].

Main exports:
    - build_agent_graph: Builds the compiled workflow graph
    - AgentState: State type definition
    - [Other models and functions]

Example:
    >>> from src.agent import build_agent_graph
    >>> graph = build_agent_graph()
    >>> result = graph.invoke({"input": "example query"})
"""

from src.agent.state import AgentState
from src.agent.workflow import build_agent_graph

__all__ = [
    "build_agent_graph",
    "AgentState",
]
