# from crew import research_crew

# result = research_crew.kickoff()

# print("\n" + "=" * 50)
# print("FINAL ANSWER")
# print("=" * 50)
# print(result.raw)

# # from tools import greeting_tool

# # print(greeting_tool("Manoj"))
# from llm_config  import llm
# from src.llm_config import llm

# response = llm.call("Say hello in one sentence.")

# print(response)
# from src.llm_provider import llm

# print("=" * 50)
# print("Testing Ollama Connection")
# print("=" * 50)

# response = llm.call("Reply with only: Hello Manoj")

# print("\nResponse:")
# print(response)

# from src.crew import research_crew

# print("=" * 60)
# print("Running CrewAI Template")
# print("=" * 60)

# result = research_crew.kickoff()

# print("\n" + "=" * 60)
# print("FINAL ANSWER")
# print("=" * 60)

# print(result.raw)

# from src.tools import employee_file_tool
 
# from src.tools import employee_file_tool

# result = employee_file_tool.run(
#     file_path="data/employee.txt"
# )

# print(result)

from src.crew import research_crew

print("=" * 60)
print("Running CrewAI Template")
print("=" * 60)

result = research_crew.kickoff()

print("\n" + "=" * 60)
print("FINAL ANSWER")
print("=" * 60)

print(result.raw)