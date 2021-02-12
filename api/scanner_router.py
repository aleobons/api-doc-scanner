import crud
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import StreamingResponse
import io

router = APIRouter()


@router.post("/", status_code=201)
async def scan_doc(file: UploadFile = File(...)):
    image_to_scan = await file.read()

    scanned_image = await crud.post(image_to_scan)

    return StreamingResponse(io.BytesIO(scanned_image), media_type="image/png")
