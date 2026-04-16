from fastapi import FastAPI
import asyncio
import time

app=FastAPI()

@app.get("/slow")
async def slow():
    start=time.time()
    print(f"start:{start:.2f}")

    await asyncio.sleep(3)

    end=time.time()
    print(f"End: {end:.2f}")

    return {"start":start, "end":end}
