import time
import threading
import concurrent.futures

t1 = time.time()

def do_something(seconds):
    print(f'Waiting {seconds} second')
    time.sleep(seconds)
    return f'Sleeping done {seconds}'

# do_something()
# do_something()
# do_something()


# with concurrent.futures.ThreadPoolExecutor() as executor:
#     results = executor.map(do_something, range(2))

#     for result in results:
#         print(result)

def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(do_something, range(2))

        for result in results:
            print(result)


if __name__ == "__main__":
    main()
    t2 = time.time()

    dt = t2 - t1

    print(f"Program done in {dt} seconds")





# for i in range(5, 0, -1):
#     thread = threading.Thread(target=do_something, args=[i])
#     thread.start()
#     threads.append(thread)

# for thread in threads:
#     thread.join()


