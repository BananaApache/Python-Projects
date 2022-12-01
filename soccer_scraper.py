
import requests
from bs4 import BeautifulSoup as bs

base_url = "https://www.espn.com/soccer/fixtures/_/date"
date = input("Enter a day: ")
# day = "04"
# date = f"202209{day}"

r = requests.get(f"{base_url}/{date}")

soup = bs(r.content, 'html.parser')

game_tables = soup.find_all("div", class_="responsive-table-wrap")
games = []
dates = []

for game in game_tables:
    tbody = game.find("tbody")
    for child in tbody.descendants:
        if child.find("abbr") == None:
            continue
        elif child.find("abbr") == -1:
            continue
        else:
            if child.find("a", class_="team-name") is not None:
                team_name = str(child.find("a", class_="team-name").find("span"))
                games.append(team_name[6:len(team_name) - 7])

for t in soup.find_all("td", attrs={"data-behavior": "date_time"}):
    time = t.get("data-date")
    time = time[11:len(time)-1]
    hour = int(time[:2]) - 4
    minute = time[3:]
    if hour > 12:
        time = f"{hour - 12}:{minute} PM"
    elif hour < 12:
        time = f"{hour}:{minute} AM"
    elif hour == 12:
        time = f"{hour}:{minute} PM"
    print(time.split("-")[2][:2])
    
prev = ""
for i in games:
    if i == prev:
        games.remove(i)
    prev = i

vs_games = []
count = 0

for x in range(len(games)):
    if count % 2 == 0:
        vs_games.append(games[x] + " vs " + games[x+1])
    count += 1

for view in vs_games:
    print(view)
