""" import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv()) """
import json
from pymongo import MongoClient

def database_func():
    
    connection_string = 'mongodb+srv://cemsari:test123@cluster0.oyrul3n.mongodb.net/?retryWrites=true&w=majority'
    client = MongoClient(connection_string)
    Mylogs = client.Mylogs
    collection = Mylogs.logs

    with open('data.json') as json_file:
        data = json.load(json_file)
        json_file.close()
    collection.insert_many(data)