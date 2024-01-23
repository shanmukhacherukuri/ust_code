import datetime
import time
def time_now():
    print("time now", datetime.datetime.now())
def add():
    print("add of 2 and 5 is:", 2+5)
def sub():
    print("sub of 10 and 6 is", 10-6)

def sleep():
    print("initiates sleep for 2 secs", datetime.datetime.now())
    time.sleep(3)
    print("Sleep completed ----------", datetime.datetime.now())

def main():
    time_now()
    add()
    sub()
    sleep()

if __name__ == "__main__":
    main()