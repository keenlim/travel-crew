from crewai import Process, Crew
from agents import TripAgent
from tasks import TripTask

class My_Crew:
    def __init__(self, country='Vancouver', interests='Shopping', numberofdays='7'):
        self.country = country
        self.interests = interests
        self.numberofdays = numberofdays
    
    def run(self):
        # Define Agents
        tripAgent = TripAgent()
        local_expert_agent = tripAgent.local_expert_agent()
        food_expert_agent = tripAgent.food_expert_agent()
        travel_planner_agent = tripAgent.travel_planner_agent()
        docs_formatter_agent = tripAgent.docs_formatter_agent()
        
        # Define Tasks
        tripTask = TripTask()
        local_task = tripTask.local_task(local_expert_agent, self.country, self.interests)
        food_task = tripTask.food_task(food_expert_agent, self.country)
        travel_planner_task = tripTask.planner_task(travel_planner_agent, self.numberofdays, self.interests, food_task, local_task)
        docs_task = tripTask.docs_task(docs_formatter_agent)
        
        # Create and Run the Crew
        my_crew = Crew(
            agents = [local_expert_agent, food_expert_agent, travel_planner_agent,docs_formatter_agent],
            tasks = [local_task, food_task, travel_planner_task, docs_task],
            verbose = True, 
            process = Process.sequential, 
        )
        
        result = my_crew.kickoff()
        return result

