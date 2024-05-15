import docx
from crewai_tools import tool 
from Markdown2docx import Markdown2docx

class Docswriter:
    @tool("DOCSWriter Tool")
    def run() -> str:
        """
        This tool will provide support in converting markdown documents to word document. 
        No input is needed for this Tool. 
        """
        project = Markdown2docx('plan')
        project.eat_soup()
        project.save()
        return "Sucesfully saved Word Document. Refer to file path '../plan.docs' to view the Full Itinerary."


    
    
    