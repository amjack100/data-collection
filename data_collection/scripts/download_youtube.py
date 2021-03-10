import fire
from data_collection import run_command


def main(url, destination):

    command = f"youtube-dl {url} -o {destination}"
    # print(command)
    run_command(command=command)


if __name__ == "__main__":
    fire.Fire(main)