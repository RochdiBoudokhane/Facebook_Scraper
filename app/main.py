from typing import Union

from fastapi import FastAPI
from scraping import Scraper

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")

app = FastAPI()
posts = Scraper()

db = client["Facebook"]
msg_collection = db["posts"]


@app.get("/{tags}")
async def read_items(tags):
  ScrapingPost = posts.scrapedata(tags)
  result = msg_collection.insert_many(ScrapingPost)
  print('*******', result.inserted_id)
  x = msg_collection.find_one()
  print(x)

  return ScrapingPost

@app.get(
  "/scraping/posts", response_description="List all posts", response_model=List[posts]
)
async def list_posts():
    posts = await msg_collection.find().to_list(50)
    return posts

