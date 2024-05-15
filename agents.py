from crewai import Agent
from langchain_openai import ChatOpenAI
from langchain.agents import load_tools
from dotenv import load_dotenv, find_dotenv
from langchain_community.tools import DuckDuckGoSearchRun
from crewai_tools import SerperDevTool
from Tools.docswriter import Docswriter
import os

_ = load_dotenv(find_dotenv())
openai_api_key = os.getenv("OPENAI_API_KEY")
serper_api_key = os.getenv("SERPER_API_KEY")

search_tool = SerperDevTool()

# Loading Human Tools
human_tool = load_tools(["human"])

# Add Tools
searchTool = DuckDuckGoSearchRun()

# Define all agents 
class TripAgent:
    
    def __init__(self):
        self.llm_model = ChatOpenAI(model_name="gpt-3.5-turbo-0125",api_key = openai_api_key, temperature=0)
    
    def local_expert_agent(self):
        local_expert_agent = Agent(
            role = "Professional Guide",
            goal = "Provide best insights about the country",
            backstory = """
                        You are a knowledgeable local guide with extensive information aobut the country, it's attractions and would be able to provide insights and recommendations to the travellers.         
                        """,
            verbose = True, 
            llm = self.llm_model,
            tools = [search_tool]
        )
        return local_expert_agent
    
    def food_expert_agent(self):
        food_expert_agent = Agent(
            role = "Food Researcher",
            goal = "Find the best food option in the country",
            backstory = """
            You are a group of food enthusiats who love to explore local cuisines. You are always on the lookout for hidden gems and authentic dining experience. Your task and goal is to discover and recommend the best local food in the country of visit. 
                        """,
            verbose = True, 
            llm = self.llm_model,
            tools = [search_tool]
        )
        return food_expert_agent
    
    def travel_planner_agent(self):
        travel_planner_agent = Agent(
            role = "Travel Planner",
            goal = "Create personalised iteraries",
            backstory = """
                You are an expert in creating the most amazing travel itineraries with budget. You are a specialist in travel planning as you understand the diverse interests of travelers and aim to curate a unique and personalised experiences for each individual. 
                        """,
            verbose = True, 
            llm = self.llm_model, 
        )
        return travel_planner_agent
    
    def docs_formatter_agent(self):
        docs_formatter_agent = Agent(
            role = "Docs Formatter",
            goal = "Convert travel itineraries saved in Markdown format into Word Document",
            backstory = """
                        You are an expert in converting and formatting Markdown documents into word document to allow travellers to have a better view of their travel itinerary in Word Document. You are given the DOCSWriter Tool to aid in the completion of the task.
                        """,
            verbose = True, 
            llm = self.llm_model, 
            tools = [Docswriter().run]
        )
        return docs_formatter_agent
    