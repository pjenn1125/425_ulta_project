from fastapi import APIRouter
router = APIRouter(
    prefix="/auth",
    tags=["authentication"],
)

@router.get("/")
def auth_test():
    return {"message": "Auth working"
            }
