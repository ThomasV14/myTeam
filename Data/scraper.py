import requests
import mysql.connector
from bs4 import BeautifulSoup
from selenium import webdriver

TEAMS = ["ATL", "BOS", "CHI", "CHO","CLE","DAL","DEN","DET","GSW",
		"HOU","IND","LAC","LAL","MEM","MIA","MIL","MIN","NOP","OKC",
		"BRK","NYK","ORL","PHI","PHO","POR","SAC","SAS","TOR","UTA","WAS"]

def insertTeams(URLS):
	teamNames = dict()
	for team,url in URLS.items():
		r = requests.get(url)
		soup = BeautifulSoup(r.text, 'html.parser')
		element = soup.find_all('h1',attrs={'itemprop':'name'})[0].find_all('span')[1]
		teamNames[team] = element.text
	
	cnx = mysql.connector.connect(user='root', password='password',
                              host='127.0.0.1',
                              database='myTeam')
	cursor = cnx.cursor()
	insert = ("INSERT INTO Teams (TeamAbbreviation, TeamName) VALUES (%s, %s)")
	for team,name in teamNames.items():
		insert_data = (team,name)
		cursor.execute(insert,insert_data)
	cnx.commit()
	cursor.close()
	cnx.close()



def checkWin(outcome):
	if outcome == 'L':
		return False
	else:
		return True

def findLastGame(team,soup):
	meta_data = soup.find_all('div', attrs={'id':'meta'})
	info = meta_data[0].find_all('p')
	if info[3].text[1:10] == 'Last Game':
		last_game_string = "".join(info[3].text.split())[9:]
		outcome = last_game_string[0]
		score = ''.join([i for i in last_game_string if not(i.isalpha())])
		game_type = ''.join([i for i in last_game_string[1:] if (i.isalpha())])
		opposing_team = ''.join(i for i in game_type if not i.islower())
		Home = True
		if 'at' in game_type:
			Home = False
		wonGame = checkWin(outcome)
		cnx = mysql.connector.connect(user='root', password='password',
                              host='127.0.0.1',
                              database='myTeam')
		cursor = cnx.cursor()
		insert = ("INSERT INTO LastGames (Team,WIN,AT_HOME,OpposingTeam,Score) VALUES (%s,%s,%s,%s,%s)")
		insert_data = (team,wonGame,Home,opposing_team,score)
		cursor.execute(insert,insert_data)
		cnx.commit()
		cursor.close()
		cnx.close()
	else:
		return

def findPlayers(team, soup):
	players = dict()
	table = soup.find_all('table',attrs={'id':'roster'})
	tbody = table[0].find('tbody')
	trows = tbody.find_all('tr')
	for i in range(len(trows)):
		number = (trows[i].find('th',attrs={'data-stat':'number'}).text)
		if len(number) == 0:
			number = -1
		else:
			number = int(number)
		names = trows[i].find('td',attrs={'data-stat':'player'}).text.replace("(TW)","").split()
		first = names[0]
		if len(names) > 1:
			second = names[1]
		else:
			second = ''
	 	position = (trows[i].find('td',attrs={'data-stat':'pos'}).text)
	 	players[" ".join(names)] = (number,first,second,position)
	cnx = mysql.connector.connect(user='root', password='password',
                              host='127.0.0.1',
                              database='myTeam')
	cursor = cnx.cursor()
	insert = ("INSERT INTO Players (PlayerNumber,FirstName,LastName,Position,Team) VALUES (%s, %s,%s,%s,%s)")
	for player,data in players.items():
		insert_data = (data[0],data[1],data[2],data[3],team)
		cursor.execute(insert,insert_data)
	cnx.commit()
	cursor.close()
	cnx.close()


def findPlayerStatistics(team,url):
	driver = webdriver.Chrome('./chromedriver')
	driver.get(url)
	html = driver.page_source
	soup = BeautifulSoup(html,'html.parser')
	tables = soup.find_all('table',attrs={'id':'per_game'})
	rows = tables[0].find_all('tr')
	stats = dict()
	for row in rows:
		data = row.find_all('td')
		if len(data) == 0:
			continue
		else:
			player_name = data[0].text
			games_played = data[1].text
			ppg = data[26].text
			apg = data[21].text
			rpg = data[20].text
			bpg = data[23].text
			spg = data[22].text
			tovpg = data[24].text
			ft_perc = data[17].text
			fg_perc = data[7].text
			if ppg == '':
				ppg = -1
			if apg == '':
				apg = -1
			if rpg == '':
				rpg = -1
			if bpg == '':
				bpg = -1
			if spg == '':
				spg = -1
			if tovpg == '':
				tovpg = -1
			if ft_perc == '':
				ft_perc = -1
			if fg_perc == '':
				fg_perc = -1
			stats[player_name] = {'PPG':ppg,'APG':apg,'RPG':rpg,'BPG':bpg,'SPG':spg,'TOV_PER_GAME':tovpg,'FG%':fg_perc,'FT%':ft_perc}
	driver.quit()
	cnx = mysql.connector.connect(user='root', password='password',
                              host='127.0.0.1',
                              database='myTeam')
	cursor = cnx.cursor(buffered=True)
	for player,stats in stats.items():
		search = ("SELECT * FROM Players WHERE FirstName = %s AND LastName= %s AND Team=%s")
		names = player.split()
		first = names[0]
		if len(names) > 1:
			second = names[1]
		else:
			second = ' '
		query_params = (first,second,team)
		cursor.execute(search,query_params)
		if cursor.rowcount == 0:
			continue
		for row in cursor:
			player_id = row[0]
		insert = ("INSERT INTO PlayerSTATs (PlayerID,PPG,APG,RPG,SPG,BPG,TOVPG,FT_PERC,FG_PERC) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)")
		insert_data = (player_id,stats['PPG'],stats['APG'],stats['RPG'],stats['SPG'],stats['BPG'],stats['TOV_PER_GAME'],stats['FT%'],stats['FG%'])
		cursor.execute(insert,insert_data)
	cnx.commit()
	cursor.close()
	cnx.close()



def main():
	URLS = dict()
	for team in TEAMS:
		url_begin = "https://www.basketball-reference.com/teams/"
		url_end = "/2019.html"
		URLS[team] = url_begin + team + url_end
	
	insertTeams(URLS)
	print("Inserted Teams Into Database")

	for team,url in URLS.items():
		r = requests.get(url)
		soup = BeautifulSoup(r.text, 'html.parser')
		findLastGame(team,soup)
		findPlayers(team,soup)
	print("Inserted Last Games Into Database")
	print("Inserted Players Into Database")
	for team,url in URLS.items():
		findPlayerStatistics(team,url)
	print("Inserted Players Statistics Into Database")

	  
if __name__== "__main__":
	main()