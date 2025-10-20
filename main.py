from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# import router
from routers import chat,llm,db_ops,workflow
from database.models import create_conversation_table

app=FastAPI(title="FlowGenX Backend")

# Added CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Create table at startup
try:
    create_conversation_table()
except Exception as e:
    print(f"Error creating conversation table: {e}")
    raise # Re-raise the exception to prevent the app from starting

#Register the router
app.include_router(chat.router)
app.include_router(llm.router)
app.include_router(db_ops.router)
app.include_router(workflow.router)

@app.get("/")
def root():
    return{"message":"FlowGenx API running successfully"}




