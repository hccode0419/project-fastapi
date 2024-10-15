from  fastapi import FastAPI, APIRouter, HTTPException

router = APIRouter(
    prefix="/user"
)


@router.get("/sign_up")
def sign_up():

@router.get("/log_in")
def log_in():


