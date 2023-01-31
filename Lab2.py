def main():

    #complex data structure
    about_me = {
        "full_name": "Abdullah Mahfouz",
        "student_id": 10277237,
        "pizza_toppings": [
             "Chicken", 
             "Mushrooms", 
             "Cheese"
             ]
            ,
        "movies": [
            {
            "title": "The Dark nigt", 
             "genre": "action"
             },
            {
            "title": "Whiplash", 
             "genre": "psychological drama"
             }
        ]
    }
    #Added another movie to the data structure
    about_me["movies"].append({"title": "Spider-man no way home ", "genre": "Super-Hero"})
    #calling all functions in the script
    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    add_pizza_toppings(about_me, ("Olives", "Onions", "Steak"))
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me["movies"])
# Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = about_me["full_name"]
    first_name = full_name.split()[0]
    student_id = about_me["student_id"]
    print(f"My name is {full_name}, but you can call me Sir {first_name}.")
    print(f"My student ID is {student_id}.")
    
# Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me["pizza_toppings"].extend(toppings)
    about_me["pizza_toppings"] = sorted(about_me["pizza_toppings"])
    about_me["pizza_toppings"] = [topping.lower() for topping in about_me["pizza_toppings"]]

#  Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
     print("\nMy favourite pizza toppings are:")
     for topping in about_me["pizza_toppings"]:
        print("-", topping)
 
# Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    movie_genres = [movie['genre'] for movie in about_me['movies']]
    genres_str = ', '.join(movie_genres)
    if len(movie_genres) > 1:
        genres_str = genres_str.rsplit(', ', 1)[0] + ' and ' + genres_str.rsplit(', ', 1)[1]
    print(f"\nI like to watch {genres_str} movies.")

# Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
  movie_titles = [movie["title"].title() for movie in movie_list]
  print("\nSome of my favourite movies are{}!".format(", ".join(movie_titles)))
    
if __name__ == '__main__':
    main()