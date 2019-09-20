# python-api-projects
Repository for Python API Projects

## How to start application locally
Run the script `docker_cli.py` with args:
```bash
python3 docker_cli.py build
python3 docker_cli.py start
python3 docker_cli.py login
```

Once inside the container run, and the website will be at the address `localhost:9080`:
```bash
python3 -m api_projects
```

## How to deploy project
Push code to `master` branch of github
```bash
git push heroku master
```
