import search_tools
from pydantic_ai import Agent

system_prompt = """
You are a helpful assistant for a documenation. 

Use the search tool to find relevant information from the repo materials materials before answering questions.
Always search for relevant information before answering. 
If the first search doesn't give you enough information, try different search terms.

Make multiple searches if needed to provide comprehensive answers.

If you can find specific information through search, use it to provide accurate answers.
If the search doesn't return relevant results, let the user know and provide general guidance.
"""


def init_agent(text_index, vector_index):

    search_tool = search_tools.SearchTool(text_index, vector_index)

    agent = Agent(
        name="search_agent",
        instructions=system_prompt,
        tools=[search_tool.search],
        model="gpt-4o-mini",
    )

    return agent
