from subprocess import call
import argparse
import logging
import docker
import sys

CLIENT = docker.from_env()

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


class DockerCLI(object):

    def __init__(self):
        parser = argparse.ArgumentParser(
            description="Docker CLI",
            usage="""python docker.py <command> [<args>]
                    Sub-commands:
                        init    Build everything using docker-compose
                        stop    Stops the running container
                        build   Builds the stopped container
                        start   Starts the stopped container
                        login   Login to bash in the container
                    """)
        parser.add_argument("command", help="Subcommand to run")
        if len(sys.argv) != 1:
            logger.error("")
        args = parser.parse_args(sys.argv[1:])

        if not hasattr(self, args.command):
            logger.error("Unrecognized command")
            parser.print_help()
            exit(1)

        getattr(self, args.command)()

    def start(self):
        call(["docker-compose -f .docker/docker-compose.yml up -d"],
             shell=True)

    def build(self):
        call(["docker-compose -f .docker/docker-compose.yml build --no-cache"],
             shell=True)

    def stop(self):
        call(["docker-compose -f .docker/docker-compose.yml down"],
             shell=True)

    def login(self):
        prepend = "api_app_1"
        print(prepend)
        print([c.name for c in CLIENT.containers.list()])
        hashed = [c.name for c in CLIENT.containers.list() if prepend in c.name][0]

        call(["docker exec -it {} bash".format(hashed)], shell=True)


if __name__ == "__main__":
    DockerCLI()
