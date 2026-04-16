import time
import requests
from concurrent.futures import ThreadPoolExecutor


URL="http://127.0.0.1:8000/slow"

def make_request(i):
    print(f"request {i} started at time {time.time():.2f}",flush=True)

    response=requests.get(URL)

    print(f"request {i} ended at time {time.time():.2f}",flush=True)

    return response.json()


def main():
    start=time.time()


    with ThreadPoolExecutor(max_workers=5) as executor:
        results=list(executor.map(make_request,range(5)))

    
    end=time.time()
    print(f"Total time taken is {end-start:.2f}")
    print(results)


if __name__=="__main__":
    main()
