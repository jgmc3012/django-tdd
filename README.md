# Movies App

## Deploy on  Heroku
```
heroku container:login

# Create Data Base
heroku addons:create heroku-postgresql:hobby-dev

# Build image
docker build -f Dockerfile.prod -t registry.heroku.com/$(fzf heroku apps)/web .
docker push registry.heroku.com/$(fzf heroku apps)/web:latest

# Deploy
heroku container:release web

# Run command as "python manage.py migrate"
heroku run python manage.py migrate
```

## Tests
- **normal run:** 
`docker-compose exec movies pytest`

- **disable warnings:**
`docker-compose exec movies pytest -p no:warnings`

- **run only the last failed tests:** 
`docker-compose exec movies pytest --lf`

- **run only the tests with names that match the string expression:** 
`docker-compose exec movies pytest -k "movie and not all_movies"`

- **stop the test session after the first failure:**
`docker-compose exec movies pytest -x`

- **enter PDB after first failure then end the test session:** 
`docker-compose exec movies pytest -x --pdb`

- **stop the test run after two failures:** 
`docker-compose exec movies pytest --maxfail=2`

- **show local variables in tracebacks:** 
`docker-compose exec movies pytest -l`

- **list the 2 slowest tests:** 
`docker-compose exec movies pytest  --durations=2`

- **Run test with coverage**
`docker-compose exec movies pytest -p no:warnings --cov=. --cov-report html`

## Code Quality Style
### Run code review
`docker-compose exec movies flake8 .`

### Format code 
- Check
`docker-compose exec movies black --check --exclude=migrations .`

- Format
`docker-compose exec movies black --exclude=migrations .`

[More option](https://black.readthedocs.io/en/stable/installation_and_usage.html#command-line-options)

### Check imports
```
# Check-only
docker-compose exec movies /bin/sh -c "isort ./*/*.py --check-only"

# Diff
docker-compose exec movies /bin/sh -c "isort ./*/*.py --diff"

# Apply Changes
docker-compose exec movies /bin/sh -c "isort ./*/*.py"
```
