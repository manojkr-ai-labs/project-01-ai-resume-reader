from src.llm_provider import llm
# from src.ats_prompt import ATS_PROMPT
from src.prompts.ats_prompt import ATS_PROMPT


def analyze_resume(resume, job):

    prompt = f"""
{ATS_PROMPT}

Resume

{resume}


Job Description

{job}
"""

    return llm.call(prompt)