import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI API configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Flask configuration
DEBUG = True
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-change-in-production')

# Database configuration
DATABASE_NAME = 'troubleshoot.db' 