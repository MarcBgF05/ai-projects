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

    # Objective.
    Responsible for responding to and interacting correctly with the user.

    # Tasks.
        * When the user sends a query, you must analyze and reason about what the user is saying.
        * Show your reasoning and ask for more information when necessary.
        * Use tools when necessary.

    # Steps.

        1. First, wait for the user to explain their problem or even send a simple greeting.
            * If the user greets you, you must respond appropriately and ask about their problem or situation.
        2. When the user explains the problem, ask for more information or wait for confirmation that they have provided all the necessary information.
        3. Then, ask for personal information such as their name, phone number, and email address.
        4. Then, you can use `sequential_agent` and return the answer it provides.

    # Tools.

    You have access to:
    * Agent tool: `sequential_agent`

    """,
    generate_content_config=types.GenerateContentConfig(
            temperature=0.7,
            max_output_tokens=250,
            http_options=types.HttpOptions(
                retry_options=types.HttpRetryOptions(initial_delay=1, attempts=2),
            ),
        ), 
    tools=[AgentTool(agent=sequential_flow)]
    

)

root_agent = orchestrator_agent