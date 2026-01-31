from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "Voice Receptionist Agent"
    
    # Telephony
    TWILIO_ACCOUNT_SID: Optional[str] = None
    TWILIO_AUTH_TOKEN: Optional[str] = None
    TWILIO_PHONE_NUMBER: Optional[str] = None
    
    # STT
    DEEPGRAM_API_KEY: Optional[str] = None
    
    # LLM
    OPENAI_API_KEY: Optional[str] = None
    
    # TTS
    ELEVENLABS_API_KEY: Optional[str] = None
    
    class Config:
        env_file = ".env"

settings = Settings()
