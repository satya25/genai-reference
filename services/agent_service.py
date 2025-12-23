import re
import subprocess
from database.db_utils import fetch_from_db
from prompts.system_prompts import GENERAL_ADVICE_PROMPT
from services.weather_service import WeatherService  # new import

class AgentService:
    def __init__(self):
        # Initialize weather service
        self.weather_service = WeatherService()

    def process_query(self, query: str):
        """
        Minimal agent logic:
        - Database query for scores/timetable
        - Weather API for weather-related queries
        - LLM (local) for everything else
        """
        query_lower = query.lower()
        
        # Database queries
        if "score" in query_lower or "timetable" in query_lower:
            result = fetch_from_db(query_lower)
            decision = "Database Query"
            return result, decision
        
        # Weather queries
        elif "weather" in query_lower:
            # For demo, using hardcoded coordinates (e.g., New Delhi)
            result = self.weather_service.get_weather(latitude=28.6139, longitude=77.2090)
            decision = "Weather API"
            return result, decision
        
        # Local LLM for other queries
        else:
            result = self.call_local_llm(query)
            decision = "LLM Response (local)"
            return result, decision

    def call_local_llm(self, query: str):
        """
        Calls local Ollama LLM and cleans output
        """
        prompt = GENERAL_ADVICE_PROMPT + "\n\nQuestion: " + query
        try:
            output = subprocess.check_output(
                ["ollama", "run", "phi3:mini", prompt],
                stderr=subprocess.STDOUT,
                universal_newlines=True,
                encoding="utf-8"
            )
            # Remove ANSI sequences (spinners, colors)
            clean_output = re.sub(r'\x1B[@-_][0-?]*[ -/]*[@-~]', '', output)
            # Remove leading spinner characters
            clean_output = re.sub(r'^[⠋⠙⠹⠸⠼⠴⠦⠧⠇\s]+', '', clean_output)
            return clean_output.strip()
        except subprocess.CalledProcessError as e:
            return f"[LLM Error] {e.output}"
