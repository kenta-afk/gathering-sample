import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

# 環境変数からデータベース設定を取得
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD", "password")
MYSQL_HOST = os.getenv("MYSQL_HOST", "mysql")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "todo")

# データベースURLを構築
DATABASE_URL = f"mysql+aiomysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}"

engine = create_async_engine(DATABASE_URL)

AsyncSessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def get_db() -> AsyncSession:
    """
    データベースセッションを取得する依存性関数
    FastAPIのDependsで使用する
    """
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.close()