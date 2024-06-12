from fastapi import APIRouter, HTTPException
from ..controllers import addition_controller
from ..models import addition_model

router = APIRouter()

@router.post("/addition/")
async def addition(request: addition_model.AdditionRequest):
    try:
        response = addition_controller.process_batch(request.batchid, request.payload)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
