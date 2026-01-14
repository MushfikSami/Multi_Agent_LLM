from crewai import LLM 
llm=LLM(model='ollama/deepseek-r1:8b',
        base_url="http://localhost:11434",
        api_key='ollama')
