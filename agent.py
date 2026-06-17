"""
Script Name : agent.py
Description : Describe what this script does
Author      : @tonybnya
"""

import logging
from agentspan.agents import Agent, AgentRuntime, ConversationMemory, run, tool
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.WARNING)
logging.getLogger("agentspan").setLevel(logging.WARNING)
logging.getLogger("conductor").setLevel(logging.WARNING)

assistant = Agent(
    name="personal_assistant",
    model="openai/gpt-5.4-mini",
    # model="openai/gpt-4o-mini"
    instructions=(
        "You are a concise personal assistant. Use tools when they help."
        "and remember useful user details across turns"
    ),
    tools=[]
)
