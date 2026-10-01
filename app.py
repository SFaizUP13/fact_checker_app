import streamlit as st
import os

# Streamlit UI Page Setup
st.set_page_config(page_title="AI Truth Guard", page_icon="🛡️", layout="wide")

# Inject environment variables from Streamlit Cloud Secrets Dashboard first
if "GROQ_API_KEY" in st.secrets and "SERPER_API_KEY" in st.secrets:
    os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
    os.environ["SERPER_API_KEY"] = st.secrets["SERPER_API_KEY"]
else:
    st.error("⚠️ Cloud Secrets missing! Please configure GROQ_API_KEY and SERPER_API_KEY in the Streamlit Cloud Dashboard settings.")
    st.stop()

# Modular Imports
from crewai import Crew, Process
from agents.fact_checker import get_fact_checker_agent
from agents.context_analyst import get_context_analyst_agent
from agents.chief_editor import get_chief_editor_agent
from tasks import create_tasks

# UI Copy
st.title("🛡️ AI Truth Guard: Modular Multi-Agent Engine")
st.markdown("---")

user_input = st.text_area("Paste Text, Social Links, or Image URLs to audit:", height=150)
start_button = st.button("Launch Decentralized Agents 🔍", type="primary", use_container_width=True)

if start_button:
    if not user_input.strip():
        st.warning("Please provide input data.")
    else:
        with st.spinner("🕵️‍♂️ Standby. Isolated agents are firing up their subroutines and parsing databases..."):
            
            # Instantiating agents from separate files
            agent_fact = get_fact_checker_agent()
            agent_context = get_context_analyst_agent()
            agent_editor = get_chief_editor_agent()
            
            # Instantiating partitioned tasks
            agent_tasks = create_tasks(user_input, agent_fact, agent_context, agent_editor)
            
            # Assembling modular Crew
            truth_crew = Crew(
                agents=[agent_fact, agent_context, agent_editor],
                tasks=agent_tasks,
                process=Process.sequential
            )
            
            try:
                result = truth_crew.kickoff()
                st.success("🎯 Multi-Agent Analysis Complete!")
                st.markdown(result.raw)
            except Exception as e:
                st.error(f"Execution crash: {e}")
