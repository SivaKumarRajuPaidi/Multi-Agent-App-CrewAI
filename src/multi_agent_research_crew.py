from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from src.llm import llm
from crewai_tools import SerperDevTool
from tools.serp import serper_dev_tool
import yaml

# # Load YAML Configuration
# with open("config.yaml", "r") as file:
#     config = yaml.safe_load(file)

from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, task, crew
from crewai_tools import SerperDevTool

@CrewBase
class ResearchCrew:
    """A crew for conducting research, summarizing findings, and fact-checking"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self):
        self.search_tool = SerperDevTool()
        self.llm = llm

    @agent
    def research_agent(self) -> Agent:
        return Agent(config=self.agents_config['research_agent'],
                     tools=[self.search_tool],
                     llm=self.llm)

    @agent
    def summarization_agent(self) -> Agent:
        return Agent(config=self.agents_config['summarization_agent'],
                     llm=self.llm)

    @agent
    def fact_checker_agent(self) -> Agent:
        return Agent(config=self.agents_config['fact_checker_agent'],
                     tools=[self.search_tool],
                     llm=self.llm)

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config['research_task'],
                    tools=[self.search_tool])

    @task
    def summarization_task(self) -> Task:
        return Task(config=self.tasks_config['summarization_task'])

    @task
    def fact_checking_task(self) -> Task:
        return Task(config=self.tasks_config['fact_checking_task'],
                    tools=[self.search_tool])

    @crew
    def crew(self) -> Crew:
        return Crew(agents=self.agents,
                    tasks=self.tasks,
                    process=Process.sequential)


research_crew = ResearchCrew()

result = research_crew.crew().kickoff(inputs={"topic": "The impact of AI on job markets"})
print("\nFinal Verified Summary:\n", result)

# ## Agents
# research_agent = Agent(
#     role=config["agents"]["research_agent"]["role"],
#     goal=config["agents"]["research_agent"]["goal"],
#     backstory=config["agents"]["research_agent"]["backstory"],
#     tools=[serper_dev_tool],
#     llm=llm,
#     verbose=True
# )

# summarization_agent = Agent(
#     role=config["agents"]["summarization_agent"]["role"],
#     goal=config["agents"]["summarization_agent"]["goal"],
#     backstory=config["agents"]["summarization_agent"]["backstory"],
#     llm=llm,
#     verbose=True
# )

# fact_checker_agent = Agent(
#     role=config["agents"]["fact_checker_agent"]["role"],
#     goal=config["agents"]["fact_checker_agent"]["goal"],
#     backstory=config["agents"]["fact_checker_agent"]["backstory"],
#     tools=[serper_dev_tool],
#     llm=llm,
#     verbose=True
# )

# ## Tasks
# research_task = Task(
#     description=config["tasks"]["research_task"]["description"],
#     agent=research_agent,
#     tools=[serper_dev_tool],
#     expected_output=config["tasks"]["research_task"]["expected_output"]
# )
# summarization_task = Task(
#     description=config["tasks"]["summarization_task"]["description"],
#     agent=summarization_agent,
#     expected_output=config["tasks"]["summarization_task"]["expected_output"],
# )
# fact_checking_task = Task(
#     description=config["tasks"]["fact_checking_task"]["description"],
#     agent=fact_checker_agent,
#     tools=[serper_dev_tool],
#     expected_output=config["tasks"]["fact_checking_task"]["expected_output"],
# )

# ## Crew
# research_crew = Crew(
#     agents=[research_agent, summarization_agent, fact_checker_agent],
#     tasks=[research_task, summarization_task, fact_checking_task],
#     process=Process.sequential,
#     verbose=True
# )

# result = research_crew.kickoff(inputs={"topic": "The impact of AI on job markets"})
# print("\nFinal Verified Summary:\n", result)

