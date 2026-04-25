# Multi-Agents LLM

A CrewAI-based multi-agent system that fetches YouTube video transcripts and generates concise summaries.

## Architecture

Two agents work in sequence:

1. **Research Agent** — Uses the `YoutubeVideoSearchTool` to fetch the transcript of a given YouTube video.
2. **Writer Agent** — Reads the fetched transcript and writes a concise summary, writing it to `summary.txt`.

```
YouTube URL ──▶ [Research Agent] ──▶ Transcript ──▶ [Writer Agent] ──▶ summary.txt
```

## Setup

1. Install Ollama and pull the model:
   ```bash
   ollama pull deepseek-r1:8b
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your API keys in `.env` (see the file for the expected format).

4. Run the crew by executing the main entry point.

## Files

| File | Purpose |
|------|---------|
| `agents.py` | Define the two CrewAI agents |
| `tasks.py` | Define the fetching and writing tasks |
| `crew.py` | Wire agents and tasks into a CrewAI crew (sequential process) |
| `llm.py` | LLM configuration (default: `ollama/deepseek-r1:8b`) |
| `tools.py` | YouTube search tool setup |

## Tech Stack

- **Framework**: CrewAI
- **LLM**: deepseek-r1:8b via Ollama (localhost:11434)
- **Tools**: crewai_tools (YouTube transcript search)
