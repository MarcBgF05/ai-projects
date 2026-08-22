from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm 
from google.genai import types
from pydantic import BaseModel

from ...schemas.data import complete_data
from ...tools.doc_generator import document_generator


writer_agent = Agent(
    name="writer_agent",
    description="You are in charge of generating a report",
    model=LiteLlm(model="openrouter/nvidia/nemotron-3.5-lightning:free"),
    instruction="""
    # Objective
    Generate a report.

    # Data Handling
    You will receive data from the `analyzer_agent` in the following format:

        {
            "user_data": {
                "name": "Marcos",
                "email": "marcos@example.com"
            },
            "problem": "The user is having problems configuring a Python environment.",
            "tips": "Verify the Python version, create a virtual environment, check the installed dependencies"
        }

    # Steps
    1. Take the data received from the `analyzer_agent` and pass it to the `document_generator` tool.
    2. Return the response provided by the `document_generator` tool to the user.
    
    """,
    generate_content_config=types.GenerateContentConfig(
        temperature=0.7,
        max_output_tokens=250,
        http_options=types.HttpRetryOptions(max_delay=1,attempts=2)
    ),
    input_schema=complete_data,
    tools=[document_generator]
    
)