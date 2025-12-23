# GenAI Reference Project – Requirements & Specifications

## Project Title
Smart Academic Assistant (Agentic AI Demo)

## Purpose
Demonstrate an agentic AI application that interacts with students, answers academic queries, and decides which tool to use (database or LLM) to respond intelligently.

---

## Functional Requirements

1. **User Interface (Streamlit)**
   - Input box for student queries
   - Output area to display AI responses
   - Display “Agent Decision” (DB / LLM / Other)

2. **Database Interaction**
   - Connect to MySQL (XAMPP)
   - Store sample data for:
     - Student IDs, courses, scores, timetables
   - Retrieve data based on user query

3. **Agentic AI**
   - Decide whether to:
     - Query database (structured data)
     - Call LLM (unstructured/advisory)
   - Chain actions if needed (e.g., fetch + summarize)

4. **Prompt Management**
   - Store reusable prompt templates
   - System-level instructions for LLM

5. **Services Layer**
   - Encapsulate agent logic
   - Handle DB & LLM calls

6. **Testing**
   - Minimal smoke tests
   - Validate DB connection
   - Validate agent decision routing

---

## Non-Functional Requirements

- Clean folder structure
- Easily extensible for new teams
- Ready to deploy on Streamlit Cloud
- Minimal setup required (Python 3.11, XAMPP)
- Well-documented for student learning

---

## Optional / Future Enhancements

- Multi-turn conversation
- Agent explanation of decisions
- Integration with external APIs (library / campus info)
