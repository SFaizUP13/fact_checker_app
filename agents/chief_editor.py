from crewai import Agent
from config import llm

def get_chief_editor_agent():
    return Agent(
        role="Chief Verification Editor",
        goal="Synthesize findings from all agents to produce an unbiased, high-integrity truth report with an exact numerical risk profile.",
        backstory="The final editorial authority. You compile disparate research notes into clear, highly digestible summaries backed strictly by hyperlinked citation records.",
        llm=llm,
        verbose=True
    )
