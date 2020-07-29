# rescue-groups
Repository for Python Website for the rescue-groups API

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
GOOGLE_CLIENT_ID=<ID> GOOGLE_CLIENT_SECRET=<SECRET> uwsgi uwsgi.ini
```

## Setup local secrets
Create a `secrets.json` file at the top level of the repository, so we can call the rescue groups API
```json
{
    "rescue_group": {
        "url": "https://api.rescuegroups.org/http/v2.json",
        "api_key": <RESCUE_GROUPS_SECRET>,
        "data": {
            "search": {
                "resultStart": 0,
                "resultLimit": 20,
                "fields": [
                    "animalName",
                    "animalThumbnailUrl",
                    "animalSex",
                    "animalGeneralAge",
                    "animalLocation",
                    "locationAddress"
                ],
                "filters": [
                    {
                        "fieldName": "animalSpecies",
                        "operation": "equals",
                        "criteria": "cat"
                    },
                    {
                        "fieldName": "animalLocation",
                        "operation": "equals",
                        "criteria": "48105"
                    }
                ]
            }
        }
    }
}
```

## How to deploy project
Push code to `master` branch of github
```bash
git push heroku master
```
