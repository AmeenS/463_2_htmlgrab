# Open weather.com pages. Mark and save them. To be run as cron job
#
# 2014.14.02
# AMS


from urllib2 import urlopen 
import datetime 
import re 

path = '/home/ameesal/463_Spring/weather/' 

urls = ['http://www.weather.com/weather/tenday/Buffalo+NY+14215:4:US', 
	'http://www.weather.com/weather/yesterday/Buffalo+NY+14215:4:US',] 

for url in urls: 
	filename = url.replace('http://','').replace('/','_').replace('+','_').replace(':','_').replace('?','_').replace('&','_').replace('=','_') 
	filename += '.html' 
	page = urlopen(url).read() 
	time = datetime.datetime.now()	 
	now=str(time)[:-8].replace(' ','_').replace(':','-') 
	now+= filename 
	outfile = open(now+'.html','w') 
	print >>outfile, page 
	outfile.close() 
	print 'Finished.' 
