#!/bin/bash

# ======================================================
# Shell script to create the skeleton for genai-reference
# ======================================================

echo "Creating folder structure and empty files for genai-reference..."

# Folders
mkdir -p config services ui database prompts tests assets

# Empty Python files
touch app.py
touch config/llm_config.py
touch services/agent_service.py
touch database/db_utils.py
touch prompts/system_prompts.py
touch ui/components.py
touch tests/test_app.py

# README and requirements
touch README.md
touch requirements.txt
touch .gitignore

# Optional: create assets subfolders
mkdir -p assets/images assets/css assets/data

echo "Folder structure created successfully!"
echo "Your genai-reference skeleton is ready."

# to execute:  chmod +x setup_skeleton.sh
# ./setup_skeleton.sh
