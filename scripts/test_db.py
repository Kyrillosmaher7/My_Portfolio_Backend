import asyncio
from sqlalchemy import text
from app.core.database import engine


async def test_connection():
    try:
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT 1"))
            value = result.scalar()

            print("✅ DB Connected Successfully!")
            print("Result:", value)

    except Exception as e:
        print("❌ DB Connection Failed!")
        print(e)


if __name__ == "__main__":
    asyncio.run(test_connection())