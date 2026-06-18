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


@tool
def get_current_time() -> str:
    """returns the current local time"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


conversation_memory = ConversationMemory(max_messages=50)

assistant = Agent(
    name="personal_assistant",
    # openai
    # model="openai/gpt-4o",
    # model="openai/gpt-4o-mini",
    # model="openai/gpt-4-turbo",
    # model="openai/o1",
    # model="openai/o1-mini",
    # model="openai/o3-mini",

    # mistral
    # model="mistral/mistral-large-latest",
    # model="mistral/mistral-medium-latest",
    # model="mistral/mistral-small-latest",
    # model="mistral/open-mixtral-8x7b",

    # gemini
    model="google_gemini/gemini-1.5-flash",
    # model="google_gemini/gemini-1.5-pro",
    # model="google_gemini/gemini-2.0-flash",
    instructions=(
        "You are a concise personal assistant. Use tools when they help."
        "and remember useful user details across turns"
    ),
    tools=[get_current_time],
    memory=conversation_memory
)

# main entry point of the app
if __name__ == "__main__":
    print("Starting agent...")

    with AgentRuntime() as runtime:
        while True:
            prompt = input("You: ").strip()
            if prompt.lower() == "q":
                break
            if not prompt:
                continue

            result = run(assistant, prompt, runtime=runtime)
            print(f"Assistant: {result.output.get('result')}")
