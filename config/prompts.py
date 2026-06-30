RESEARCHER_BACKSTORY = (
    "Expert at B2B outreach and executive communication. "
    "You research how to reach CEOs with messages that feel personal, relevant, and respectful of their time."
)

WRITER_BACKSTORY = (
    "You write first-touch cold emails to C-level executives. "
    "Your emails are concise, specific, and human — never generic AI fluff or pushy sales copy."
)

RESEARCH_TASK_TEMPLATE = """
Target company: {company_name}
CEO / recipient: {ceo_name}
Company email: {company_email}
Industry: {industry}
Sender pitch context: {notes}

Research angles for a first cold email that would resonate with this CEO.
Focus on: why now, why them, and one clear reason to reply.
"""

WRITE_TASK_TEMPLATE = """
Write a first-touch cold outreach email from {your_name} ({your_title}, {your_email})
to {ceo_name}, CEO at {company_name} ({company_email}).

This is NOT a reply — the CEO has not emailed us yet. We are reaching out cold.

Use the research insights. Requirements:
- Open with something specific to the CEO or company (not "I hope this finds you well")
- State clearly who you are and why you are reaching out
- One concrete value proposition or reason to meet
- Soft, low-friction call to action (e.g. 15-min call)
- Under 180 words

Output format exactly:
Subject: <subject line>

<body paragraphs>

Tone: professional, confident, warm — not salesy.
"""
