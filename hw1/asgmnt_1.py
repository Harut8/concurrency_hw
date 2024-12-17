import os

# HERE I HAVE QUESTION
# WHEN USE ???
# P variants: execlp, execvp
# L variants: execl, execlp
# E variants: execle, execlpe

def simple_fork_exec():
    pid = os.fork()
    if pid == 0:
        # Child process
        print("Child process started")
        os.execl("/bin/ls", "ls", "-l")
        # anything after os.execlp() will not be executed
    elif pid < 0:
        print("Fork failed")
        return
    else:
        # Parent process
        print("Parent process done")
        os.wait()  # Wait for child to terminate

if __name__ == "__main__":
    simple_fork_exec()
