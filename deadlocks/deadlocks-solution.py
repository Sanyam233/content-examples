import threading

# Initialize two locks
lock1 = threading.Lock()
lock2 = threading.Lock()

# Function for the first thread
def task1():
    # Lock 1 is acquired first
    print("Task 1 acquiring lock 1...")
    lock1.acquire()
    print("Task 1 acquired lock 1.")
    
    # Lock 2 is acquired next
    print("Task 1 waiting for lock 2...")
    lock2.acquire()
    print("Task 1 acquired lock 2.")
    
    lock1.release()
    lock2.release()

# Function for the second thread
def task2():
    # Lock 1 is acquired first
    print("Task 2 waiting for lock 1...")
    lock1.acquire()
    print("Task 2 acquired lock 1.")

    # Lock 2 is acquired next
    print("Task 2 acquiring lock 2...")
    lock2.acquire()
    print("Task 2 acquired lock 2.")
    
    lock1.release()
    lock2.release()

# Create threads
threadA = threading.Thread(target=task1)
threadB = threading.Thread(target=task2)

# Start threads
threadA.start()
threadB.start()

# Wait for threads to complete
threadA.join()
threadB.join()