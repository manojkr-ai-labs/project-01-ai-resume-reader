from src.pdf_reader import read_pdf
from src.resume_parser import parse_resume

text = read_pdf("data/john-smith.pdf")

result = parse_resume(text)

print(result)