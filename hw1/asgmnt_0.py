import os

def print_pid_and_ppid(pid: int, p_pid: int):
    print(f"PID: {pid}, Parent PID: {p_pid}")

def print_forked_from(pid: int, parent_pid: int):
    print(f"--- Process {pid} forked from Parent {parent_pid} ---")

def multiple_forks():
    print("---START---")
    print_pid_and_ppid(os.getpid(), os.getppid())

    pid1 = os.fork()
    if pid1 == 0:
        print_forked_from(os.getpid(), os.getppid())
    else:
        os.wait()  # Wait for the child termination to avoid process clutter
    pid2 = os.fork()
    if pid2 == 0:
        print_forked_from(os.getpid(), os.getppid())
    else:
        os.wait()
    print_pid_and_ppid(os.getpid(), os.getppid())

if __name__ == "__main__":
    multiple_forks()
