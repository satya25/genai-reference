# GenAI Reference Project – Smart Academic Assistant

## Overview
This repository serves as a **reference skeleton** for building agentic AI applications using Streamlit and MySQL.  
It demonstrates a **multi-step decision-making AI** that can fetch structured data or generate natural-language responses.

## Features
- Streamlit-based interactive interface
- Agent decides between database queries and LLM responses
- Sample database integration with MySQL
- Reusable prompt templates
- Modular folder structure for learning & extension

## Folder Structure
	config/ # LLM and DB configuration
	services/ # Agent and service logic
	database/ # Sample database schema and utilities
	ui/ # Streamlit components
	prompts/ # LLM prompt templates
	assets/ # Images, CSS, static data
	tests/ # Smoke / unit tests
	

## Getting Started
1. Install dependencies: `pip install -r requirements.txt`
2. Start XAMPP and configure sample database
3. Run the demo: `streamlit run app.py`

## Contribution
Refer to `CONTRIBUTING.md` for guidelines.

