from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.genai import types
#from google.adk.tools import google_search

first_agent = Agent(
    name="first_agent",
    description="You are a general knowledge agent",
    model=LiteLlm(model="openrouter/nvidia/nemotron-3.5-lightning:free"),
    instruction= """
    You are a general knowledge agent, Answer the questions the user asks
    """,
 #   tools=[google_search], openrouter/nvidia/nemotron-3.5-lightning:free is not compatible with the google_search tool. 
    generate_content_config=types.GenerateContentConfig(
        temperature=0.7,
        max_output_tokens=250,
        http_options=types.HttpOptions(
            retry_options=types.HttpRetryOptions(initial_delay=1, attempts=2),
        ),
    )

)

root_agent = first_agent
