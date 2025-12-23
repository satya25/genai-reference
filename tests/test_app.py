from services.agent_service import AgentService

def test_agent_decision():
    agent = AgentService()
    query_db = "What is my score?"
    response, decision = agent.process_query(query_db)
    assert decision == "Database Query"
    
    query_llm = "How to improve grades?"
    response, decision = agent.process_query(query_llm)
    assert decision == "LLM Response"

    print("Smoke tests passed.")

if __name__ == "__main__":
    test_agent_decision()
