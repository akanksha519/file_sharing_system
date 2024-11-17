from pydantic import BaseModel

class FileResponse(BaseModel):
    file_id: int
    file_name: str
    file_type: str
    uploaded_by: str
