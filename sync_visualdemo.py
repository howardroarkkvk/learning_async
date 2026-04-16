import httpx
import time
import requests

URL="http://127.0.0.1:8000/slow"

def main():

    print("make request started")

    start_time=time.time()
    for i in range(5):
        print(f"Request {i} started at {time.time():.2f} ")
        response=requests.get(URL)
        print(f"Request {i} finished at {time.time():.2f}")
        print(response.json())
    end_time=time.time()
    
    print(f"overall time it has taken is : {end_time-start_time:.2f}")


if __name__=="__main__":
    main()

    