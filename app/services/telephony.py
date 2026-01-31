from twilio.twiml.voice_response import VoiceResponse, Connect, Stream
from app.core.config import settings

def generate_connect_twiml(request_host: str):
    """
    Generate TwiML to connect the call to the Media Stream.
    The stream URL is derived from the request host.
    """
    response = VoiceResponse()
    
    # Optional greeting before connection
    response.say("Connecting you to the AI receptionist. Please wait.")
    
    # Start the stream
    connect = Connect()
    stream = Stream(url=f"wss://{request_host}/media-stream")
    connect.append(stream)
    response.append(connect)
    
    # If the stream ends, say goodbye
    response.say("The connection has ended. Goodbye.")
    
    return response.to_xml()
