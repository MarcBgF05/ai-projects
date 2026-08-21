from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm 
from google.genai import types
from pydantic import BaseModel

from ...schemas.data import complete_data


writer_agent = Agent(
    name="writer_agent",
    description="You are in charge of generating a report",
    model=LiteLlm(model="openrouter/nvidia/nemotron-3.5-lightning:free"),
    instruction="""

    """,
    generate_content_config=types.GenerateContentConfig(
        temperature=0.7,
        max_output_tokens=250,
        http_options=types.HttpRetryOptions(max_delay=1,attempts=2)
    ),
    input_schema=complete_data
    
)