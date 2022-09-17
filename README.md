# Kitchen-sink

## Installation

Make sure Yarn is installed - if on Mac:

```bash
brew install yarn
```

if on Windows:
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

Installation of [NVM](https://tecadmin.net/install-nvm-macos-with-homebrew/) on Mac
or Windows: [NVM](https://dev.to/skaytech/how-to-install-node-version-manager-nvm-for-windows-10-4nbi)

```node
nvm use --lts
```

Project level packages installed with pipenv:

i.e.
```python
pipenv install mongoengine
```

.flaskenv
```node
FLASK_ENV=development
FLASK_APP=./server/src/main.py
FLASK_RUN_PORT=5001
```
