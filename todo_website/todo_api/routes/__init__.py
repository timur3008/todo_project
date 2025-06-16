from .todos import router as todos_router
from .auth import router as users_router

from ninja import NinjaAPI


api_router = NinjaAPI()

API = '/api/'

api_router.add_router(prefix=API, router=todos_router)
api_router.add_router(prefix=API, router=users_router)