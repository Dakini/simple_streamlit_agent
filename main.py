import ingest
import search_agent
import logs

import asyncio


def initialise_index():
    print(f"Starting AI Assistant")
    print(f"Intilisaing Data Ingestion...")

    text_index, vector_index = ingest.index_data()
    print(f"Data ingested...")
    return text_index, vector_index


def initialise_agent(text_index, vector_index):
    print(f"Starting Search AI Assistant")
    s_agent = search_agent.init_agent(text_index, vector_index)

    print(f"Agent Intilised")
    return s_agent


def main():
    print("Hello from app!")
    text_index, vector_index = initialise_index()
    agent = initialise_agent(text_index, vector_index)

    print("\nReady to answer your questions!")
    print("Type 'stop' to exit the program.\n")

    while True:
        question = input("Your question: ")
        if question.strip().lower() == "stop":
            print("Goodbye!")
            break
        print("Processing your question...")
        response = asyncio.run(agent.run(user_prompt=question))
        logs.log_interaction_to_file(agent, response.new_messages())
        print("\nResponse:\n", response.output)
        print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    main()
