import threading
import time

NUM_PROCESSES = 3

choosing = [False] * NUM_PROCESSES
numbers = [0] * NUM_PROCESSES
shared_resource = 0

def max_number():
    return max(numbers)

def bakery_algorithm(process_id):
    global shared_resource, choosing, numbers

    for _ in range(2):
        choosing[process_id] = True
        numbers[process_id] = max_number() + 1
        choosing[process_id] = False

        for other_id in range(NUM_PROCESSES):
            while choosing[other_id]:
                pass
            while numbers[other_id] != 0 and (
                (numbers[other_id] < numbers[process_id]) or
                (numbers[other_id] == numbers[process_id] and other_id < process_id)
            ):
                pass

        print(f"Process {process_id} entering critical section")
        shared_resource += 1
        print(f"Process {process_id} modified shared_resource to {shared_resource}")
        time.sleep(1)

        numbers[process_id] = 0
        print(f"Process {process_id} leaving critical section")
        time.sleep(1)

threads = []
for i in range(NUM_PROCESSES):
    thread = threading.Thread(target=bakery_algorithm, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Final value of shared_resource: {shared_resource}")
