from typing import Union

from fastapi import FastAPI
from scraping import Scraper

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")

app = FastAPI()
posts = Scraper()

db = client["Facebook"]
msg_collection = db["postsFa"]


@app.get("/{tags}")
async def read_items(tags):
  ScrapingPost = posts.scrapedata(tags)
  result = msg_collection.insert_many(ScrapingPost)
  print('*******', result.inserted_id)
  x = msg_collection.find_one()
  print(x)

  return ScrapingPost

#@app.get(
#    "/posts"#, response_description="List all posts", response_model=List[PostsModel]
#)
#async def list_posts():
#    students = await msg_collection.find().to_list(50)
#    return students
#
#@app.get("/post")
#async def fetch_all_todos():
#    todos = []
#    cursor = await msg_collection.find({})
#    async for document in cursor:
#        todos.append(ToDo(**document))
#    return todos
#
#
##@app.get("/items/{item_id}")
##def read_item(item_id: int, q: Union[str, None] = None):
##    return {"item_id": item_id, "q": q}
#