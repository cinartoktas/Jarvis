from langgraph.graph import StateGraph, END

from agents.planner_agent import planla
from agents.executor_agent import execute



def planner_node(state):

    plan = planla(
        state["user_input"]
    )


    return {
        "plan": plan
    }




def executor_node(state):

    sonuc = execute(
        state["plan"]
    )


    return {
        "response": sonuc
    }




graph_builder = StateGraph(dict)


graph_builder.add_node(
    "planner",
    planner_node
)


graph_builder.add_node(
    "executor",
    executor_node
)



graph_builder.set_entry_point(
    "planner"
)


graph_builder.add_edge(
    "planner",
    "executor"
)


graph_builder.add_edge(
    "executor",
    END
)



graph = graph_builder.compile()