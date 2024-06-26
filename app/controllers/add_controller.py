from fastapi import APIRouter,HTTPException
from app.models import AddRequest,AddResponse
from datetime import datetime
from app.utils.addition import makeaddition
from app.utils.logger import log_information, log_error


add_endpoint = APIRouter()

@add_endpoint.post('/add', response_model= AddResponse)
async def add(request:AddRequest):
    start_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    #log startting time
    log_information(f"processing batch with batchid {request.batchid} start time is {start_time}")
    try:
        result = makeaddition(request.payload)
        end_time =datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        #log ending time
        log_information(f"processing batch with batchid {request.batchid} end time is {end_time}")
        return AddResponse(
            batchid = request.batchid,
            response = result,
            status ='completed',
            started_at = start_time,
            completed_at = end_time
        )
    except Exception as err:
        # log error
        raise HTTPException (status_code= 500, detail=str(err))