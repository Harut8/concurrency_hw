import os

def fork_exec_with_arguments():
    pid = os.fork()
    if pid == 0:
        # Child process
        os.execl("/bin/echo", "echo", "Hello from the child process")
    else:
        # Parent process
        os.wait()  # Wait for child to terminate
        # !!! os.wait() if this line will be after the line below it will work in different way
        print("Parent process done")

if __name__ == "__main__":
    fork_exec_with_arguments()
