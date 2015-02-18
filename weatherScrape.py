# Scrape high and low temperature data of each current day and future forecasts. 
#
# 2014.14.02
# AMS

import datetime 
import re 
#print head wholething 
 
now=str(datetime.datetime.now())[:-8].replace(' ','_').replace(':','-') 
outfile = open('weather_file_'+now+'.txt','w') 

wholething = open('2014-02-14_20-27-0.html') 

outfile.write(now + '\n\n') 

hitemp_re = re.compile( '"wx-temp"> (.*)<sup>')		#capture hitemps 
lotemp_re = re.compile( '"wx-temp-alt"> (.*)<sup>') #capture lotemps 
date_re = re.compile('"wx-table">([A-Z][a-z]{2}) [0-9]{1,2}</span>')	 
#capture month date 

hitemps = re.findall(hitemp_re, wholething) 
lotemps = re.findall(lotemp_re, wholething) 
dates =  re.findall(date_re, wholething) 

for date, hi, lo in zip(dates, hitemps, lotemps): 
	outfile.write(date, hi, lo + '\n') 
	 
outfile.close()
