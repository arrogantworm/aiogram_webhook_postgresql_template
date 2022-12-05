import asyncpg


class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def new_user(self, user_id, username):
        query = 'INSERT INTO UserInfo VALUES (?, ?) ON CONFLICT (user_id) DO UPDATE SET username=?', (user_id, username, username)
        await self.connector.execute(query)
        