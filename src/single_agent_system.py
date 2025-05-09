from crewai import Agent, Task, Crew
from src.llm import llm

senior_technical_writer = Agent(
    role="Senior Technical Writer",
    goal="""Craft clear, engaging, and informative technical 
    documentation for software products, ensuring that complex 
    concepts are easily understood by the target audience. 
    Collaborate with developers and product managers to gather 
    information and create user manuals, API documentation, 
    and online help resources. Maintain a consistent style and 
    tone across all documentation, adhering to company standards 
    and best practices.""",

    backstory="""You are an experienced technical writer
                 with expertise in simplifying complex
                 concepts, structuring content for readability,
                 and ensuring accuracy in documentation.""",

    llm=llm,

    verbose=True,
)

writing_task = Task(
    description="""Write a well-structured, engaging,
                   and technically accurate article
                   on {topic}.""",
    
    agent=senior_technical_writer, 
    
    
    expected_output="""A polished, detailed, and easy-to-read
                       article on the given topic.""",
)

code_reviewer = Agent(
    role="Senior Code Reviewer",
    goal="""Review code for bugs, inefficiencies, and 
            security vulnerabilities while ensuring adherence 
            to best coding practices.""",
    backstory="""You are a seasoned software engineer with years of 
                 experience in writing, reviewing, and optimizing 
                 production-level code in multiple programming languages.""",
    llm=llm,
    verbose=True
)

legal_reviewer = Agent(
    role="Legal Document Expert Reviewer",
    goal="""Review contracts and legal documents to 
            ensure compliance with applicable laws and 
            highlight potential risks.""",
    backstory="""You are a legal expert with deep knowledge 
                 of contract law, regulatory frameworks, 
                 and risk mitigation strategies.""",
    llm=llm,
    verbose=True
)

crew = Crew(
    agents=[senior_technical_writer],
    tasks=[writing_task],
    verbose=True
)

response = crew.kickoff(inputs={"topic":"AI Agents"})