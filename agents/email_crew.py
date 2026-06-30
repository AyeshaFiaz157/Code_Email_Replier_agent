from crewai import Agent, Crew, LLM, Process, Task

from config.prompts import (
    RESEARCHER_BACKSTORY,
    RESEARCH_TASK_TEMPLATE,
    WRITE_TASK_TEMPLATE,
    WRITER_BACKSTORY,
)


def build_email_crew(context: dict) -> Crew:
    llm = LLM(
        model="groq/llama-3.3-70b-versatile",
        api_key=context.get("groq_key"),
    )

    company_name = context["company_name"] or _company_from_email(context["company_email"])

    researcher = Agent(
        role="Company Research Analyst",
        goal=f"Find the best angle to reach the CEO of {company_name}",
        backstory=RESEARCHER_BACKSTORY,
        llm=llm,
        verbose=True,
    )

    writer = Agent(
        role="Cold Email Outreach Specialist",
        goal="Write first-touch cold emails that get CEOs to respond",
        backstory=WRITER_BACKSTORY,
        llm=llm,
        verbose=True,
    )

    research_task = Task(
        description=RESEARCH_TASK_TEMPLATE.format(
            company_name=company_name,
            ceo_name=context["ceo_name"],
            company_email=context["company_email"],
            industry=context["industry"] or "Unknown",
            notes=context["notes"] or "General business introduction",
        ),
        expected_output="3-5 bullet points for CEO outreach personalization",
        agent=researcher,
    )

    write_task = Task(
        description=WRITE_TASK_TEMPLATE.format(
            your_name=context["your_name"] or "Sender",
            your_title=context["your_title"] or "Professional",
            your_email=context["your_email"] or "sender@example.com",
            ceo_name=context["ceo_name"],
            company_name=company_name,
            company_email=context["company_email"],
        ),
        expected_output="Subject line and cold email body in plain text",
        agent=writer,
        context=[research_task],
    )

    return Crew(
        agents=[researcher, writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
    )


def _company_from_email(email: str) -> str:
    domain = email.split("@")[-1].split(".")[0] if "@" in email else "the company"
    return domain.capitalize()
