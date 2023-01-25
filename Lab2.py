def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'name': 'Abdullah',
        'Last name': 'Mahfouz',
        'fav player':'Ronaldo',
        'Most iconic' :'Ozil',
        'Fav Footballers': [
           'Ronaldo',
            'Ozil',
            'Mbappe',
            'Ramos'
         ],
        'Ronaldo Vs Messi Goals' : [
            { 
             'player': 'Ronaldo',
             'Goals' : 819,
             'assits': 794
            },
            {
                'player ': 'Messi',
                'goals' : 819,
                'assits': 500
            }
        ]
    }

    # TODO: Step 3 - Add another movie to the data structure
 
    print_Fav_players_name(about_me)
    add_fav_teams(about_me, ('Real Madrdid', ' Man United', 'Liverpool'))
    print_fav_teams(about_me)
# TODO: Step 4 - Function that prints student name and ID	
def print_Fav_players_name(Fav_players):
    print(f"{Fav_players['name']} Thinks {Fav_players['Most iconic'].title()} will always be the best passer")
    
    
# adds fav teams
def add_fav_teams(fav_teams, teams):
    fav_teams['teams'].extend(teams)
    for i, p in enumerate(fav_teams['teams']):
       fav_teams['teams'][i] = p.title()
    
    fav_teams['teams'].sort()
    
    pass 
    
# prints fac teams
def print_fav_teams(fav_teams):
    print('\nThe team lis is:')
    for t in fav_teams['teams']:
        print(f'- {t}')
  

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(Rivaly):
 return
   

if __name__ == '__main__':
    main()