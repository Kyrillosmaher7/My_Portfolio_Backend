from fastapi import FastAPI , HTTPException

from app.api.health import router as health_router
from app.api.v1.profile import router as profile_router
from app.api.v1.skill import router as skill_router
from app.api.v1.publication import router as publication_router
from app.api.v1.project import router as project_router
from app.api.v1.repositories import router as repos_router
from app.api.v1.contact_message import router as messages_router
from app.api.v1.auth import router as auth_router
from app.api.v1.admin import router as admin_router
from app.api.v2.notifications import router as notification_router
from app.api.v2.websockest import router as web_socket
from app.core.handler import (
    app_exception_handler,
    global_exception_handler,
    http_exception_handler
)
from app.core.exceptions import AppException
from app.middlewares.request_logger import RequestLoggingMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="PhD Portfolio API")


app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads",
)

# middleware
app.add_middleware(RequestLoggingMiddleware)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://myportoflio-production.up.railway.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(health_router)
app.include_router(profile_router)
app.include_router(skill_router)
app.include_router(publication_router)
app.include_router(project_router)
app.include_router(repos_router)
app.include_router(messages_router)
app.include_router(auth_router)
app.include_router(notification_router)
app.include_router(admin_router)
app.include_router(web_socket)
# Exception handlers
app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)

@app.get("/")
async def root():
    return {
        "message": "API running"
    }
