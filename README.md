# Songs REST API

MongoDB-backed Flask microservice for the IBM Back-end Application Development Capstone. Implements health, count, list, retrieve, create, update and delete.

Supply MONGO_URI through the environment (never commit credentials), install requirements.txt with Python 3.9, and run `flask run --host 0.0.0.0 --port 5000`. The initial 20 songs are inserted only when the collection is empty. A unique id index prevents duplicates.

Verified 13 real HTTP checks: health, count, list, retrieval, missing retrieval, invalid creation, creation, duplicate creation, update, unchanged update, missing update, deletion and missing deletion. The starter tests incorrectly refer to Pictures, so service-specific HTTP verification is included separately.
