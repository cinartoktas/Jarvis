from langgraph.graph import StateGraph, END

from agents.planner_agent import planla
from agents.executor_agent import execute
from agents.memory_agent import calistir as hafiza_calistir
from models.state import JarvisState


# =========================================================
# HAFIZA
# =========================================================

def hafiza_node(state: JarvisState):

    kullanildi, cevap = hafiza_calistir(
        state["user_input"]
    )

    return {
        "memory_handled": kullanildi,
        "response": cevap
    }


# =========================================================
# HAFIZA YÖNLENDİRME
# =========================================================

def hafiza_yonlendir(state: JarvisState):

    if state.get("memory_handled"):
        return "end"

    return "planner"


# =========================================================
# PLANNER
# =========================================================

def planner_node(state: JarvisState):

    kullanici_girdisi = state["user_input"]

    # =====================================================
    # DEVAM ET
    # =====================================================

    if kullanici_girdisi.strip().lower() in (
        "devam et",
        "devam",
        "sürdür",
        "surdur"
    ):

        pending = state.get("pending_plan")

        if pending:

            return {
                "plan": pending
            }

        return {
            "plan": {
                "steps": [],
                "goal": "Devam edilecek bekleyen görev bulunamadı."
            }
        }

    # =====================================================
    # NORMAL PLAN
    # =====================================================

    plan = planla(
        kullanici_girdisi
    )

    return {
        "plan": plan
    }


# =========================================================
# EXECUTOR
# =========================================================

def executor_node(state: JarvisState):

    sonuc = execute(
        state["plan"]
    )

    # Executor artık sadece liste değil,
    # durum bilgisi içeren dict döndürüyor.

    if isinstance(sonuc, dict):

        return {
            "response": sonuc.get(
                "response",
                []
            ),
            "pending_plan": sonuc.get(
                "pending_plan"
            )
        }

    # Eski tip dönüş için güvenlik
    return {
        "response": sonuc,
        "pending_plan": None
    }


# =========================================================
# GRAPH
# =========================================================

graph_builder = StateGraph(
    JarvisState
)


graph_builder.add_node(
    "hafiza",
    hafiza_node
)


graph_builder.add_node(
    "planner",
    planner_node
)


graph_builder.add_node(
    "executor",
    executor_node
)


# Başlangıç
graph_builder.set_entry_point(
    "hafiza"
)


# Hafıza sonrası
graph_builder.add_conditional_edges(
    "hafiza",
    hafiza_yonlendir,
    {
        "planner": "planner",
        "end": END
    }
)


# Planner → Executor
graph_builder.add_edge(
    "planner",
    "executor"
)


# Executor → END
graph_builder.add_edge(
    "executor",
    END
)


graph = graph_builder.compile()