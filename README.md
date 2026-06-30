# Cold Email Replier Agent 🤖📧

An autonomous, multi-agent AI system built using **CrewAI** and wrapped in a clean **Streamlit** web interface. This tool automates the process of researching target companies (specifically SaaS) and drafting personalized, value-driven cold outreach sequences for AI automation services.

## 🚀 Features
* **CrewAI Orchestration:** Leverages specialized AI agents to handle background research and copywriting copy seamlessly.
* **Custom Tools:** Integrated with custom email sending and scraping utilities.
* **Streamlit UI:** An intuitive frontend allowing users to input what they offer, target specific roles (like Founders), and generate emails instantly.
* **LiteLLM / Groq Patching:** Custom wrapper to ensure stable completion calls across open-source LLM providers.

## 🛠️ Project Structure
```text
COLD_EMAIL_REPLIER_AGENT/
├── agents/             # Agent definitions and roles
├── config/             # Agent and Task configuration files (YAML/Prompts)
├── tools/              # Custom execution tools (e.g., email_sender.py)
├── cold.py             # Main Streamlit application and Crew orchestration
└── requirements.txt    # Python dependencies