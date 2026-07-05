
# from __future__ import annotations

# import uuid
# from datetime import datetime
# from typing import Optional

# from sqlalchemy import (
#     JSON,
#     Boolean,
#     DateTime,
#     Enum as SAEnum,
#     ForeignKey,
#     Integer,
#     String,
#     Text,
#     func,
# )
# from sqlalchemy.orm import (
#     DeclarativeBase,
#     Mapped,
#     mapped_column,
#     relationship,
# )

# from app.models.Enums.SkillCategory import SkillCategory
# from app.models.Enums.PublicationStatus import PublicationStatus
# from app.models.Enums.PublicationType import PublicationType


# # ============================================================
# # Base
# # ============================================================

# class Base(DeclarativeBase):
#     pass


# def _uuid() -> str:
#     return str(uuid.uuid4())


# # ============================================================
# # Profile
# # ============================================================

# class Profile(Base):
#     __tablename__ = "profiles"

#     id: Mapped[str] = mapped_column(
#         String(36),
#         primary_key=True,
#         default=_uuid,
#     )

#     name: Mapped[str] = mapped_column(String(200), nullable=False)
#     role: Mapped[str] = mapped_column(String(200), nullable=False)
#     tagline: Mapped[str] = mapped_column(Text, nullable=False)
#     location: Mapped[str] = mapped_column(String(150), nullable=False)
#     status: Mapped[str] = mapped_column(String(200), nullable=False)
#     email: Mapped[str] = mapped_column(String(255), nullable=False)

#     image: Mapped[Optional[str]] = mapped_column(
#         String(500),
#         nullable=True,
#         default=None,
#     )

#     links: Mapped[dict] = mapped_column(
#         JSON,
#         nullable=False,
#         default=dict,
#     )

#     bio: Mapped[list] = mapped_column(
#         JSON,
#         nullable=False,
#         default=list,
#     )

#     highlights: Mapped[list] = mapped_column(
#         JSON,
#         nullable=False,
#         default=list,
#     )

#     created_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True),
#         server_default=func.now(),
#     )

#     updated_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True),
#         server_default=func.now(),
#         onupdate=func.now(),
#     )

#     skills: Mapped[list["Skill"]] = relationship(
#         back_populates="profile",
#         cascade="all, delete-orphan",
#     )

#     notifications: Mapped[list["Notification"]] = relationship(
#         back_populates="profile",
#         cascade="all, delete-orphan",
#     )

# # ============================================================
# # Admin
# # ============================================================


# class Admin(Base):

#     __tablename__ = "admins"

#     id: Mapped[str] = mapped_column(
#         String(36),
#         primary_key=True,
#         default=_uuid,
#     )

#     email: Mapped[str] = mapped_column(
#         String(255),
#         unique=True,
#         nullable=False,
#     )

#     password_hash: Mapped[str] = mapped_column(
#         String(255),
#         nullable=False,
#     )

#     created_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True),
#         server_default=func.now(),
#     )

#     refresh_tokens: Mapped[list["RefreshToken"]] = relationship(
#         back_populates="admin",
#         cascade="all, delete-orphan",
#     )

# # ============================================================
# # Skill
# # ============================================================

# class Skill(Base):
#     """
#     Represents a skill or technology that a profile has experience with.
#     Used to populate the SkillsSection on the frontend.
#     """

#     __tablename__ = "skills"

#     id: Mapped[str] = mapped_column(
#         String(36),
#         primary_key=True,
#         default=_uuid,
#     )

#     profile_id: Mapped[str] = mapped_column(
#         ForeignKey("profiles.id"),
#         nullable=False,
#     )

#     category: Mapped[SkillCategory] = mapped_column(
#         SAEnum(SkillCategory),
#         nullable=False,
#     )

#     name: Mapped[str] = mapped_column(
#         String(150),
#         nullable=False,
#     )

#     sort_order: Mapped[int] = mapped_column(
#         Integer,
#         default=0,
#     )

#     profile: Mapped["Profile"] = relationship(
#         back_populates="skills"
#     )

# # ============================================================
# # Notification
# # ============================================================
# class Notification(Base):
#     __tablename__ = "notifications"

