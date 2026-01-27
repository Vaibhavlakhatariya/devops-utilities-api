from fastapi import APIRouter, HTTPException
from services.aws_service import get_bucket_info


router = APIRouter()

@router.get("/s3", status_code=200)
def get_buckets():  
    
    try:
        bucket_info = get_bucket_info()
        return bucket_info
    except:
        raise HTTPException(
            status_code=500,
            detail="internal server error"
        )