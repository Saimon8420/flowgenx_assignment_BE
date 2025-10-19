from fastapi import APIRouter,HTTPException, Body
from services.llm_service import process_llm_message

router=APIRouter(prefix="/api/llm",tags=["LLM"])

@router.post("/process")
def process_llm(payload:dict = Body(..., example={"message": "Explain quantum computing in simple terms."})):
    message=payload.get("message")
    if not message:
        raise HTTPException(status_code=400,detail="Message required")
    response=process_llm_message(message)
    return {"response":response}