import os
from dotenv import load_dotenv, find_dotenv
from crewai import LLM

def load_env():
    _ = load_dotenv(find_dotenv())

def get_gemini_api_key():
    load_env()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in environment variables.")
    return api_key

def get_serper_api_key():
    load_env()
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key:
        raise ValueError("SERPER_API_KEY not found in environment variables.")
    return api_key

def get_gemini_llm(model_name="gemini-2.5-flash", temperature=0.7):
    api_key = get_gemini_api_key()
    llm = LLM(
        model=model_name,
        api_key=api_key,
        temperature=temperature
    )
    return llm
