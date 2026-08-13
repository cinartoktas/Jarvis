from typing import TypedDict, Optional


class JarvisState(TypedDict, total=False):

    user_input: str
    plan: dict
    response: str
    pending_plan: Optional[dict]
    memory_handled: bool