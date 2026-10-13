import asyncio
from dotenv import load_dotenv
load_dotenv()
from langchain.messages import HumanMessage
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent



stdio_server_params = StdioServerParameters(
    command="python",
    args=["/Users/bhavikagupta/Desktop/mcp_servers/own_mcp/servers/math_server.py"],
)
async def main():
    async with stdio_client(stdio_server_params) as (read,write):
        async with ClientSession(read_stream=read,write_stream=write) as session:
            await session.initialize()
            print("Session Initialized")
            tools = await load_mcp_tools(session)
            # print(tools)

            agent = create_agent(model="gpt-4o-mini",tools=tools)
            result = await agent.ainvoke({"messages":[HumanMessage(content="What is 54+2*3?")]})
            print(result["messages"][-1].content)

if __name__=="__main__":
    asyncio.run(main())