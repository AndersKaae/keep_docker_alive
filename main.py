import subprocess
from time import sleep
from datetime import datetime

def check_docker_container(container_name):
    try:
        result = subprocess.run(['docker', 'ps'], capture_output=True, text=True, check=True)
        return container_name in result.stdout
    except subprocess.CalledProcessError as e:
        print(f'Error checking Docker containers: {e}')
        return False

def kill_docker_desktop():
    try:
        subprocess.run('killall "Docker Desktop"', shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f'Error restarting Docker Desktop: {e}')

def start_docker_desktop():
    try:
        subprocess.run('open -a "Docker Desktop"', shell=True, check=True)
        print(f'{datetime.now()}: Docker Desktop has been restarted.')
    except subprocess.CalledProcessError as e:
        print(f'Error restarting Docker Desktop: {e}')


def main():
    container_name = 'enhjorning_nuxt'
    check_interval = 60  # seconds

    while True:
        if not check_docker_container(container_name):
            print(f'Cannot find container: {container_name}')
            kill_docker_desktop()
            sleep(5)
            start_docker_desktop()
        sleep(check_interval)

if __name__ == '__main__':
    main()
