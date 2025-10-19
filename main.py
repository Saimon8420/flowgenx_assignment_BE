from fastapi import FastAPI

# import router
from routers import chat,llm,db_ops,workflow
from database.models import create_conversation_table

app=FastAPI(title="FlowGenX Backend")

# Create table at startup
create_conversation_table()

#Register the router
app.include_router(chat.router)
app.include_router(llm.router)
app.include_router(db_ops.router)
app.include_router(workflow.router)

@app.get("/")
def root():
    return{"message":"FlowGenx API running successfully"}




