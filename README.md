# Kitchen-sink

## Installation

Make sure Yarn is installed:

```node
npm install --global yarn
```

Make sure pipenv is installed - if on Mac:

```bash
brew install pipenv
```
if on Windows:
[Installation](https://www.pythontutorial.net/python-basics/install-pipenv-windows/)

Ensure Node conformity, running 16.x for development:

```node
nvm use --lts
```

.flaskenv
```node
FLASK_ENV=development
FLASK_APP=./server/src/main.py
FLASK_RUN_PORT=5001
```
