from crewai import Task

class TripTask:
    
    def local_task(self, agent, country, interests):
        task = Task(
            description = f"""
                As a local expert on this country - {country} you must compile an in-depth guide for someone travelling there and wanting to have the BEST TRIP ever!
                Gather information about the key attractions, local customs, and any special events, and daily activity recommendations. Find the best spots to go to, this kind of place only a local would know. You should also take into account the traveller's interest - {interests}. You can use the searchTool to aid in your completion of the task. 
                
                This guide should provide an in-depth overview of what the country has to offer, including hidden gems, cultural hotspots and must-visit landmarks. 
                
                The final answer should provide a comprehensive city guide, rich in cultural insights and practical tips to enhance their travel experience. 
                
                IMPORTANT:
                - You DO NOT delegate to other agents to complete the task.
                        """,
                agent = agent, 
                expected_output = "A in-depth paragraphs or text that provide a comprehensive city guide.",
        )
        return task
    
    def food_task(self, agent, country):
        task = Task(
            description = f"""
            You are a local food blogger who will identify the best local food spots in the country - {country}. 
            
            You are to look for the best food spots that will allow travellers to have an authentic dining experience and also recommend a list of must-try dishes and locations. You can use the searchTool to aid in your completion of the task. 
            
            You should provide the list of dishes as well as the location of the places. 
            
            IMPORTANT:
            - You DO NOT delegate to other agents to complete the task.
                        """,
            agent = agent, 
            expected_output = "A list of must-try dishes as well as a list of recommended food places for the travellers.",
        )
        return task
    
    def planner_task(self, agent, number_of_days, interest, food_task : Task, local_task : Task):
        task = Task(description = f"""
                    Based on the output from the previous tasks, you are tasked to create a personalised intinerary for travellers with the interests in {interest}. You are to expand this guide into a {number_of_days}-day travel itinerary with detailed per-day plans, including places to eat and a budget breakdown. 
                    
                    You MUST be as detailed as possible and suggest actual places to visit, actual hotels to stay and actual restaurants to go to. 
                    
                    This itinierary should cover all the aspects of the trip, from arrival to departure, integrating the city guide information with pracical travel logistics. 
                    
                    Your final output MUST be a complete expanded travel plan, formatted as markdown, encompassing a daily schedule, anticipated weather conditions, recommended clothing and items to pack, and a detailed budget, ensuring the BEST TRIP EVER> 
                    
                    IMPORTANT:
                    - You DO NOT delegate to other agents to complete the task.
                    - You DO NOT need to use any tools for this agent.
                    """,
        agent = agent, 
        expected_output = "A complete expanded travel plan formatted in markdown format.",
        context = [food_task, local_task],
        output_file = "plan.md"
        )
        return task
    
    def docs_task(self,agent):
        task = Task(
            description = """
                        You are to convert the markdown file into a word document. To complete the task, you will NEED to use the DOCSWriter tool assign to the agent. No input is needed to use the DOCSWriter tool.
                        """,
            agent = agent, 
            expected_output = "A string to determine if the document is successfully converted and saved."
        )
        return task
        
        
        
    
