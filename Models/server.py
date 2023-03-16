from players import players

kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
}

#Challenge 1
class Player:

    def __init__(self, player):
        self.name = player['name']
        self.age = player['age']
        self.position = player['position']
        self.team = player['team']
    
    @classmethod
    def get_team(cls, team_list):
        new_list = []
        for i in range(len(team_list)):
            new_list.append(team_list[i])
        return new_list



#Challenge 2
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

#BONUS
new_team = [Player.get_team(players)]

#Challenge 3
new_team = []

def loop_players(players):
    for i in range(len(players)):
        new_team.append(players[i])

loop_players(players)

Player.get_team(players)