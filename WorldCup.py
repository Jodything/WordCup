#World Cup Team Info Finder
#data pulled from the site http://softwareforgood.com/soccer-good/

import urllib #for urlencoder usage
import urllib2 #making HTTP requests
import json #makes the data easier to work with

#team result data
teams = urllib2.urlopen('http://worldcup.sfg.io/teams').read()

#to show our user the input needed to find the info they want. AKA the proper team names
for team in json.loads(teams.decode('utf-8')):
	print (team['fifa_code'], team['country'])

#finding out what team we will pull info from
team_name = raw_input("What team do you want to know about? \nFind your team's 3 digit abbreivation above and type it in to find out: ")

#turns non word characters into url-safe characters and upper cases user's input for correct url
team_name = urllib.quote_plus(team_name).upper()

#adding the user's team name inputted to the url
url = 'http://worldcup.sfg.io/matches/country?fifa_code='+team_name

response = urllib2.urlopen(url) #calling the site

for site in response:
	print site

#exporting to all info received into a text file
Results = open("TeamStats.txt", "w")
Results.write(site)
Results.close()

print ('\nYour results have been output to a text file for later use as well')

raw_input('Press enter to exit')
