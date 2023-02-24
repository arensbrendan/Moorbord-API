import asyncio
import user_server, login_server


if __name__ == "__main__":
    asyncio.run(user_server.serve())
    asyncio.run(login_server.serve())
