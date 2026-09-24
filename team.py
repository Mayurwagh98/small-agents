from agno.team import Team
from agno.agent import Agent
from agno.models.google import Gemini
from dotenv import load_dotenv

load_dotenv()

eng_agent = Agent(
    name="English Agent",
    role="Answer the query in english",
)
hindi_agent = Agent(
    name="Hindi Agent",
    role="Answer the query in hindi",
)
chi_agent = Agent(
    name="Chinese Agent",
    role="Answer the query in chinese",
)

team = Team(
    name="Research Team",
    members=[eng_agent, hindi_agent,chi_agent],
    model=Gemini(id="gemini-3.6-flash"),
    instructions="Make sure all the agents reply to the query and not a single one"
)

team.print_response("What is the captial of india", stream=True)