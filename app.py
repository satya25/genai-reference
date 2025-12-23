import streamlit as st
from services.agent_service import AgentService

st.set_page_config(page_title="Smart Academic Assistant", layout="centered")
st.title("Smart Academic Assistant Demo")

# Initialize Agent
agent = AgentService()

# Maintain chat history in session state
if "history" not in st.session_state:
    st.session_state.history = []

# User query
query = st.text_input("Enter your academic query:")

if st.button("Submit") and query.strip() != "":
    response, decision = agent.process_query(query)
    
    # Save to chat history
    st.session_state.history.append({
        "query": query,
        "decision": decision,
        "response": response
    })

# Display chat
for chat in st.session_state.history[::-1]:  # most recent first
    st.markdown(f"**You:** {chat['query']}")
    st.markdown(f"**Agent Decision:** {chat['decision']}")
    st.markdown(f"**Response:** {chat['response']}")
    st.markdown("---")
