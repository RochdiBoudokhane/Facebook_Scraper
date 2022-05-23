from facebook_scraper import get_posts
import pandas as pd 

class Scraper():


  def scrapedata(self, tags):
    post_list = []
    post_number = 0
    for post_info in get_posts(tags, cookies='Cookies.txt', pages=5, options={"comments": 10, "reactors": False, "progress":False, "posts_per_page": 10}):
      post_number += 1
      print("POST Nº", int(post_number), " - URL: ", post_info["post_url"])
      print("ID: ", int(post_info["post_id"]))
      print("POST TEXT: ", post_info["post_text"])
      print("TIME: ", post_info["time"], " - ", "TIMESTAMP: ", post_info["timestamp"])
      print("LIKES: ", post_info["likes"])
      print("COMMENTS: ", post_info["comments"])
      print("SHARES: ", post_info["shares"])
      post_list.append(post_info)  # Add post to list
      print(post_info)
    print(len(post_list))

    return post_list
posts = Scraper()
posts.scrapedata('Tunisia')