#!/usr/bin/env python3
# encoding: utf-8

import json
import requests
import time

ligas = {"LaLiga": 455, "Premier": 445}
print('Ligas disponibles : Premier, LaLiga')
league = input ("Selecciona una liga : ")


def getJSONRDawData():
	headers = { 'X-Auth-Token': 'xxxxxxx', 'X-Response-Control': 'minified' }
	r = requests.get(url,headers=headers)
	return r.json()	

def parseJSON(rawdata):
	jornada_actual = getJourney(getJSONRDawData())
	for i in range (0,380):
		jornada = rawdata['fixtures'][i]['matchday']
		status = rawdata['fixtures'][i]['status']
		if ((jornada == jornada_actual)and(status == "FINISHED")):
			resultgh = rawdata['fixtures'][i]['result']['goalsHomeTeam']
			resultga = rawdata['fixtures'][i]['result']['goalsAwayTeam']
			home = rawdata ['fixtures'][i]['homeTeamName']
			away = rawdata ['fixtures'][i]['awayTeamName']
			match = "%s vs %s -- %s - %s"%(home,away,resultgh,resultga)
			print(match)
		elif ((jornada == jornada_actual)and(status == "TIMED")):
			home = rawdata ['fixtures'][i]['homeTeamName']
			away = rawdata ['fixtures'][i]['awayTeamName']
			match = "%s vs %s -- Pending"%(home,away)
			print(match)
		elif ((jornada == jornada_actual)and(status == "IN_PLAY")):
			home = rawdata ['fixtures'][i]['homeTeamName']
			away = rawdata ['fixtures'][i]['awayTeamName']
			match = "%s vs %s -- Playing now"%(home,away)		
			print(match)
			#return match

def getMatchesEPL():
	return parseJSON(getJSONRDawData())

def getTime():
	return time.strftime('%Y-%m-%d')

def getJourney(rawdata):
	for i in range (0,380):
		date = rawdata['fixtures'][i]['date']	
		if(date > getTime()):
			perd = rawdata['fixtures'][i]['matchday']
			return perd		

for i in ligas:
	if(league == i):
		url= 'http://api.football-data.org/v1/competitions/{}/fixtures'.format(ligas[i])
		#print(url)
		getMatchesEPL()


#getTime()
#getJourney(getJSONRDawData())