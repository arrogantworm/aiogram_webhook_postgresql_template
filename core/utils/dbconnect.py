import asyncpg


class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def new_user(self, user_id, username):
        query = "INSERT INTO UserInfo (user_id, username) VALUES (%i, %s) " \
                "ON CONFLICT (user_id) DO UPDATE SET username=%s" % (user_id, username, username)
        await self.connector.execute(query)
