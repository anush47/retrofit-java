from langgraph.graph import StateGraph, END
from state import AgentState
from agents import reasoning_agent, generation_agent, validation_agent
from nodes import analysis_tool_node

# Define the graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("reasoning", reasoning_agent)
workflow.add_node("analysis_tool", analysis_tool_node)
workflow.add_node("generation", generation_agent)
workflow.add_node("validation", validation_agent)

# Define edges
# Flow: Reasoning -> Analysis -> Generation -> Validation -> End
workflow.set_entry_point("reasoning")
workflow.add_edge("reasoning", "analysis_tool")
workflow.add_edge("analysis_tool", "generation")
workflow.add_edge("generation", "validation")
workflow.add_edge("validation", END)

# Compile the graph
app = workflow.compile()
