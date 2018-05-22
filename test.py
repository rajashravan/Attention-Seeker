#my python script for instagram API

from InstagramAPI import InstagramAPI

api = InstagramAPI("raja.shravan", "PASS HERE")
api.login() # login


api.tagFeed("cat") # get media list by tag #cat
media_id = api.LastJson # last response JSON
api.like(media_id["ranked_items"][0]["pk"]) # like first media
api.getUserFollowers(media_id["ranked_items"][0]["user"]["pk"]) # get first media owner followers
