import urllib
# url="http://s1.bia2m.in/Series/24/s1/24%20S01%20E11%20(Bia2Movies).mkv"
season_name= "The Last Ship"
# season_number="1"
for season_number in xrange(1,4):
	season_number=str(season_number)
	season_episode_number_outside=12
	zero="0"
	la = []
	fourofour = []
	# url="http://s1.bia2m.in/Series/"+ str(season_name)+"/s"+str(season_number)+"/"+str(season_name)+"%20S"+str(zero+season_number)+"%20E"+str(zero+season_episode_number)+"%20(Bia2Movies).mkv"

	def main1(fourofour):
		print fourofour

	def main(season_name,season_number,season_episode_number):
		season_episode_number_outside=season_episode_number+1
		for season_episode_number in range(1,season_episode_number_outside):
			temp_if = season_episode_number
			season_episode_number=str(season_episode_number)
			if temp_if<=9:
				url="http://s1.bia2m.in/Series/"+ str(season_name)+"/s"+str(season_number)+"/"+str(season_name)+"%20S"+str(zero+season_number)+"%20E"+str(zero+season_episode_number)+"%20(Bia2Movies).mkv"
			else:
				url="http://s1.bia2m.in/Series/"+ str(season_name)+"/s"+str(season_number)+"/"+str(season_name)+"%20S"+str(zero+season_number)+"%20E"+str(season_episode_number)+"%20(Bia2Movies).mkv"
			la.append(url)
		percent = round(100.0/len(la), 2)
		check(la,season_episode_number_outside,percent)

	def check(la,season_episode_number_outside,percent):
		temp=0
		for season_episode_number in range(1,season_episode_number_outside):
			x = urllib.urlopen(la[season_episode_number-1]).getcode()
			temp=temp+percent
			if temp>=99:
				temp=100
			print str(temp)+"% completed"
			print la[season_episode_number-1]
			if int(x)==200:
				print "Sucessfull"
			else:
				fourofour.append(la[season_episode_number-1])
				
		main1(fourofour)

	main(season_name,season_number,season_episode_number_outside)
