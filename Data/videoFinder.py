import mysql.connector
import json
from googleapiclient.discovery import build


API_KEY = ''
API_VERSION = 'v3'

UNDISPUTED_YT_ID   = 'UCLXzq85ijg2LwJWFrz4pkmw'
ESPN_YT_ID 		   = 'UCiWLfSweyRNmLpgEHekhoAg'
FIRST_THINGS_YT_ID = 'UCOTPo2y-NHJjg1EuENrxypA'
BREAKDOWN_YT_ID    = 'UCSpvjDk06HLxBaw8sZw7SkA'
HIGHLIGHTS_YT_ID   = 'UCS7kvhJx431xCKuSgkBaUWw'
NBA_YT_ID 		   = "UCWJ2lWNubArHWmf3FIHbfcQ"



def findLastGameHighlights():
	cnx = mysql.connector.connect(user='root', password='password',
                              host='127.0.0.1',
                              database='myTeam')
	cursor = cnx.cursor()
	search = ("SELECT Team,OpposingTeam FROM LastGames")
	cursor.execute(search)
	GAMES = []
	for row in cursor:
		GAMES.append((row[0],row[1]))
	for game in GAMES:
		teams_in_game = []
		search_1 = ("SELECT TeamName FROM Teams WHERE TeamAbbreviation = '{}'".format(game[0]))
		cursor.execute(search_1)
		for row in cursor:
			teams_in_game.append(row[0].split()[len(row[0].split()) - 1])
		search_2 = ("SELECT TeamName FROM Teams WHERE TeamAbbreviation = '{}'".format(game[1]))
		cursor.execute(search_2)
		for row in cursor:
			teams_in_game.append(row[0].split()[len(row[0].split()) - 1])
		youtube = build('youtube',API_VERSION,developerKey=API_KEY)
		req = youtube.search().list(part='snippet',maxResults=1,q='{} vs. {} Full Game Recap'.format(teams_in_game[0],teams_in_game[1]),type='video',channelId=NBA_YT_ID)
		res = req.execute()
		for element in res['items']:
			video_id = element['id']['videoId']
		insert = ("INSERT INTO Videos (Team,VideoUrlId) VALUES (%s,%s)")
		insert_data = (game[0],video_id)
		cursor.execute(insert,insert_data)
	cnx.commit()
	cursor.close()
	cnx.close()
	print("Last Game Highlights Inserted")

def createStars():
	cnx = mysql.connector.connect(user='root', password='password',
                              host='127.0.0.1',
                              database='myTeam')
	cursor = cnx.cursor(buffered=True)
	pg_search = ("SELECT Players.PlayerID,Players.FirstName,Players.LastName,Players.Team \
														FROM Players JOIN PlayerSTATs ON (Players.PlayerID = PlayerSTATs.PlayerID) WHERE Players.Position = 'PG' \
														AND PlayerSTATs.PPG > 10 AND PlayerSTATs.APG > 5")
	sg_search = ("SELECT Players.PlayerID,Players.FirstName,Players.LastName,Players.Team \
														FROM Players JOIN PlayerSTATs ON (Players.PlayerID = PlayerSTATs.PlayerID) WHERE Players.Position = 'SG' \
														AND PlayerSTATs.PPG > 18;")
	sf_search = ("SELECT Players.PlayerID,Players.FirstName,Players.LastName,Players.Team \
														FROM Players JOIN PlayerSTATs ON (Players.PlayerID = PlayerSTATs.PlayerID) WHERE Players.Position = 'SF' \
														AND PlayerSTATs.PPG > 15 AND PlayerSTATs.RPG > 5")
	pf_search = ("SELECT Players.PlayerID,Players.FirstName,Players.LastName,Players.Team \
														FROM Players JOIN PlayerSTATs ON (Players.PlayerID = PlayerSTATs.PlayerID) WHERE Players.Position = 'PF' \
														AND PlayerSTATs.PPG > 15 AND PlayerSTATs.RPG > 5;")
	c_search  = ("SELECT Players.PlayerID,Players.FirstName,Players.LastName,Players.Team \
														FROM Players JOIN PlayerSTATs ON (Players.PlayerID = PlayerSTATs.PlayerID) WHERE Players.Position = 'C' \
														AND PlayerSTATs.PPG > 10 AND PlayerSTATs.RPG > 7 AND PlayerSTATS.BPG > 1")
	star_queries = [pg_search,sg_search,sf_search,pf_search,c_search]
	inserts_to_be_made = []
	for query in star_queries:
		cursor.execute(query)
		for row in cursor:
			
			id_ = row[0]
			first_name = row[1]
			last_name = row[2]
			team = row[3]

			insert = ("INSERT INTO Stars (PlayerID,FirstName,LastName,Team) VALUES (%s,%s,%s,%s)")
			data = (id_,first_name,last_name,team)
			inserts_to_be_made.append((insert,data))
	for statement in inserts_to_be_made:
		cursor.execute(statement[0],statement[1])
	cnx.commit()
	cursor.close()
	cnx.close()

def returnStars():
	cnx = mysql.connector.connect(user='root', password='password',
                              host='127.0.0.1',
                              database='myTeam')
	cursor = cnx.cursor()
	query = ("SELECT * FROM Stars")
	cursor.execute(query)
	players = dict()
	for row in cursor:
		players[" ".join( [row[2],row[3]] )] = (row[1],row[4])
	cursor.close()
	cnx.close()
	return players

def returnTeamNames():
	cnx = mysql.connector.connect(user='root', password='password',
                              host='127.0.0.1',
                              database='myTeam')
	cursor = cnx.cursor()
	query = ("SELECT * FROM Teams")
	cursor.execute(query)
	teams = dict()
	for row in cursor:
		teams[ ( (row[1].split())[len((row[1].split())) - 1] )  ] = row[0]
	cursor.close()
	cnx.close()
	return teams


def checkUndisputed(playersToLookFor,teamsToLookFor):
	names = list(playersToLookFor.keys())
	teams = list(teamsToLookFor.keys())
	
	youtube = build('youtube',API_VERSION,developerKey=API_KEY)
	req_1 = youtube.search().list(part='snippet',maxResults=10,q='',type='video',channelId=UNDISPUTED_YT_ID,order='date')
	res_1 = req_1.execute()
	videos = []
	for element in res_1['items']:
		if 'NBA' in element['snippet']['title']:
			videos.append(element['id']['videoId'])
	req_2 = youtube.videos().list(part='snippet',id=",".join(videos))
	res_2 = req_2.execute()
	# Only checking for player names
	videos_to_add = []
	for item in res_2['items']:
		for name in names:
			if name in item['snippet']['description'] or name in item['snippet']['title']:
				team = playersToLookFor[name]
				video = item['id']
				videos_to_add.append(  [video,team[1]]  )
	
	cnx = mysql.connector.connect(user='root', password='password',
                              host='127.0.0.1',
                              database='myTeam')
	cursor = cnx.cursor()
	insert = ("INSERT INTO Videos (Team,VideoUrlId) VALUES (%s,%s)")
	for element in videos_to_add:
		insert_data = (element[1],element[0])
		cursor.execute(insert,insert_data)
	cnx.commit()
	cursor.close()
	cnx.close()



def findAnalystVideos():
	createStars()
	playersToLookFor = returnStars()
	teamsToLookFor = returnTeamNames()
	checkUndisputed(playersToLookFor,teamsToLookFor)


# Alter videos table to classify videos as highlights or analysis

def main():
	#findLastGameHighlights()
	#findAnalystVideos()

if __name__== "__main__":
	main()