#     id: Mapped[str] = mapped_column(
#         String(36),
#         primary_key=True,
#         default=_uuid,
#     )

#     title: Mapped[str] = mapped_column(
#         String(50),
#         nullable=False,
#     )

#     content: Mapped[Optional[str]] = mapped_column(
#         String(500),
#         nullable=True,
#     )

#     is_read: Mapped[bool] = mapped_column(
#         Boolean,
#         default=False,
#         nullable=False,
#     )

#     profile_id: Mapped[str] = mapped_column(
#         ForeignKey("profiles.id"),
#         nullable=False,
#     )

#     created_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True),
#         server_default=func.now(),
#     )

#     profile: Mapped["Profile"] = relationship(
#         back_populates="notifications"
#     )



# # ============================================================
# # Contact Message
# # ============================================================
# class ContactMessage(Base):
#     """
#     Represents a single message sent through the contact form.
#     """
#     __tablename__ = "contact_messages"

#     id: Mapped[str] = mapped_column(String(36), primary_key=True, default=_uuid)

#     name: Mapped[str] = mapped_column(String(200), nullable=False)
#     email: Mapped[str] = mapped_column(String(255), nullable=False)
#     subject: Mapped[str] = mapped_column(String(300), nullable=False)
#     message: Mapped[str] = mapped_column(Text, nullable=False)

#     is_read: Mapped[bool] = mapped_column(Boolean, default=False)
#     created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
#     replies: Mapped[list["ContactMessageReply"]] = relationship(
#         back_populates="ContactMessage",
#         cascade="all, delete-orphan",
#     )


# # ============================================================
# # Contact Message Reply
# # ============================================================


# class ContactMessageReply(Base):
#     """
#     Represents a Reply For conatct From message .
#     """
#     __tablename__ = "contact_messages_reply"

#     id: Mapped[str] = mapped_column(String(36), primary_key=True, default=_uuid)
#     message_id: Mapped[str] = mapped_column(String(36), primary_key=True, default=_uuid)
#     name: Mapped[str] = mapped_column(String(200), nullable=False)
#     email: Mapped[str] = mapped_column(String(255), nullable=False)
#     subject: Mapped[str] = mapped_column(String(300), nullable=False)
#     message: Mapped[str] = mapped_column(Text, nullable=False)
#     created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


# # ============================================================
# # Publication
# # ============================================================

# class Publication(Base):
#     __tablename__ = "publications"

#     id: Mapped[str] = mapped_column(
#         String(36),
#         primary_key=True,
#         default=_uuid,
#     )

#     type: Mapped[PublicationType] = mapped_column(
#         SAEnum(PublicationType),
#         nullable=False,
#     )

#     status: Mapped[PublicationStatus] = mapped_column(
#         SAEnum(PublicationStatus),
#         nullable=False,
#     )

#     title: Mapped[str] = mapped_column(
#         Text,
#         nullable=False,
#     )

#     venue: Mapped[str] = mapped_column(
#         String(255),
#         nullable=False,
#     )

#     year: Mapped[int] = mapped_column(
#         Integer,
#         nullable=False,
#     )

#     authors: Mapped[list] = mapped_column(
#         JSON,
#         nullable=False,
#         default=list,
#     )

#     abstract: Mapped[str] = mapped_column(
#         Text,
#         nullable=False,
#     )

#     tags: Mapped[list] = mapped_column(
#         JSON,
#         nullable=False,
#         default=list,
#     )

#     links: Mapped[dict] = mapped_column(
#         JSON,
#         nullable=False,
#         default=dict,
#     )

#     image: Mapped[Optional[str]] = mapped_column(
#         String(500),
#         nullable=True,
#         default=None,
#     )

#     sort_order: Mapped[int] = mapped_column(
#         Integer,
#         default=0,
#     )

#     created_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True),
#         server_default=func.now(),
#     )

#     updated_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True),
#         server_default=func.now(),
#         onupdate=func.now(),
#     )


# # ============================================================
# # Repository
# # ============================================================

# class Repository(Base):
#     __tablename__ = "repositories"

#     id: Mapped[str] = mapped_column(
#         String(36),
#         primary_key=True,
#         default=_uuid,
#     )

#     name: Mapped[str] = mapped_column(
#         String(255),
#         nullable=False,
#     )

