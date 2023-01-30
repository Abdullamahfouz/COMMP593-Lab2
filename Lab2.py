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
    about_me["movies"].append({"title": "spider-man no way home ", "genre": "action"})
    print_student_name_and_id(about_me)
    add_pizza_toppings(about_me, ("olives", "onions", "steak"))
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

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return
    
if __name__ == '__main__':
    main()