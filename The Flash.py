import urllib
from openpyxl import Workbook
book = Workbook()
sheet = book.active
series = "The Flash"
no_of_season = 2
no_of_season=no_of_season+1
# episode_list = ['01','10','24']
for season in range(1,no_of_season):
	seasons="/s"+str(season)
	url = "http://s1.bia2m.in/Series/"+series+seasons
	n=25
	for item in range(1,n):
		if item <=9:
			item == '0'+str(item)
			actuallink = url+"/"+str(series)+"%20S0"+str(season)+"%20E0"+str(item)+"%20(Bia2Movies).mkv"	
		else:
			actuallink = url+"/"+str(series)+"%20S0"+str(season)+"%20E"+str(item)+"%20(Bia2Movies).mkv"
		
		print actuallink
		x = urllib.urlopen(actuallink).getcode()
		print x

		if(x == 200):
			col = "A"+str(item)
		else:
			col = "B"+str(item)

		sheet[col] = actuallink
		book_name = series+"_"+str(season)+".xlsx"
		book.save(book_name)
