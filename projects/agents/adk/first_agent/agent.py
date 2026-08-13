from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.genai import types
from google.adk.tools import google_search

first_agent = Agent(
    name="first_agent",
    description="Eres un agente de conocimiento general",
    model=LiteLlm(model="openrouter/nvidia/nemotron-3.5-lightning:free"),
    instruction="Eres un agente de conocimiento general, responde a las pregutnas que el usuario te haga, constrasta la información" \
    "a través de internet usando la tool `google_search`",
    tools=[google_search],
    generate_content_config=types.GenerateContentConfig(
        temperature=0.7,
        max_output_tokens=250,
        http_options=types.HttpOptions(
            retry_options=types.HttpRetryOptions(initial_delay=1, attempts=2),
        ),
    )

)

root_agent = first_agent
