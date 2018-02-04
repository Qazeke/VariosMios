#!/usr/bin/env python
# encoding: utf-8

import httplib
import json
import requests

#connection = httplib.HTTPConnection('api.football-data.org')
#headers = { 'X-Auth-Token': '6e5f9808ecd24c57b0491e81cdf7e02b', 'X-Response-Control': 'full' }
#connection.request('GET', '/v1/competitions/445/fixtures', None, headers )
#response = json.loads(connection.getresponse().read().decode())


def getJSONRDawData():
	r = requests.get('http://api.football-data.org/v1/competitions/445/fixtures')
	return r.json()

def parseJSON(rawdata):
	
	for i in range (0,380):
		jornada = rawdata['fixtures'][i]['matchday']
		status = rawdata['fixtures'][i]['status']
		if ((jornada == 26)and(status == "FINISHED")):
			resultgh = rawdata['fixtures'][i]['result']['goalsHomeTeam']
			resultga = rawdata['fixtures'][i]['result']['goalsAwayTeam']
			home = rawdata ['fixtures'][i]['homeTeamName']
			away = rawdata ['fixtures'][i]['awayTeamName']
			match = "%s vs %s -- %s - %s"%(home,away,resultgh,resultga)
			print(match)
		elif ((jornada == 26)and(status == "TIMED")):
			home = rawdata ['fixtures'][i]['homeTeamName']
			away = rawdata ['fixtures'][i]['awayTeamName']
			match = "%s vs %s -- Pending"%(home,away)
			print(match)
		elif ((jornada == 26)and(status == "IN_PLAY")):
			home = rawdata ['fixtures'][i]['homeTeamName']
			away = rawdata ['fixtures'][i]['awayTeamName']
			match = "%s vs %s -- Playing now"%(home,away)		
			print(match)
			#return match

def getMatchesEPL():
	return parseJSON(getJSONRDawData())

#print(getMatchesEPL())