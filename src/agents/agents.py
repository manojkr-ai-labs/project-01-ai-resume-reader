from crewai import Agent

from src.llm_provider import llm
from src.tools import employee_file_tool

research_agent = Agent(
    role="AI Research Engineer",
    goal="Research AI topics accurately.",
    backstory="You explain clearly.",
    llm=llm,
    tools=[employee_file_tool],
    verbose=True
)
writer_agent = Agent(
    role="Technical Writer",

    goal="""
    Convert research into professional documentation.
    """,

    backstory="""
    You are an experienced technical writer.
    You create clear, concise, and professional reports.
    """,

    llm=llm,

    verbose=True
)