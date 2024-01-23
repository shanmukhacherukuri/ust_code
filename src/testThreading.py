import threading

def dog():
    print("Dog function called")

def cat():
    print("Cat function called")

def tiger():
    print("tiger function called")

def thread():
    f1 = threading.Thread(target=dog())
    f2 = threading.Thread(target=cat())
    f3 = threading.Thread(target=tiger())
    #Start All 3 threads
    f1.start()
    f2.start()
    f3.start()

    f1.join(2)
    f2.join(2)
    f3.join(2)

def main():
    print("All threads are started")
    thread()
    print("All threads are ended")

if __name__ == "__main__":
    main()