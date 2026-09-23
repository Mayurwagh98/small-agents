from agno.agent import Agent
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.google import Gemini
from agno.tools.yfinance import YFinanceTools

load_dotenv()

def build_agent():
    return Agent(
        model=Gemini(id="gemini-3.6-flash"),
        markdown=True,
        tools=[DuckDuckGoTools(),YFinanceTools(all=True)],
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=["Format your response using markdown and use tables to display data where possible."],
    )

agent = build_agent()

agent.print_response("Share the NVDA stock price and analyst recommendations", markdown=True)