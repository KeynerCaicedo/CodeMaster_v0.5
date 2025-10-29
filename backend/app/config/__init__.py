import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env")
load_dotenv(dotenv_path)
print("✅ .env loaded from:", dotenv_path)
print("🔑 OPENAI_API_KEY =", os.getenv("OPENAI_API_KEY"))
