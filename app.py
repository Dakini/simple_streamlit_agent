import streamlit as st
import asyncio
import sys
from pathlib import Path

# Add parent directory to path to import modules
import ingest
import search_agent
import logs

# Page configuration
st.set_page_config(
    page_title="AI Hero - Search Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🤖 AI Hero - Documentation Assistant")
st.markdown(
    "Ask questions about the documentation and get AI-powered answers with streaming responses."
)

# Initialize session state
if "initialized" not in st.session_state:
    with st.spinner("Loading search agent..."):
        text_index, vector_index = ingest.index_data()
        search_agent
        st.session_state.agent = search_agent.init_agent(text_index, vector_index)
        st.session_state.initialized = True

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Ask a question about the documentation...")

if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate and stream response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        try:
            # Get response from search agent
            response = asyncio.run(st.session_state.agent.run(user_prompt=user_input))
            full_response = response.output

            # Log the interaction
            logs.log_interaction_to_file(
                st.session_state.agent, response.new_messages()
            )

            # Display the response
            message_placeholder.markdown(full_response)

        except Exception as e:
            st.error(f"Error: {str(e)}")
            full_response = f"Error processing your request: {str(e)}"
            message_placeholder.markdown(full_response)

    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
