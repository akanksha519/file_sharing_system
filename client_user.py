from fastapi import APIRouter, Depends
from app.services.auth import authenticate_user
from app.services.file import generate_download_link, list_files

router = APIRouter()

@router.post("/login")
def login(data: dict):
    return authenticate_user(data["email"], data["password"])

@router.get("/files")
def list_uploaded_files(user=Depends(get_current_user)):
    return list_files(user)

@router.get("/download/{file_id}")
def download_file(file_id: int, user=Depends(get_current_user)):
    return generate_download_link(file_id, user)
