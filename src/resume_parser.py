from src.llm_provider import llm
from src.prompts import RESUME_PARSER_PROMPT


def parse_resume(resume_text: str):

    prompt = f"""
{RESUME_PARSER_PROMPT}

Resume:

{resume_text}
"""

    return llm.call(prompt)