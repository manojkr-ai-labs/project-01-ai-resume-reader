Final Architecture
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

This is a real multi-agent workflow.