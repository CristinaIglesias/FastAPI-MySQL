from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    openapi_tags=[{
        "name": "users",
        "description": "users routes"
    }]
)


app.include_router(user)
