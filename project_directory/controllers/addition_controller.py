import multiprocessing
from datetime import datetime
from typing import List
from .models.addition_model import AdditionRequest, AdditionResponse

def perform_addition(numbers: List[int]) -> int:
    return sum(numbers)

def process_batch(batchid: str, payload: List[List[int]]) -> AdditionResponse:
    started_at = datetime.now().isoformat()
    with multiprocessing.Pool() as pool:
        result = pool.map(perform_addition, payload)
    completed_at = datetime.now().isoformat()
    return AdditionResponse(
        batchid=batchid,
        response=result,
        status="complete",
        started_at=started_at,
        completed_at=completed_at
    )
