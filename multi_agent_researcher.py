import re
import streamlit as st
from dotenv import load_dotenv
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_supervisor
import  os
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

def clean_text(text: str):
    cleaned_text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    return cleaned_text.strip()


# ✅ Use Groq model
model = ChatGroq(
    model="qwen/qwen3-32b",  # or "mixtral-8x7b" / "gemma-7b"
    temperature=0,
    api_key=groq_api_key
)

query_refiner_prompt = (
    "You are a query refiner agent.\n\n"
    "INSTRUCTIONS:\n"
    "- Refine the user's query to make it more specific and actionable\n"
    "- Respond ONLY with the refined query, do NOT include any other text."
)

research_prompt = (
    "You are a research agent.\n\n"
    "INSTRUCTIONS:\n"
    "- Assist ONLY with research-related tasks, DO NOT do anything else\n"
    "- After you're done with your research, respond to the supervisor directly\n"
    "- Respond ONLY with the summary of the results, do NOT include ANY other text."
)

supervisor_prompt = (
    "You are a supervisor agent.\n\n"
    "INSTRUCTIONS:\n"
    "- Manage the workflow between the query refiner and researcher agents\n"
    "- Use the Query Refiner Agent to correct typos and enhance the query for better search relevance\n"
    "- Use the Research Agent to retrieve up-to-date information from the web\n"
    "- Respond ONLY with the final response, do NOT include any other text."
)

query_refiner_agent = create_react_agent(
    model=model,
    tools=[],
    prompt=query_refiner_prompt,
    name="query_refiner_agent"
)

research_agent = create_react_agent(
    model=model,
    tools=[DuckDuckGoSearchRun()],
    prompt=research_prompt,
    name="research_agent"
)

supervisor_agent = create_supervisor(
    model=model,
    agents=[query_refiner_agent, research_agent],
    prompt=supervisor_prompt
)

app = supervisor_agent.compile()


# ✅ Chat UI
st.title("🔎 Multi-Agent Researcher (Groq + LangGraph)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input box
if user_query := st.chat_input("Ask me anything..."):
    # Store user message
    st.session_state["messages"].append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    # Call supervisor agent
    result = app.invoke({
        "messages": [{"role": "user", "content": user_query}]
    })

    research_result = clean_text(result["messages"][-1].content)

    # Store assistant reply
    st.session_state["messages"].append({"role": "assistant", "content": research_result})
    with st.chat_message("assistant"):
        st.markdown(research_result)
