from agno.agent import Agent
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.google import Gemini

load_dotenv()

def build_agent():
    return Agent(
        model=Gemini(id="gemini-3.6-flash"),
        markdown=True,
        tools=[DuckDuckGoTools()],
        instructions="You are a helpful and expert travel agent.",
        add_datetime_to_context=True # to get the current date and time
    )

agent = build_agent()

agent.print_response("is it safe to travel to UAE today?")