# Multi-Agent AI Researcher
A multi-agent AI researcher using Groq, LangGraph, and Streamlit to find results from the web that matches the user's query and give a summarized answer based on those results. It uses the supervisor architecture to manage multiple agents, where the main agent delegates tasks to other agents.

## 🚀 Features

- **Agent-based Architecture**: Implements multiple specialized agents (e.g., Researcher, Analyst, Coordinator, Aggregator) coordinating together to solve research problems.  
- **Task Decomposition & Workflow Management**: The system splits an overarching research goal into subtasks, assigns them to agents, tracks progress and integrates results.  
- **Interactive Interface**: Provides a simple interface (CLI or web/app) for initiating research tasks and monitoring agent status in real time.  
- **Extensible & Modular**: Agents are modular and can be extended or replaced for different research themes, domains or data sources.  
- **Pre-built Example Use-Cases**: Includes one or more ready-to-run scenarios demonstrating full workflow from query to output.


Install the dependencies using pip:

```bash
pip install -r requirements.txt
```

# Run
Run the Streamlit app:

```bash
streamlit run multi_agent_researcher.py
```

## 🧠 System Overview
Agent Roles & Responsibilities

Coordinator Agent: Oversees workflow initiation, role assignment, progress monitoring and final aggregation of results.
Research Agent: Gathers data, literature, evidence, and sources relevant to the research topic.
Analysis Agent: Synthesizes gathered data, evaluates findings, generates insights, and performs reasoning.
Aggregator Agent: Compiles insights, formats the output (e.g., report, visualization), and exports results.

## Workflow Flow

User Input: Provide a research topic or problem statement.
Task Decomposition: Coordinator breaks down the task into subtasks (search, analysis, summarization).
Agent Execution: Each agent carries out its role; agents communicate their outputs to the coordinator or other agents.
Result Aggregation: Aggregator collates agent outputs into the final deliverable (e.g., markdown report, PDF, data summary).
Output: Display or save the result for the user.




## 🧑‍🎓 Author

**👨‍💻 Jay Rathod**  
*Software Engineer | AI & ML Trainer*  
📍 Ahmedabad, India  

🔗 [LinkedIn](https://www.linkedin.com/in/rathodjay3497/) | [GitHub](https://github.com/JayRathod341997)
