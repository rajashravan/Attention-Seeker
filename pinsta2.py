from InstagramAPI import InstagramAPI
import math
import datetime

#use getTime(user, password) returns

#getPic(user, password) returns a link to the user's profile pic

def getTime(user, password):
	api = InstagramAPI(user, password)
	api.login()
	#print(api.username_id)
	api.getTimeline()
	g = api.LastJson
	##print(g)
	##
	##likesval = 0
	##count = 0
	##
	#for x in g['items']:
	##    likesval += x['like_count']
	##    count += 1
	##        print(y)
	##
	##print(likesval)
	##print(count)

	totallikes = 0
	avg = 0;

	for x in g["items"]:
		avg += x['like_count'] * x['taken_at']
		totallikes += x['like_count']
		#print(x)
	#	for y in x.keys():
	#		print(y)

	avg = avg / totallikes #get avg timestamp
	#avg = avg * 1000
	avg = math.floor(avg)

	#the following 3 lines rounds the time down to the nearest hour (ex 1:05 goes to 1:00)
	avg = avg / 3600
	avg = math.floor(avg)
	avg = avg * 3600

	returnstring = "Your followers are most active between "
	returnstring += datetime.datetime.fromtimestamp(
	        int(avg)
	    ).strftime('%H:%M:%S')
	returnstring += " and "
	returnstring += datetime.datetime.fromtimestamp(
	        int(avg + 3600)
	    ).strftime('%H:%M:%S')
	returnstring += " (24 hour notation)."

	return returnstring



def getPic(user, password):
	api = InstagramAPI(user, password)
	api.login()
	api.getProfileData()
	me = api.LastJson

	returnstring = " "
	returnstring = me['user']['profile_pic_url']
	return returnstring
	#print(returnstring) #prints the url to the person's 


	"""
	self_followers = [] #array of userIDs of my followers
	for x in g['users']:
		#print(x)
		if isinstance(x, dict):
			self_followers.append(x['pk'])

	print(len(self_followers))

	api.getUsernameInfo(self_followers[0])
	api.getTimeline();
	last = api.LastJson
	#mulitply timestamps by number of likes
	#keep track of total likes
	#divide 1 by 2 --> get time stamp
	#convert to regular time, return the hour
	print("XXXXXXXXXXXXXXXXX")
	print(self_followers[0])
	#print(last)

	#for user in self_followers:
	"""