from fastapi import FastAPI
from app.routes import ops_user, client_user
from app.config import settings

app = FastAPI(title="Secure File Sharing System")

# Include routes
app.include_router(ops_user.router, prefix="/ops", tags=["Ops User"])
app.include_router(client_user.router, prefix="/client", tags=["Client User"])
