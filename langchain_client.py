import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI()

async def main():
    print("hello langchain mcp")

if __name__=="__main__":
    asyncio.run(main())
