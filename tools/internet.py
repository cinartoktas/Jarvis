from tavily import TavilyClient
from config import TAVILY_API_KEY

client = TavilyClient(api_key=TAVILY_API_KEY)


def internette_arat(sorgu):

    cevap = client.search(
        query=sorgu,
        search_depth="advanced",
        max_results=5
    )

    return cevap