import os
from langchain_groq import ChatGroq
from crewai_tools import SerperDevTool

# LLM and Search Tools shared config
llm = ChatGroq(temperature=0.1, model_name="openai/gpt-oss-120b")
search_tool = SerperDevTool()
