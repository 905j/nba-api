import requests

url = 'https://api.balldontlie.io/v1/players'
header = {'Authorization' : '940a9c22-0ac1-4315-9fb7-562db67e1162'}

response = requests.get(url, headers=header)

print(response.status_code)
playerInfo = response.json()["data"]
for player in playerInfo:
  print(f"{player['first_name']} {player['last_name']} went to {player['college']} for college and was drafted in {player['draft_year']}.")
