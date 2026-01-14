""" FastAPI router"""



from fastapi import APIRouter
from dataclasses import dataclass

router = APIRouter()

@dataclass
class ResponseBody:
    msg: str

@router.get("/smoke-test")
def prompt() -> ResponseBody:
    return {"msg": "Service Healthy"}

