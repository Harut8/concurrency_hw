import os

def multiple_forks_execs():
    for command in [("ls", "ls"), ("date", "date")]:
        pid = os.fork()
        if pid == 0:
            # Child process
            os.execl("/bin/" + command[0], command[1])
        else:
            # Parent process
            print(f"Child process {command[1]} created")
            os.wait()  # Wait for the specific child to terminate

    print("Parent process done")

if __name__ == "__main__":
    multiple_forks_execs()
