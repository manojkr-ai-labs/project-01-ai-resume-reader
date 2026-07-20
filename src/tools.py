# Task 1
# from crewai.tools import tool

# @tool("Greeting Tool")
# def greeting_tool(name: str) -> str:
#     """
#     Returns a greeting message.
#     """
#     return f"Hello {name}! Welcome to CrewAI."

# Task 2
# from crewai.tools import tool
# from datetime import datetime

# @tool("Current Time Tool")
# def current_time_tool() -> str:
#     """
#     Returns the current system time.
#     """
#     return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# from crewai.tools import tool

# @tool("Read Company File")
# def read_company_file() -> str:
#     """
#     Reads the company information file.
#     """

#     with open("data/company.txt", "r", encoding="utf-8") as file:
#         return file.read()
    
# started 
from crewai_tools import FileReadTool

employee_file_tool = FileReadTool(file_path="data/employee.txt")
    