import psycopg

from schema import CreateOrderRequest, get_settings

settings = get_settings()


async def create_order(request: CreateOrderRequest):
    result = ""
    async with await psycopg.AsyncConnection.connect(
        f"host={settings.postgres_host} port={settings.postgres_port} dbname={settings.postgres_dbname} user={settings.postgres_user} password={settings.postgres_pass}"
    ) as conn:
        # Open a cursor to perform database operations
        async with conn.cursor() as cur:
            query = f"INSERT INTO orders VALUES ({request.p_id}, {request.price}) RETURNING *"

            await cur.execute(query)

            result = await cur.fetchall()

            await conn.commit()

    return result
