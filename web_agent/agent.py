import os
from google.adk import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="web_search_agent",
    model="gemini-2.0-flash",
    description="Agent to answer questions using Google Search.",
    instruction="You can answer your questions by searching the internet through the available tool.",
    tools=[google_search]
)
