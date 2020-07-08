# python-api-projects
Repository for Python API Projects

## How to start application locally
Use docker-compose commands to build, run, and exec into
```bash
docker-compose build
docker-compose up -d
docker-compose exec rescue-groups-app bash
docker-compose down
```

Once inside the container run, and the website will be at the address `localhost:9080`:
```bash
python3 -m rescue_groups
```

## How to deploy project
Push code to `master` branch of github
```bash
git push heroku master
```