#     description: Mapped[str] = mapped_column(
#         Text,
#         nullable=False,
#     )

#     language: Mapped[str] = mapped_column(
#         String(100),
#         nullable=False,
#     )

#     stars: Mapped[int] = mapped_column(
#         Integer,
#         default=0,
#     )

#     forks: Mapped[int] = mapped_column(
#         Integer,
#         default=0,
#     )

#     topics: Mapped[list] = mapped_column(
#         JSON,
#         nullable=False,
#         default=list,
#     )

#     url: Mapped[str] = mapped_column(
#         String(500),
#         nullable=False,
#     )

#     homepage: Mapped[Optional[str]] = mapped_column(
#         String(500),
#         nullable=True,
#         default=None,
#     )

#     archived: Mapped[bool] = mapped_column(
#         Boolean,
#         nullable=False,
#         default=False,
#     )

#     image: Mapped[Optional[str]] = mapped_column(
#         String(500),
#         nullable=True,
#         default=None,
#     )

#     sort_order: Mapped[int] = mapped_column(
#         Integer,
#         default=0,
#     )

#     created_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True),
#         server_default=func.now(),
#     )

#     updated_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True),
#         server_default=func.now(),
#         onupdate=func.now(),
#     )


# # ============================================================
# # Production Project
# # ============================================================

# class ProductionProject(Base):
#     __tablename__ = "production_projects"

#     id: Mapped[str] = mapped_column(
#         String(36),
#         primary_key=True,
#         default=_uuid,
#     )

#     title: Mapped[str] = mapped_column(String(255), nullable=False)
#     organization: Mapped[str] = mapped_column(String(255), nullable=False)
#     period: Mapped[str] = mapped_column(String(100), nullable=False)
#     summary: Mapped[str] = mapped_column(Text, nullable=False)
#     role: Mapped[str] = mapped_column(String(150), nullable=False)

#     impact: Mapped[list] = mapped_column(
#         JSON,
#         nullable=False,
#         default=list,
#     )

#     stack: Mapped[list] = mapped_column(
#         JSON,
#         nullable=False,
#         default=list,
#     )

#     links: Mapped[dict] = mapped_column(
#         JSON,
#         nullable=False,
#         default=dict,
#     )

#     image: Mapped[Optional[str]] = mapped_column(
#         String(500),
#         nullable=True,
#         default=None,
#     )

#     confidential: Mapped[bool] = mapped_column(
#         Boolean,
#         nullable=False,
#         default=False,
#     )

#     sort_order: Mapped[int] = mapped_column(
#         Integer,
#         default=0,
#     )

#     created_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True),
#         server_default=func.now(),
#     )

#     updated_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True),
#         server_default=func.now(),
#         onupdate=func.now(),
#     )
# # ============================================================
# # Device Token
# #============================================================
# class DeviceToken(Base):
#     __tablename__ = "device_tokens"

#     id: Mapped[str] = mapped_column(
#         String(36),
#         primary_key=True,
#         default=_uuid,
#     )

#     profile_id: Mapped[str] = mapped_column(
#         ForeignKey("profiles.id"),
#         nullable=False,
#     )

#     token: Mapped[str] = mapped_column(
#         String(500),
#         nullable=False,
#         unique=True,
#     )

#     platform: Mapped[str] = mapped_column(
#         String(20),
#         nullable=False,
#     )


# #============================================================
# #Refresh Token
# #============================================================

# class RefreshToken(Base):

#     __tablename__ = "refresh_tokens"

#     id: Mapped[str] = mapped_column(
#         String(36),
#         primary_key=True,
#         default=_uuid,
#     )

#     admin_id: Mapped[str] = mapped_column(
#         ForeignKey("admins.id"),
#         nullable=False,
#     )

#     token: Mapped[str] = mapped_column(
#         String(512),
#         unique=True,
#         nullable=False,
#     )

#     revoked: Mapped[bool] = mapped_column(
#         Boolean,
#         default=False,
#         nullable=False,
#     )

#     expires_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True),
#         nullable=False,
#     )

#     created_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True),
#         server_default=func.now(),
#     )

#     admin: Mapped["Admin"] = relationship(
#         back_populates="refresh_tokens"
#     )