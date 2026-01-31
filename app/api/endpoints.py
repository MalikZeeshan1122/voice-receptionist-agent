from fastapi import APIRouter, Request, WebSocket
from fastapi.responses import Response
from app.services.telephony import generate_connect_twiml
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/incoming-call")
async def incoming_call(request: Request):
    """
    Handle incoming call from Twilio.
    Returns TwiML to connect to the Media Stream.
    """
    host = request.headers.get("host")
    twiml = generate_connect_twiml(host)
    return Response(content=twiml, media_type="application/xml")

@router.websocket("/media-stream")
async def media_stream(websocket: WebSocket):
    """
    Handle the WebSocket connection for the media stream.
    """
    await websocket.accept()
    logger.info("WebSocket connection accepted")
    
    try:
        while True:
            # Receive message from Twilio
            message = await websocket.receive_text()
            # For now, just keep the connection open and listen
            # In real implementation, this is where we send audio to STT
            # and receive audio from TTS.
            pass
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
    finally:
        logger.info("WebSocket connection closed")
