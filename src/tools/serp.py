import os
from dotenv import load_dotenv
from crewai_tools import SerperDevTool

load_dotenv()

serper_dev_tool = SerperDevTool()
