import os

def fork_exec_with_grep():
    pid = os.fork()
    if pid == 0:
        # Child process

        os.execl("/usr/bin/grep", "grep", "standard", "test.txt")
    else:
        # Parent process
        os.wait()  # Wait for child to terminate
        print("Parent process completed")

if __name__ == "__main__":
    fork_exec_with_grep()
