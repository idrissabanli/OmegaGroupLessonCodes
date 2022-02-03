import time
import threading
import concurrent.futures

import requests

def download_image(i):
    with open(f'images/image_{i}.png', 'wb') as f:
        res = requests.get('https://picsum.photos/200/300') 
        f.write(res.content)


def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(download_image, range(100))

        # for result in results:
        #     print(result)


if __name__ == "__main__":
    t1 = time.time()
    main()
    t2 = time.time()
    dt = t2-t1

    print(f"Program done in {dt} seconds")


