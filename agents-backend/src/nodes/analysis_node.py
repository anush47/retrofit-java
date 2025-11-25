from langchain_core.messages import HumanMessage
from state import AgentState
from mcp.client.session import ClientSession

async def analysis_tool_node(state: AgentState, config):
    """
    Executes analysis tools via MCP.
    """
    session: ClientSession = config["configurable"].get("mcp_session")
    if session:
        print("Analysis Tool: Calling MCP...")
        try:
            result = await session.call_tool("get_java_version", {})
            content = result.content[0].text
            return {"messages": [HumanMessage(content=f"Java Version: {content}")]}
        except Exception as e:
            return {"messages": [HumanMessage(content=f"Error calling tool: {e}")]}
    return {"messages": [HumanMessage(content="No MCP session available")]}
