from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent


load_dotenv()


@tool
def get_order_status(order_id: str) -> str:
    """Look up the status of an order by its id."""
    return f'{{"order_id": "{order_id}", "status": "shipped"}}'


agent = create_react_agent(ChatOpenAI(model="gpt-4o-mini"), [get_order_status])
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What is the status of order A-100?"}]}
)

print(result["messages"][-1].content or "No response")
