from crewai import Agent
from config import llm, search_tool

def get_fact_checker_agent():
    return Agent(
        role="Lead OSINT Fact-Checking Journalist",
        goal="Identify specific factual assertions in the user input and cross-reference them with authoritative web databases.",
        backstory="You are a veteran metadata and open-source intelligence analyst. You look for structural inconsistencies, check fact-check archives, and flag unverified rumors.",
        tools=[search_tool],
        llm=llm,
        verbose=True
    )
