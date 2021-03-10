import subprocess
import fire
import sys
import os
import fire


def main(url, destination):

    command = f"youtube-dl {url} -o {destination}".split()

    process = subprocess.Popen(command)

    while True:
        if process.poll() is not None:
            print("Done")
            break


fire.Fire(main)