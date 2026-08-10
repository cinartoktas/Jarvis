from langgraph.graph import StateGraph, END

from agents.planner_agent import planla
from agents.executor_agent import execute
from agents.memory_agent import calistir as hafiza_calistir


def hafiza_node(state):
    kullanildi, cevap = hafiza_calistir(state["user_input"])

    return {
        "memory_handled": kullanildi,
        "response": cevap
    }


def hafiza_yonlendir(state):
    if state.get("memory_handled"):
        return "end"

    return "planner"


def planner_node(state):
    plan = planla(state["user_input"])

    return {
        "plan": plan
    }


def executor_node(state):
    sonuc = execute(state["plan"])

    return {
        "response": sonuc
    }


graph_builder = StateGraph(dict)

graph_builder.add_node("hafiza", hafiza_node)
graph_builder.add_node("planner", planner_node)
graph_builder.add_node("executor", executor_node)

graph_builder.set_entry_point("hafiza")

graph_builder.add_conditional_edges(
    "hafiza",
    hafiza_yonlendir,
    {
        "planner": "planner",
        "end": END
    }
)

graph_builder.add_edge("planner", "executor")
graph_builder.add_edge("executor", END)

graph = graph_builder.compile()