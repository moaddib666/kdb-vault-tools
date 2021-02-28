# Contributing to `kdb_vault_tools`

## Development

- Setup your python env
- Setup `docker` and `docker-compose`
- Install packages `pip install -r requirements.txt -r requirements-dev.txt` 
- Run `vault` in development mode with help of compose `docker-compose up`
- Run `tox` to check if your code ready to be published
- `tox -e py39test-kdb-vault-tools` to e.g. to run the specific test for chosen python version
- `tox -e lint` to run lint checks

## Pull Requests
Please follow guidelines of [GIT FLOW](https://www.conventionalcommits.org/en/v1.0.0/) and [CONVENTIONAL COMMITS](https://www.conventionalcommits.org/en/v1.0.0/)

### Sending of Pull Requests

Everyone is welcome to contribute code to `kdb_vault_tools` via GitHub pull requests (PRs).