from crewai import Agent
from config import llm, search_tool

def get_context_analyst_agent():
    return Agent(
        role="Forensic Digital Context & Timeline Analyst",
        goal="Determine if older information, historical media, or out-of-context assets are being maliciously repackaged as a current event.",
        backstory="Expert in temporal forensics. You analyze when images or text narratives first appeared on the web relative to the current timestamp to detect deceptive framing.",
        tools=[search_tool],
        llm=llm,
        verbose=True
    )
