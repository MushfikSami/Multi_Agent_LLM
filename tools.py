import os 
from crewai_tools import YoutubeVideoSearchTool 

os.environ.setdefault("OPENAI_API_KEY", "dummy")
yt_tool=YoutubeVideoSearchTool()