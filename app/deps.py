from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.utils.mail_config import settings

# ============================
# Repositories
# ============================

from app.repositories.admin_repo import AdminRepository
from app.repositories.chat_message_repository import ChatMessageRepository
from app.repositories.chat_session_repository import ChatSessionRepository
from app.repositories.contact_message_repository import ContactMessageRepository
from app.repositories.device_tokens_repository import DeviceTokenRepository
from app.repositories.notification_repository import NotificationRepository
from app.repositories.production_project_repository import ProductionProjectRepository
from app.repositories.profile_repository import ProfileRepository
from app.repositories.publications_repository import PublicationsRepository
from app.repositories.refreshToken_repository import RefreshTokenRepository
from app.repositories.repositories_repository import RepositoriesRepository
from app.repositories.skill_repository import SkillRepository

# ============================
# Services
# ============================

from app.services.auth_service import AuthService
from app.services.email_service import EmailService
from app.services.firebase_push_service import FirebasePushService
from app.services.image_service import ProfileImageService
from app.services.jwt_service import JWTService
from app.services.notification_service import NotificationService
from app.services.password_service import PasswordService

# ============================================================
# Repository Dependencies
# ============================================================

async def get_profile_repo(
    db: AsyncSession = Depends(get_db),
) -> ProfileRepository:
    return ProfileRepository(db)


async def get_skill_repo(
    db: AsyncSession = Depends(get_db),
) -> SkillRepository:
    return SkillRepository(db)


async def get_production_project_repo(
    db: AsyncSession = Depends(get_db),
) -> ProductionProjectRepository:
    return ProductionProjectRepository(db)


async def get_repositories_repo(
    db: AsyncSession = Depends(get_db),
) -> RepositoriesRepository:
    return RepositoriesRepository(db)


async def get_publications_repo(
    db: AsyncSession = Depends(get_db),
) -> PublicationsRepository:
    return PublicationsRepository(db)


async def get_chat_session_repo(
    db: AsyncSession = Depends(get_db),
) -> ChatSessionRepository:
    return ChatSessionRepository(db)


async def get_chat_message_repo(
    db: AsyncSession = Depends(get_db),
) -> ChatMessageRepository:
    return ChatMessageRepository(db)


async def get_contact_message_repo(
    db: AsyncSession = Depends(get_db),
) -> ContactMessageRepository:
    return ContactMessageRepository(db)


async def get_notification_repo(
    db: AsyncSession = Depends(get_db),
) -> NotificationRepository:
    return NotificationRepository(db)


async def get_device_token_repo(
    db: AsyncSession = Depends(get_db),
) -> DeviceTokenRepository:
    return DeviceTokenRepository(db)


async def get_admin_repo(
    db: AsyncSession = Depends(get_db),
) -> AdminRepository:
    return AdminRepository(db)


async def get_refresh_token_repo(
    db: AsyncSession = Depends(get_db),
) -> RefreshTokenRepository:
    return RefreshTokenRepository(db)

# ============================================================
# Infrastructure Services
# ============================================================

async def get_email_service() -> EmailService:
    return EmailService()


async def get_image_service() -> ProfileImageService:
    return ProfileImageService()


async def get_password_service() -> PasswordService:
    return PasswordService()


async def get_push_service() -> FirebasePushService:
    return FirebasePushService()

# ============================================================
# JWT Service
# ============================================================

def get_jwt_service() -> JWTService:
    return JWTService(
        secret_key=settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
        access_minutes=settings.ACCESS_TOKEN_MINUTES,
        refresh_days=settings.REFRESH_TOKEN_DAYS,
    )

# ============================================================
# Business Services
# ============================================================

async def get_auth_service(
    admin_repo: AdminRepository = Depends(get_admin_repo),
    refresh_token_repo: RefreshTokenRepository = Depends(get_refresh_token_repo),
    password_service: PasswordService = Depends(get_password_service),
):
    return AuthService(
        admin_repo=admin_repo,
        refresh_token_repo=refresh_token_repo,
        password_service=password_service,
        jwt_service=get_jwt_service(),
    )


async def get_notification_service(
    notification_repo=Depends(get_notification_repo),
    device_token_repo=Depends(get_device_token_repo),
    push_service=Depends(get_push_service),
    admin_repo=Depends(get_admin_repo),
):
    return NotificationService(
        notification_repo=notification_repo,
        device_token_repo=device_token_repo,
        push_service=push_service,
        admin_repo=admin_repo
    )