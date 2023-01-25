def main():

    # a complex data structure
    fav_soccer_player = {
        'name': 'Cristiano Ronaldo',
        'nickname': 'CR7',
        'player_best_team':'Real-Madrid',
        'players_played_with': 
            [
             'Marclo',
             'Pepe',
             'benzema'
        ],
          
        'Rivals':[
            { 
             'Player': 'Messi',
             'Goals' : 794,
             'assits': 350
            },
            {
              'Player ': 'Cristiano Ronaldo',
              'goals' : 819,
              'Asists': 266
            }
        ]
    }

    # Added New rival
    fav_soccer_player['Rivals'].insert(1,{'Player': 'Zlatan Ibrahimović', 'Goals':  574, 'Assits': 157 })
    add_other_fav_players(fav_soccer_player,('Ozil', 'Bale', 'ramos'))
    print_player_name(fav_soccer_player)
    # Function that prints the player nickname and name 
def print_player_name(soccer_player):
    print(f"{soccer_player['nickname']} Aka {soccer_player['name'].title()} has to be one of the best players of all-time for {soccer_player['']}  ")
   
    
    
# adds fav teams
def add_other_fav_players(team,):
   print( f'\n He played with players such as:')
   for p in team['players_played_with']:
       print(f'- {p}')
       
    
# prints fac teams
def print_Rivals(rival):
   
  return

# Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(Rivaly):
    return
   

if __name__ == '__main__':
    main()