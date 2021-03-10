import subprocess


def run_command(command: str):

    command = command.split()

    process = subprocess.Popen(command)

    while True:
        if process.poll() is not None:
            print("Done")
            break