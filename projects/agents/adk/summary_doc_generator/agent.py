from google.genai import types
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.sequential_agent import sequential_flow

orchestrator_agent = Agent(
    name="orchestrator_agent",
    description="You are a main agent in charge of orchestrating and interacting with the user.",
    model=LiteLlm(model="openrouter/nvidia/nemotron-3.5-lightning:free"),
    instruction="""
    # Objetctive. 
    To provide answers 
    

    """,
    generate_content_config=types.GenerateContentConfig(
        temperature=0.7,
        max_output_tokens=250,
        http_options=types.HttpOptions(
            retry_options=types.HttpRetryOptions(initial_delay=1, attempts=2)
        )
    ),
    tools=[AgentTool(agent=sequential_flow)]
    

)

root_agent = orchestrator_agent