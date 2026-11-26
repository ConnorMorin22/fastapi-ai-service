from fastapi import APIRouter, Depends
from .services import AIService, get_ai_service
from .models import Query

router = APIRouter(
    prefix="/api",
    tags=["api"],
    responses={404: {"description": "Not Found"}}
)

@router.post("", tags=["api"])
def get_ai_response(body: Query, service: AIService = Depends(get_ai_service)):
    return service.answer(body)