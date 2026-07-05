import asyncio

from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.repositories import Repository
from app.core.database import engine


async def seed_repositories(session: AsyncSession):
    repositories_data = [
        {
            "name": "efficient-asr",
            "description": (
                "Structured pruning + INT8 quantization toolkit for "
                "transformer-based ASR models, optimized for on-device inference."
            ),
            "language": "Python",
            "stars": 142,
            "forks": 23,
            "topics": [
                "speech-recognition",
                "model-compression",
                "pytorch",
                "onnx",
            ],
            "url": "https://github.com/kyrillos-nassief/efficient-asr",
            "homepage": None,
            "archived": False,
            "image": None,
            "sort_order": 1,
        },
        {
            "name": "cs-arabic-asr",
            "description": (
                "Training and evaluation pipeline for code-switched "
                "Arabic-English speech recognition, with augmentation recipes "
                "and pretrained checkpoints."
            ),
            "language": "Python",
            "stars": 98,
            "forks": 17,
            "topics": [
                "arabic-nlp",
                "code-switching",
                "speech",
                "huggingface",
            ],
            "url": "https://github.com/kyrillos-nassief/cs-arabic-asr",
            "homepage": None,
            "archived": False,
            "image": None,
            "sort_order": 2,
        },
        {
            "name": "spectro-viz",
            "description": (
                "Lightweight browser-based spectrogram and waveform visualizer "
                "for inspecting audio datasets during preprocessing."
            ),
            "language": "JavaScript",
            "stars": 64,
            "forks": 9,
            "topics": [
                "audio",
                "visualization",
                "data-tooling",
            ],
            "url": "https://github.com/kyrillos-nassief/spectro-viz",
            "homepage": "https://spectro-viz.example.dev",
            "archived": False,
            "image": None,
            "sort_order": 3,
        },
        {
            "name": "diarization-bench",
            "description": (
                "Benchmark suite comparing self-supervised vs. supervised "
                "speaker embeddings across low-resource diarization datasets."
            ),
            "language": "Python",
            "stars": 51,
            "forks": 6,
            "topics": [
                "speaker-diarization",
                "benchmark",
                "self-supervised-learning",
            ],
            "url": "https://github.com/kyrillos-nassief/diarization-bench",
            "homepage": None,
            "archived": False,
            "image": None,
            "sort_order": 4,
        },
        {
            "name": "streaming-conformer",
            "description": (
                "Reference implementation of chunked-attention streaming "
                "Conformer variants for low-latency live captioning."
            ),
            "language": "Python",
            "stars": 87,
            "forks": 14,
            "topics": [
                "conformer",
                "streaming",
                "real-time",
                "asr",
            ],
            "url": "https://github.com/kyrillos-nassief/streaming-conformer",
            "homepage": None,
            "archived": False,
            "image": None,
            "sort_order": 5,
        },
        {
            "name": "voicecmd-tinyml",
            "description": (
                "Wake-word and command recognition models tuned for ARM "
                "Cortex-M microcontrollers, with TFLite Micro deployment scripts."
            ),
            "language": "C++",
            "stars": 39,
            "forks": 5,
            "topics": [
                "tinyml",
                "embedded",
                "wake-word",
                "tflite",
            ],
            "url": "https://github.com/kyrillos-nassief/voicecmd-tinyml",
            "homepage": None,
            "archived": False,
            "image": None,
            "sort_order": 6,
        },
    ]

    # Development reset
  
    for repo_data in repositories_data:
            session.add(Repository(**repo_data))

    

    await session.commit()

    print("✅ Repositories seeded successfully")


async def main():
    async with AsyncSession(engine) as session:
        await seed_repositories(session)


if __name__ == "__main__":
    asyncio.run(main())