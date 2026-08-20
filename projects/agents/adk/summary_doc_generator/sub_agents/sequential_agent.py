from google.adk.agents.sequential_agent import SequentialAgent 
from .analyzer import analyzer_agent
from .writer import writer_agent


sequential_flow = SequentialAgent(
    name="sequential_flow_agent",
    description="You must sustain the sequential flow.",
    sub_agents=[analyzer_agent,writer_agent]
)
