import threading
import time

# Therading is like setTimeOut if in JavaScript

done = False


def worker(name):
    count = 0
    while not done:
        time.sleep(1)
        count += 1
        print(f"{name}:{count}")


# worker()
# if i type worker without threading the input never be execute

# threading.Thread(target=worker).start()

tha = threading.Thread(target=worker, daemon=True, args=("A"))
thb = threading.Thread(target=worker, daemon=True, args=("B"))

tha.start()
thb.start()

# if program still running use daemon parameter to stop the program
# if the function target is have parameter use args parameter to fill it
# join() method is use if the thread finish, under join method code will be run


input("Press enter to quit")
done = True

tha.join()
thb.join()
print("Done...")

