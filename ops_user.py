from fastapi import APIRouter, Depends, UploadFile, HTTPException
from app.services.auth import get_current_user
from app.services.file import save_file

router = APIRouter()

@router.post("/upload")
def upload_file(file: UploadFile, user=Depends(get_current_user)):
    if user.role != "ops":
        raise HTTPException(status_code=403, detail="Not authorized")
    if file.content_type not in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                                 "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                                 "application/vnd.openxmlformats-officedocument.presentationml.presentation"]:
        raise HTTPException(status_code=400, detail="Invalid file type")
    return save_file(file, user)
