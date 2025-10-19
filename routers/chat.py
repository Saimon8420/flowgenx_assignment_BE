from fastapi import APIRouter, HTTPException, Body
from services.llm_service import process_llm_message
from services.db_service import save_conversation

router=APIRouter(prefix="/api/chat",tags=["Chat"])

@router.post("/message")
def handle_message(payload: dict = Body(..., example={"message": "Hello, how are you?"})):
    user_message=payload.get("message")
    if not user_message:
        raise HTTPException(status_code=400,detail="Message required")
    
    ai_response=process_llm_message(user_message)
    if ai_response.startswith("Error"):
        raise HTTPException(status_code=500, detail=ai_response)
    
    save_conversation(user_message,ai_response)
    return {"user_message":user_message,"ai_response":ai_response}