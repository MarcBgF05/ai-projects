from google.adk.agents import SequentialAgent 


sequential_flow = SequentialAgent(
    name="sequential_flow_agent",
    description="You must sustain the sequential flow.",
    sub_agents=[]
)
