# from crewai import Crew, Process

# from agents import research_agent
# from tasks import research_task

# research_crew = Crew(
#     agents=[research_agent],

#     tasks=[research_task],

#     process=Process.sequential,

#     verbose=True
# )
from crewai import Crew 

from src.agents.agents import research_agent, writer_agent
from src.tasks import research_task, writing_task

research_crew = Crew(
    agents=[research_agent, writer_agent],
    tasks=[research_task, writing_task],
    verbose=True
)