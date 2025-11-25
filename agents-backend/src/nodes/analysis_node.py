from langchain_core.messages import HumanMessage
from state import AgentState
from mcp import ClientSession
from mcp.client.sse import sse_client
import os

async def analysis_node(state: AgentState, config):
    """
    Executes tools via MCP.
    """
    print("Analysis Tool: Calling MCP...")
    
    sse_url = os.getenv("MCP_SERVER_URL", "http://localhost:8080/mcp/sse")
    
    try:
        async with sse_client(sse_url) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                
                # For now, just call get_java_version as a test
                result = await session.call_tool("get_java_version", arguments={})
                
                content = result.content[0].text
                print(f"Output from analysis_tool:\n  {content}")
                
                return {"messages": [HumanMessage(content=f"Analysis Result: {content}")]}
    except Exception as e:
        print(f"Error calling tool: {e}")
        return {"messages": [HumanMessage(content=f"Error calling tool: {e}")]}
