import asyncio

from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import engine
from app.models.production_project import ProductionProject


async def seed_production_projects(session: AsyncSession):
    projects_data = [
        {
            "title": "Real-Time Call Center Transcription Engine",
            "organization": "Confidential Client (Fintech)",
            "period": "2024 — Present",
            "summary": (
                "Production streaming ASR pipeline transcribing live customer "
                "support calls in Arabic and English with sub-second latency, "
                "feeding downstream sentiment and QA models."
            ),
            "role": "Lead Speech ML Engineer",
            "impact": [
                "Reduced word error rate by 18% relative on noisy call audio",
                "Cut end-to-end transcription latency to under 400ms",
                "Deployed across 3 regional contact centers",
            ],
            "stack": [
                "PyTorch",
                "NVIDIA NeMo",
                "Triton Inference Server",
                "Kubernetes",
                "gRPC",
            ],
            "links": {
                "caseStudy": "#",
                "demo": None,
            },
            "image": None,
            "confidential": True,
            "sort_order": 1,
        },
        {
            "title": "On-Device Voice Command Recognizer",
            "organization": "IoT Hardware Partner",
            "period": "2023 — 2024",
            "summary": (
                "Wake-word and short-command recognition model compressed to run "
                "fully on-device on ARM Cortex-M microcontrollers for a smart-home "
                "product line."
            ),
            "role": "ML Engineer (Speech)",
            "impact": [
                "Model footprint reduced to under 250KB via quantization",
                "98.2% wake-word detection accuracy in shipped firmware",
                "Shipped in a consumer hardware product, units sold at retail",
            ],
            "stack": [
                "TensorFlow Lite Micro",
                "C++",
                "Quantization-Aware Training",
            ],
            "links": {
                "caseStudy": "#",
                "demo": None,
            },
            "image": None,
            "confidential": False,
            "sort_order": 2,
        },
        {
            "title": "Live Captioning Service for University Lectures",
            "organization": "University Accessibility Initiative",
            "period": "2022 — 2023",
            "summary": (
                "Deployed a streaming captioning system for live lecture halls "
                "to support deaf and hard-of-hearing students, integrating domain "
                "adaptation for academic vocabulary."
            ),
            "role": "Contributor / Research Engineer",
            "impact": [
                "Used in 40+ live lecture sessions per semester",
                "Domain-adapted vocabulary improved technical-term WER by 22%",
            ],
            "stack": [
                "ESPnet",
                "WebRTC",
                "FastAPI",
                "Python",
            ],
            "links": {
                "caseStudy": "#",
                "demo": None,
            },
            "image": None,
            "confidential": False,
            "sort_order": 3,
        },
    ]

    # Development-only reset
    #await session.execute(delete(ProductionProject))

    for project_data in projects_data:
        session.add(ProductionProject(**project_data))

    await session.commit()

    print("✅ Production projects seeded successfully")


async def main():
    async with AsyncSession(engine) as session:
        await seed_production_projects(session)


if __name__ == "__main__":
    asyncio.run(main())