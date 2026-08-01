from deepagents import create_deep_agent

from models import model, SYSTEM_PROMPT

from langgraph.checkpoint.memory import MemorySaver

from tools import *


#creating the agent and the thread that will store the conversation

spotify_agent = create_deep_agent(
    model = model,
    name = "JARVIS-MK2",
    tools = [search_track, play_song, pause_song, resume_song],
    system_prompt = SYSTEM_PROMPT,
    checkpointer = MemorySaver()
)

main_thread = {"configurable": {"thread_id": "thread1"}}