import asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import engine
from app.models.publication import Publication
from app.models.Enums.PublicationType import PublicationType
from app.models.Enums.PublicationStatus import PublicationStatus


publications_data = [
    {
        "type": PublicationType.CONFERENCE_PAPER,
        "status": PublicationStatus.PUBLISHED,
        "title": "Noise-Robust Acoustic Modeling for Code-Switched Arabic–English Speech Recognition",
        "venue": "Interspeech",
        "year": 2025,
        "authors": [
            "Kyrillos Maher Nassief",
            "A. Collaborator",
            "S. Collaborator",
        ],
        "abstract": "We propose an acoustic modeling approach that improves recognition accuracy on code-switched Arabic–English speech under realistic noise conditions, combining self-supervised pretraining with targeted data augmentation.",
        "tags": ["ASR", "Code-Switching", "Low-Resource", "Arabic NLP"],
        "links": {
            "pdf": "#",
            "doi": "https://doi.org/10.0000/placeholder",
            "code": "https://github.com/kyrillos-nassief/cs-arabic-asr",
        },
        "image": None,
        "sort_order": 1,
    },
    {
        "type": PublicationType.WORKSHOP_PAPER,
        "status": PublicationStatus.PUBLISHED,
        "title": "Self-Supervised Speaker Representations for Low-Resource Diarization",
        "venue": "ICASSP Workshop on Self-Supervised Learning for Speech",
        "year": 2024,
        "authors": [
            "Kyrillos Maher Nassief",
            "M. Collaborator",
        ],
        "abstract": "An evaluation of self-supervised embeddings for speaker diarization in settings with limited labeled audio, showing competitive performance against fully supervised baselines.",
        "tags": ["Speaker Diarization", "Self-Supervised Learning"],
        "links": {
            "pdf": "#",
            "doi": "https://doi.org/10.0000/placeholder-2",
            "code": None,
        },
        "image": None,
        "sort_order": 2,
    },
    {
        "type": PublicationType.PREPRINT,
        "status": PublicationStatus.UNDER_REVIEW,
        "title": "Efficient On-Device ASR via Structured Pruning and Quantization",
        "venue": "arXiv",
        "year": 2025,
        "authors": ["Kyrillos Maher Nassief"],
        "abstract": "We study the latency/accuracy trade-off of pruning and INT8 quantization on transformer-based ASR models, targeting real-time inference on mobile hardware.",
        "tags": ["Model Compression", "Edge Deployment", "ASR"],
        "links": {
            "pdf": "https://arxiv.org/abs/0000.00000",
            "doi": None,
            "code": "https://github.com/kyrillos-nassief/efficient-asr",
        },
        "image": None,
        "sort_order": 3,
    },
    {
        "type": PublicationType.THESIS,
        "status": PublicationStatus.PUBLISHED,
        "title": "Multilingual End-to-End Speech Recognition for Low-Resource Dialects (BSc Thesis)",
        "venue": "Faculty of Engineering",
        "year": 2023,
        "authors": ["Kyrillos Maher Nassief"],
        "abstract": "An end-to-end exploration of multilingual ASR architectures applied to underrepresented Arabic dialects, with an emphasis on transfer learning from high-resource languages.",
        "tags": ["Multilingual ASR", "Transfer Learning", "Dialectal Arabic"],
        "links": {
            "pdf": "#",
            "doi": None,
            "code": "https://github.com/kyrillos-nassief/multilingual-asr-thesis",
        },
        "image": None,
        "sort_order": 4,
    },
    {
        "type": PublicationType.PREPRINT,
        "status": PublicationStatus.DRAFT,
        "title": "Streaming Conformer Variants for Real-Time Captioning",
        "venue": "arXiv (in preparation)",
        "year": 2026,
        "authors": [
            "Kyrillos Maher Nassief",
            "R. Collaborator",
        ],
        "abstract": "Comparing streaming-friendly Conformer variants for sub-300ms latency live captioning, with a focus on accuracy degradation under chunked attention.",
        "tags": ["Streaming ASR", "Conformer", "Live Captioning"],
        "links": {
            "pdf": None,
            "doi": None,
            "code": None,
        },
        "image": None,
        "sort_order": 5,
    },
]


async def seed_publications(session: AsyncSession):
    # OPTIONAL: clean dev database (safe for development only)
    # await session.execute("DELETE FROM publications")

    for pub in publications_data:
        session.add(
            Publication(
                type=pub["type"],
                status=pub["status"],
                title=pub["title"],
                venue=pub["venue"],
                year=pub["year"],
                authors=pub["authors"],
                abstract=pub["abstract"],
                tags=pub["tags"],
                links=pub["links"],
                image=pub["image"],
                sort_order=pub["sort_order"],
            )
        )

    await session.commit()
    print("✅ Publications seeded successfully")


async def main():
    async with AsyncSession(engine) as session:
        await seed_publications(session)


if __name__ == "__main__":
    asyncio.run(main())