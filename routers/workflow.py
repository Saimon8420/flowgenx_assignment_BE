from fastapi import APIRouter

router=APIRouter(prefix="/api",tags=["Workflow"])

@router.post("/save-or-update/workflow")
def save_workflow(payload:dict):
    return {"status":"workflow saved","workflow":payload}