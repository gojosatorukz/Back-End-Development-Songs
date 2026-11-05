from . import app
import json
import os
from pathlib import Path
from urllib.parse import quote_plus
from flask import jsonify, request
from pymongo import MongoClient
from bson import json_util
uri = os.getenv('MONGO_URI')
if not uri:
    host=os.environ.get('MONGODB_SERVICE','localhost')
    user=os.environ.get('MONGODB_USERNAME')
    password=os.environ.get('MONGODB_PASSWORD')
    auth=f'{quote_plus(user)}:{quote_plus(password)}@' if user and password else ''
    uri=f'mongodb://{auth}{host}/?authSource=admin'
client=MongoClient(uri,serverSelectionTimeoutMS=10000)
db=client.songs
collection=db.songs
collection.create_index('id',unique=True)
if collection.count_documents({})==0:
    with open(Path(__file__).parent/'data'/'songs.json',encoding='utf-8') as source:
        songs_list=json.load(source)
    if songs_list:
        collection.insert_many(songs_list)
def parse_json(value):
    return json.loads(json_util.dumps(value))
@app.route('/health')
def health():
    client.admin.command('ping')
    return jsonify(status='OK'),200
@app.route('/count')
def count():
    return jsonify(count=collection.count_documents({})),200
@app.route('/song',methods=['GET'])
def get_songs():
    return jsonify(songs=parse_json(list(collection.find({})))),200
@app.route('/song/<int:id>',methods=['GET'])
def get_song_by_id(id):
    song=collection.find_one({'id':id})
    if song is None:
        return jsonify(message='song with id not found'),404
    return jsonify(parse_json(song)),200
@app.route('/song',methods=['POST'])
def create_song():
    song=request.get_json(silent=True)
    if not isinstance(song,dict) or not isinstance(song.get('id'),int):
        return jsonify(message='Invalid input parameter'),400
    if collection.find_one({'id':song['id']}):
        return jsonify(Message=f"song with id {song['id']} already present"),302
    result=collection.insert_one(song)
    return jsonify(parse_json({'inserted id':result.inserted_id})),201
@app.route('/song/<int:id>',methods=['PUT'])
def update_song(id):
    song=request.get_json(silent=True)
    if not isinstance(song,dict) or not song:
        return jsonify(message='Invalid input parameter'),400
    if collection.find_one({'id':id}) is None:
        return jsonify(message='song not found'),404
    song.pop('_id',None)
    song['id']=id
    result=collection.update_one({'id':id},{'$set':song})
    if result.modified_count==0:
        return jsonify(message='song found, but nothing updated'),200
    return jsonify(parse_json(collection.find_one({'id':id}))),201
@app.route('/song/<int:id>',methods=['DELETE'])
def delete_song(id):
    result=collection.delete_one({'id':id})
    if result.deleted_count:
        return '',204
    return jsonify(message='song not found'),404
