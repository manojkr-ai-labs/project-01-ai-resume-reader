# AI Resume Reader

A local resume-screening assistant. It reads a PDF resume and a job description, then asks a local language model to review the candidate the way an applicant-tracking reviewer would: matching skills, missing skills, strengths, weaknesses, and concrete recommendations.

The model runs through [Ollama](https://ollama.com/) on your machine. Resume text and job text stay local.

## What you get

Running the app against the sample resume (`data/john-smith.pdf`) and the sample role (`data/job-description.txt`) prints a Markdown review with these sections:

- ATS score
- Matching skills
- Missing skills
- Strengths
- Weaknesses
- Recommendations

The reviewer is instructed to use only what is written in the resume. If a skill is not stated, it is marked **Not Found** rather than inferred.

## How it works today

```
PDF resume ──► PDF reader ──┐
                            ├──► ATS analyzer (local LLM) ──► Markdown review
Job description ──► loader ─┘
```

1. **PDF reader** (`src/readers/pdf_reader.py`) extracts text from the resume with PyMuPDF.
2. **Job reader** (`src/readers/job_reader.py`) loads the role requirements as plain text.
3. **ATS analyzer** (`src/agents/ats_agent.py`) fills a fixed review prompt and calls the local model.
4. **Entry point** (`src/main.py`) runs that path on the sample files and prints the review.

A resume parser (`src/agents/resume_parser.py`) can also pull name, contact, skills, experience, education, and certifications into structured text. It is ready to call; the entry point currently goes straight to the ATS review.

## Target workflow

The screening flow above is the first slice of a larger multi-agent review. The intended pipeline is:

```
                 User
                   │
              Upload Resume
                   │
                   ▼
            PDF Reader Tool
                   │
                   ▼
           Resume Parser Agent
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
 Skill Agent   ATS Agent   Interview Agent
        │          │          │
        └──────────┼──────────┘
                   ▼
            Report Generator
                   │
                   ▼
          Markdown / PDF Report
```

| Stage | Role | In this repo |
| --- | --- | --- |
| PDF reader | Turn an uploaded resume into text | Used by `src/main.py` |
| Resume parser | Extract identity, skills, experience, education | Implemented, not called from `main` |
| ATS agent | Score the resume against one job description | Used by `src/main.py` |
| Skill agent | Judge skill depth separately from keyword match | Planned |
| Interview agent | Draft interview questions from the gaps | Prompt file only |
| Report generator | Combine the agent outputs into one Markdown or PDF report | Planned |

Alongside that pipeline, `src/crew.py` defines a small [CrewAI](https://crewai.com/) crew: a research agent reads `data/employee.txt` with a file tool, and a writer agent turns those findings into a Markdown report. That crew shows tool use and handoff between agents. It is not wired into `src/main.py`.

## Stack

| Piece | Choice |
| --- | --- |
| Language | Python |
| Agents and crews | CrewAI |
| Model access | CrewAI `LLM` client pointed at Ollama |
| PDF extraction | PyMuPDF |
| Config | `python-dotenv` |

Pinned packages are in `requirements.txt`. PDF reading also needs PyMuPDF, which is installed in the setup steps below.

## Project layout

```
src/
  main.py                 # runnable ATS review
  config.py               # MODEL and BASE_URL from .env
  llm_provider.py         # Ollama-backed LLM client
  crew.py                 # research + writer crew
  tasks.py                # crew tasks
  tools.py                # file-read tool used by the research agent
  agents/
    ats_agent.py          # resume vs job review
    resume_parser.py      # structured resume extraction
    agents.py             # CrewAI research and writer agents
  prompts/
    ats_prompt.py
    resume_prompt.py
    interview_prompt.py
  readers/
    pdf_reader.py
    job_reader.py
data/
  john-smith.pdf          # sample resume
  resume-sample1.pdf
  job-description.txt     # Senior Full Stack AI Engineer role
  employee.txt            # sample file for the crew tool
  company.txt
```

## Run it

You need Python 3.10 or newer, and [Ollama](https://ollama.com/) running locally with a model pulled (for example `llama3.1`).

From the project root in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install pymupdf
```

Create a `.env` file in the project root:

```
MODEL=llama3.1
BASE_URL=http://localhost:11434
```

`MODEL` is the Ollama model name. `BASE_URL` defaults to `http://localhost:11434` when it is omitted.

Pull the model if you have not already, then run the review:

```powershell
ollama pull llama3.1
python -m src.main
```

The command reads `data/john-smith.pdf` and `data/job-description.txt`, then prints the ATS review. To screen another pair, change those two paths in `src/main.py`.

## Design choices

- **Local model.** Screening uses Ollama so candidate documents are not sent to a hosted API.
- **Evidence-only review.** The ATS prompt forbids guessing. Missing skills stay missing.
- **Narrow first slice.** PDF text in, structured review out. Extra agents are separated so they can be added without rewriting the reader or the model client.
- **Tool-using crew, kept separate.** The CrewAI research and writer crew demonstrates an agent deciding to read a file and passing that result to a second agent. The hiring review does not depend on that demo.
