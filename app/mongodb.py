from pymongo import MongoClient
client = MongoClient()

db = client["Facebook"]
msg_collection = db["posts"]

posts = Scraper()

