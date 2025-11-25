from langchain_core.messages import HumanMessage
from state import AgentState

async def validation_agent(state: AgentState, config):
    """
    The Gatekeeper. Validates the generated code.
    """
    print("Validation Agent: Validating code...")
    
    # Simulation: In a real scenario, this would:
    # 1. Compile the code
    # 2. Run linters
    # 3. Check compliance with the plan
    
    return {"messages": [HumanMessage(content="Code Validated")]}
