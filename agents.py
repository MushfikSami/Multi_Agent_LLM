from crewai import Agent 
from tools import yt_tool
from llm import llm 

blog_research_agent = Agent(
    role="You are an expert YouTube content researcher.",
    goal=(
        "Given a YouTube video URL in the variable {youtube_video_url}, "
        "call the YoutubeVideoSearchTool exactly once with JSON arguments:\n"
        "{\n"
        '  "youtube_video_url": "{youtube_video_url}",\n'
        '  "search_query": "full transcript"\n'
        "}\n"
        "Do not leave any field empty and do not ask the user for the URL."
    ),
    verbose=True,
    backstory="You specialize in extracting accurate transcripts and details from educational YouTube videos.",
    tools=[yt_tool],
    allow_delegation=False,
    llm=llm,
)

blog_writer_agent = Agent(
    role="You are an expert YouTube content writer.",
    goal=(
        "Given the transcript and metadata of a YouTube video (already fetched by another agent), "
        "write a concise summary in clear language. Do not ask the user for a video URL; "
        "always work only with the provided transcript and context."
    ),
    verbose=True,
    memory=False,
    backstory="You have extensive experience in writing summaries and analyzing content.",
    tools=[yt_tool],
    allow_delegation=False,
    llm=llm,
)
