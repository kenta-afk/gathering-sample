from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

engine = create_async_engine("mysql+aiomysql://root:password@mysql/todo")

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