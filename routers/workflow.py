from fastapi import APIRouter, Body

router=APIRouter(prefix="/api",tags=["Workflow"])

@router.post("/save-or-update/workflow")
def save_workflow(payload:dict = Body(..., examples=[{"nodes": [{"id": "1", "type": "chatInput", "data": {"label": "Chat Input"}}, {"id": "2", "type": "llmCall", "data": {"label": "LLM Call"}}], "edges": [{"id": "e1-2", "source": "1", "target": "2"}]}])):
    return {"status":"workflow saved","workflow":payload}