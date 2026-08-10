from typing import TypedDict


class JarvisState(TypedDict):
    user_input: str
    plan: dict
    response: str