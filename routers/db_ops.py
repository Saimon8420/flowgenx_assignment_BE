from fastapi import APIRouter,HTTPException
from services.db_service import save_conversation

router=APIRouter(prefix="/api/db",tags=["Database"])

@router.post("/save")
def save_to_db(payload:dict):
    user_message=payload.get("user_message")
    ai_response=payload.get("ai_response")
    if not (user_message and ai_response):
        raise HTTPException(status_code=400,detail="Both message and response required")
    save_conversation(user_message,ai_response)
    return{"status":"saved"}