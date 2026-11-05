# Songs REST API

MongoDB-backed Flask microservice for the IBM Back-end Application Development Capstone. Implements health, count, list, retrieve, create, update and delete.

Supply MONGO_URI through the environment (never commit credentials), install requirements.txt with Python 3.9, and run `flask run --host 0.0.0.0 --port 5000`. The initial 20 songs are inserted only when the collection is empty. A unique id index prevents duplicates.

Verified 13 real HTTP checks: health, count, list, retrieval, missing retrieval, invalid creation, creation, duplicate creation, update, unchanged update, missing update, deletion and missing deletion. The starter tests incorrectly refer to Pictures, so service-specific HTTP verification is included separately.

## Environment Setup

This repository was created from the IBM Skills Network template `hvlga-Back-End-Development-Songs`. The supported course runtime is Python 3.9.x; use the dedicated virtual environment `backend-songs-venv`.

Run the provided setup script from the repository root:

```bash
bash bin/setup.sh
```

The script reports `Capstone Environment Setup Complete` when it reaches its final setup step. Verify Python 3.9.x and create the named service environment:

```bash
python3.9 --version
python3.9 -m venv ~/backend-songs-venv
source ~/backend-songs-venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -v
```

The Songs API was verified with 13 HTTP checks.

Setup verification: `bin/setup.sh` completed with `Capstone Environment Setup Complete`. Python 3.9.25 was verified in both dedicated named environments.
