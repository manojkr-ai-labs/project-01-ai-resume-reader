# from src.pdf_reader import read_pdf
# from src.resume_parser import parse_resume

# text = read_pdf("data/john-smith.pdf")

# result = parse_resume(text)

# print(result)

from src.pdf_reader import read_pdf
from src.job_reader import read_job_description
from src.ats_agent import analyze_resume

resume = read_pdf("data/john-smith.pdf")

job = read_job_description("data/job-description.txt")

result = analyze_resume(resume, job)

print(result)