from crewai import Crew ,Process 
from agents import blog_research_agent,blog_writer_agent
from tasks import fetching_task,write_task


crew=Crew(
    agents=[blog_research_agent,blog_writer_agent],
    tasks=[fetching_task,write_task],
    process=Process.sequential,
    memeory=False,
    share_crew=True
)