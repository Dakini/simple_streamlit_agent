from typing import List, Any
from ingest import embed_query


class SearchTool:

    def __init__(self, text_index, vector_index):
        self.text_index = text_index
        self.vector_index = vector_index

    def search(self, query: str) -> List[Any]:
        """
        Perform a d search on the repo readme files index.

        Args:
            query (str): The search query string.

        Returns:
            List[Any]: A list of up to 10 search results returned by the repo readme files.
        """
        print(query)
        text_result = self.text_index.search(query, num_results=5)
        q = embed_query(query)
        vector_result = self.vector_index.search(q, num_results=5)

        seen_ids = set()
        current_results = []

        for doc in text_result + vector_result:
            if doc["filename"] not in seen_ids:
                seen_ids.add(doc["filename"])
                current_results.append(doc)

        return current_results
