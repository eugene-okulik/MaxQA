import time


def main():
    print("Hello world!")
    print("Are you still alive?")
    t = time.localtime()
    current_time = time.strftime("%Y-%m-%d | %H:%M:%S", t)
    print(current_time)
    time.sleep(5)


while True:
    main()
