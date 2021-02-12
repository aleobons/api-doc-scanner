import api.scanner_router as scanner_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(scanner_router.router, prefix="/scan-doc", tags=["scan-doc"])