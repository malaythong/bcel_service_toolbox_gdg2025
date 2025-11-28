import os
from google.adk.agents.llm_agent import Agent
from toolbox_core import ToolboxSyncClient

toolbox = ToolboxSyncClient("http://127.0.0.1:5000")


tools = toolbox.load_toolset('my_first_toolset')

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='You are the "BCEL Service Assistant," the primary customer support agent for Banque pour le Commerce Exterieur Lao Public (BCEL)',
    tools=tools,
)