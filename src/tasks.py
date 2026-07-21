# from crewai import Task
# from agents import research_agent

# research_task = Task(
#     description="""
#     Use the Greeting Tool to greet Manoj.
#     """,

#     expected_output="""
#     A greeting message for Manoj.
#     """,

#     agent=research_agent
# )
# research_task = Task(
#     description="""
#     Use the Current Time Tool.

#     Tell me the current system time.

#     You MUST use the tool.
#     """,

#     expected_output="""
#     Current date and time.
#     """,

#     agent=research_agent
# ).

# Tasks 
# from crewai import Task
# from agents import research_agent

# # research_task = Task(
# #     description="""
# #     Use the Read Company File tool.

# #     Answer these questions:

# #     1. Who is the CEO?
# #     2. Where is the headquarters?
# #     3. When was the company founded?

# #     Use the tool before answering.
# #     """,

# #     expected_output="""
# #     A clear answer using information from the company file.
# #     """,

# #     agent=research_agent
# # )


from crewai import Task
from src.agents.agents import research_agent
from src.agents.agents import writer_agent

# research_task = Task(
#     description="""
#     Explain what CrewAI is.

#     Explain it in simple language.

#     Give one real-world example.
#     """,

#     expected_output="""
#     A beginner-friendly explanation with one practical example.
#     """,

#     agent=research_agent
# )

research_task = Task(
    description="""
    Read the employee file.

    Answer:

    1. Employee Name
    2. Experience
    3. Skills

    Use the tool before answering.
    """,

    expected_output="""
    Answer using the employee file.
    """,

    agent=research_agent
)
writing_task = Task(
    description="""
    Write a professional report based on the research findings.
    Include:

    - Introduction
    - Main Points
    - Conclusion
    """,

    expected_output="""
    A professional report in Markdown format.
    """,

    agent=writer_agent
)