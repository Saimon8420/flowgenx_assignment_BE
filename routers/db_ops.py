from fastapi import APIRouter,HTTPException, Body
from services.db_service import save_conversation

router=APIRouter(prefix="/api/db",tags=["Database"])

@router.post("/save")
def save_to_db(payload:dict = Body(..., example={"user_message": "What is the capital of France?", "ai_response": "The capital of France is Paris."})):
    user_message=payload.get("user_message")
    ai_response=payload.get("ai_response")
    if not (user_message and ai_response):
        raise HTTPException(status_code=400,detail="Both message and response required")
    save_conversation(user_message,ai_response)
    return{"status":"saved"}