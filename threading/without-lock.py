#Race Condition (Multi-threading)

import threading
import time

# Initial account balance
balance = 100

def deposit(amount):
    global balance
    print(f"Initial Balance: ${balance}")
    temp_balance = balance + amount
    
    #Mimic a real life network request delay
    time.sleep(2)
    balance = temp_balance

thread1 = threading.Thread(target=deposit, args=(50,))
thread2 = threading.Thread(target=deposit, args=(50,))

thread1.start() 
thread2.start()

thread1.join()
thread2.join()

print(f"Final balance: ${balance}") #Final balance: $150