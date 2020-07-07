import datetime
import database

menu = """Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Add user to the app.
7) Search for a movie.
8) Exit

Your selection: """
welcome = "Welcome to the watchlist app!"


print(welcome)
database.create_tables()


def prompt_add_movie():
    """
    Prompt a user to add new movie
    """
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-YYYY): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()

    database.add_movie(title, timestamp)


def print_movie_list(heading, movies):
    """
    Print list of upcoming movies
    """
    print(f"-- {heading} Movies --")
    for _id, title, release_date in movies:
        movie_date = datetime.datetime.fromtimestamp(release_date)
        human_date = movie_date.strftime("%b %d %Y")
        print(f"{_id}: {title} (on {human_date})")
    print("--- \n")


def prompt_watch_movie():
    """
    Mark a movie as watched
    """
    username = input("Username: ")
    movie_id = input("Movie: ID: ")
    database.watch_movie(username, movie_id)


def prompt_add_user():
    username = input("Username: ")
    database.add_user(username)


def prompt_show_watched_movies():
    username = input("Username: ")
    movies = database.get_watched_movies(username)
    if movies:
        print_movie_list(f"{username}'s watched movies", movies)
    else:
        print("That user has no watched movies.")


user_input = input(menu)

while user_input != "8":
    if user_input == "1":
        prompt_add_movie()
        user_input = input(menu)
    elif user_input == "2":
        movies = database.get_movies(True)
        print_movie_list("Upcoming", movies)
        user_input = input(menu)
    elif user_input == "3":
        movies = database.get_movies()
        print_movie_list("All", movies)
        user_input = input(menu)
    elif user_input == "4":
        prompt_watch_movie()
        user_input = input(menu)
    elif user_input == "5":
        prompt_show_watched_movies()
        user_input = input(menu)
    elif user_input == "6":
        prompt_add_user()
        user_input = input(menu)
    else:
        print("Invalid input, please try again!")
