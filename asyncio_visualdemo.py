import asyncio
import httpx
import time


URL="http://127.0.0.1:8000/slow"

async def make_request(i):
    print(f"Request {i} started at {time.time():.2f} should finish at ")

    async with httpx.AsyncClient() as client:
        response= await client.get(URL)

    print(f"Request {i} finished at {time.time():.2f}")
    return response.json()


async def main():
    print("main started")
    start=time.time()

    tasks=[make_request(i) for i in range(5)]
    results=await asyncio.gather(*tasks)

    end=time.time()

    print(f"\n Total time : {end-start:.2f} seconds")

if __name__=="__main__":
    asyncio.run(main())