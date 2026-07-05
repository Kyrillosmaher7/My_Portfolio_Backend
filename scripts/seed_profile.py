import asyncio
from email.mime import text

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import engine
from app.models.profile import Profile
from app.models.skill import Skill
from app.models.Enums.SkillCategory import SkillCategory
from scripts.test_db import test_connection


async def seed_profile_and_skills(session: AsyncSession):
    profile = Profile(
        name="Kyrillos Maher Nassief",
        role="AI Researcher · Speech & Audio Intelligence",
        tagline=(
            "I build systems that turn raw acoustic signal into language and meaning — "
            "researching at the edge of speech recognition, and shipping it where it has "
            "to survive real microphones, real accents, and real noise."
        ),
        location="Cairo, Egypt",
        status="Open to MSc/PhD positions and industry research roles",
        email="kyrillos.nassief@example.com",
        links={
            "github": "https://github.com/kyrillos-nassief",
            "linkedin": "https://linkedin.com/in/kyrillos-nassief",
            "scholar": "https://scholar.google.com/citations?user=placeholder",
            "orcid": "https://orcid.org/0000-0000-0000-0000",
            "huggingface": "https://huggingface.co/kyrillos-nassief",
            "cv": "/cv-kyrillos-nassief.pdf",
        },
        bio=[
            "I'm an AI researcher focused on automatic speech recognition (ASR), speaker representation learning, and low-resource acoustic modeling.",
            "My work sits between research and production systems.",
            "I'm currently looking for MSc/PhD opportunities in speech & spoken language processing.",
        ],
        highlights=[
            {"label": "Years in speech/audio ML", "value": "4+"},
            {"label": "Publications & preprints", "value": "5"},
            {"label": "Production ASR systems shipped", "value": "3"},
            {"label": "Open-source repos maintained", "value": "9"},
        ],
    )

    skills_data = {
        SkillCategory.RESEARCH: [
            "Automatic Speech Recognition (ASR)",
            "Speaker Diarization & Verification",
            "Self-Supervised Audio Representation Learning",
            "Low-Resource & Code-Switched Speech",
            "Sequence-to-Sequence Modeling",
            "Acoustic & Language Model Fusion",
        ],
        SkillCategory.ML_FRAMEWORKS: [
            "PyTorch",
            "TensorFlow",
            "HuggingFace Transformers",
            "ESPnet",
            "NVIDIA NeMo",
            "Kaldi",
            "ONNX Runtime",
        ],
        SkillCategory.LANGUAGES_TOOLS: [
            "Python",
            "C++",
            "Bash",
            "CUDA (applied)",
            "Docker",
            "FastAPI",
            "gRPC",
            "Git / DVC",
        ],
        SkillCategory.DATA_INFRA: [
            "Distributed training (multi-GPU)",
            "Audio data pipelines",
            "Model quantization & on-device deployment",
            "MLOps / experiment tracking (W&B, MLflow)",
        ],
        SkillCategory.SOFT: [
            "Technical writing & peer review",
            "Research mentorship",
            "Cross-functional collaboration (research ↔ product)",
            "Conference presentation",
        ],
    }

    sort_order = 1

    for category, skills in skills_data.items():
        for skill_name in skills:
            profile.skills.append(
                Skill(
                    category=category,
                    name=skill_name,
                    sort_order=sort_order,
                )
            )
            sort_order += 1

    session.add(profile)
    await session.commit()

    print("✅ Profile and skills seeded successfully")


async def main():
    await test_connection()

    async with AsyncSession(engine) as session:
        await seed_profile_and_skills(session)


if __name__ == "__main__":
    asyncio.run(main())

