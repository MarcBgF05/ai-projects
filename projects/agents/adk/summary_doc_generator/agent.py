from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.genai import types

summary_doc_generator = Agent(
    name="",
    description="",
    model="",
    instruction="",
    generate_content_config=types.GenerateContentConfig(
        temperature=0.7,
        max_output_tokens=250,
        http_options=types.HttpOptions(
            retry_options=types.HttpRetryOptions(initial_delay=1, attempts=2)
        )
    )

)

root_agent = summary_doc_generator