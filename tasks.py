from crewai import Task
from tools import yt_tool 
from agents import blog_research_agent, blog_writer_agent


fetching_task = Task(
    description=(
        "Use the YoutubeVideoSearchTool to search and fetch content from the YouTube video.\n"
        "You MUST call the tool with BOTH of these fields:\n"
        " - 'youtube_video_url': use the exact value from the input variable {youtube_video_url}\n"
        " - 'search_query': use a short query summarizing what to extract, e.g. 'full transcript' or 'main concepts'."
    ),
    expected_output=(
        "The video title, URL, and the transcript or main content relevant to the query."
    ),
    tools=[yt_tool],
    agent=blog_research_agent,
)



write_task=Task(
    description="Read the fetched transcript and write a concise summary of the video",
   expected_output="A concise summary of the video",
   tools=[yt_tool],
   agent=blog_writer_agent,
   async_execution=False,
   output_file="summary.txt",
   context=[fetching_task]
)
