import asyncpg
import os
from fastapi import FastAPI
from contextlib import asynccontextmanager

db_connect = os.getenv("URL_DATABASE")

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.db_pool = await asyncpg.create_pool(dsn=db_connect)
    yield
    await app.state.db_pool.close()

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def get_zones():
    async with app.state.db_pool.acquire() as conn:
        query = """WITH cte AS (SELECT id,
                MAX(CASE WHEN period = 1 THEN name END) AS first_period,
                MAX(CASE WHEN period = 2 THEN name END) AS second_period,
                MAX(CASE WHEN period = 1 THEN forecast END) AS first_forecast,
                MAX(CASE WHEN period = 2 THEN forecast END) AS second_forecast
                FROM dev.forecasts
                GROUP BY id)

                SELECT z.name, z.state, c.first_period, c.second_period,
                c.first_forecast, c.second_forecast,
                ST_AsText(g.geom) AS geom
                FROM dev.zones z
                JOIN cte c
                ON z.id = c.id
				JOIN dev.geometries g
				ON z.id = g.id;"""
        rows = await conn.fetch(query)
        return [dict(row) for row in rows]

