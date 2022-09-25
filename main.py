import uvicorn
import asyncio

from src.app import container_general, container_parser
from src.routers.lamoda import router as lamoda_router
from src.routers.twitch import router as twitch_router


container_general.app.include_router(lamoda_router)
container_general.app.include_router(twitch_router)

if __name__ == '__main__':
    asyncio.run(container_parser.lamoda.lamoda_parse())
    uvicorn.run(
        'src.app:container_general.app',
        host=container_general.config.service.host,
        port=container_general.config.service.port,
        reload=container_general.config.service.reload,
    )
