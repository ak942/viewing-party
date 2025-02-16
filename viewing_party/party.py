# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movies = {}
    if title != None and genre != None and rating != None:
        movies= {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return movies
    else:
        return None


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    #we want to move the movies (title, genre, rating) into the user_data["watch"]

    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum_avg_rating = 0.0

    if len(user_data["watched"]) == 0:
        return sum_avg_rating
    else:
        for movie in user_data["watched"]:
            sum_avg_rating += movie["rating"]
            avg_rating = sum_avg_rating / len(user_data["watched"])
        return avg_rating
    
def get_most_watched_genre(user_data):
    freq = {}
    highest_count = 0

    if len(user_data["watched"]) == 0:
        return None

    for movie in user_data["watched"]:
        if movie["genre"] in freq:
            freq[movie["genre"]] += 1
        else: 
            freq[movie["genre"]]= 1

    for genre, count in freq.items():
        if count > highest_count:
            highest_count = count
            highest_genre = genre
    return highest_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
# 1. Create a function named `get_unique_watched`. This function should...
# - take one parameter: `user_data`
#   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries, and a `"friends"`
#     - This represents that the user has a list of watched movies and a list of friends
#     - The value of `"friends"` is a list
#     - Each item in `"friends"` is a dictionary. This dictionary has a key `"watched"`, which has a list of movie dictionaries.
#     - Each movie dictionary has a `"title"`.
# - Consider the movies that the user has watched, and consider the movies that their friends have watched. 
#   Determine which movies the user has watched, but none of their friends have watched.
# - Return a list of dictionaries, that represents a list of movies

# 2. Create a function named `get_friends_unique_watched`. This function should...
# - take one parameter: `user_data`
#   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries, and a `"friends"`
#     - This represents that the user has a list of watched movies and a list of friends
#     - The value of `"friends"` is a list
#     - Each item in `"friends"` is a dictionary. This dictionary has a key `"watched"`, which has a list of movie dictionaries.
#     - Each movie dictionary has a `"title"`.
# - Consider the movies that the user has watched, and consider the movies that their friends have watched. 
# Determine which movies at least one of the user's friends have watched, but the user has not watched.
# - Return a list of dictionaries, that represents a list of movies

def get_unique_watched(user_data):
    unique_movie = []
    friends_watched = user_data["friends"]
    friend_watch_list= []
    user_watched = user_data["watched"]

    for friends in friends_watched:
        for movie in friends["watched"]:
            if movie["title"] not in friend_watch_list:
                friend_watch_list.append(movie["title"])
    
    for user_movie in user_watched:
        if user_movie["title"] not in friend_watch_list:
            unique_movie.append(user_movie)
    print("unique_movies", unique_movie)
    return unique_movie

def get_friends_unique_watched(user_data):
    unique_movie = []
    user_watched_list_titles= []
    friends_watched_list_title = []

    for user_movie in user_data["watched"]:
        user_watched_list_titles.append(user_movie["title"])
    
    for friends in user_data["friends"]:
        for movie in friends["watched"]:
            if movie["title"] not in user_watched_list_titles and movie["title"] not in friends_watched_list_title:
                friends_watched_list_title.append(movie["title"])
                unique_movie.append(movie)
                
    return unique_movie

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
# 1. Create a function named `get_available_recs`. This function should...
# - take one parameter: `user_data`
#   - `user_data` will have a field `"subscriptions"`. The value of `"subscriptions"` is a list of strings
#     - This represents the names of streaming services that the user has access to
#     - Each friend in `"friends"` has a watched list. Each movie in the watched list has a `"host"`, which is a string that says what streaming service it's hosted on
# - Determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The user has not watched it
#   - At least one of the user's friends has watched
#   - The `"host"` of the movie is a service that is in the user's `"subscriptions"`
# - Return the list of recommended movies

def get_available_recs(user_data):
    user_not_watched = get_friends_unique_watched(user_data)
    list_of_rec_movies = []

    for movie in user_not_watched:
        if movie["host"] in user_data["subscriptions"]:
            list_of_rec_movies.append(movie)
    
    return list_of_rec_movies

    # match movie title key to the title key of user_not_watched 
    # check for value in key 'host' is found in the value of subscription 

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

# 1. Create a function named  `get_new_rec_by_genre`. This function should...
# - take one parameter: `user_data`
# - Consider the user's most frequently watched genre. Then, determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The user has not watched it
#   - At least one of the user's friends has watched
#   - The `"genre"` of the movie is the same as the user's most frequent genre
# - Return the list of recommended movies

# 2. Create a function named  `get_rec_from_favorites`. This function should...
# - take one parameter: `user_data`
#   - `user_data` will have a field `"favorites"`. The value of `"favorites"` is a list of movie dictionaries
#     - This represents the user's favorite movies
# - Determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The movie is in the user's `"favorites"`
#   - None of the user's friends have watched it
# - Return the list of recommended movies
def get_new_rec_by_genre (user_data):
    user_not_watched = get_friends_unique_watched(user_data)
    most_freq_genre = get_most_watched_genre(user_data)
    rec_movies_by_genre = []

    for movies in user_not_watched:
        if movies["genre"] == most_freq_genre:
            rec_movies_by_genre.append(movies)
    
    return rec_movies_by_genre


def get_rec_from_favorites(user_data):
    user_favorite_movie = []
    user_watched = get_unique_watched(user_data)
    favorite_movie_titles = []

    for movie in user_data["favorites"]:
        favorite_movie_titles.append(movie["title"])
    
    for movie in user_watched:
        if movie["title"] in favorite_movie_titles:
            user_favorite_movie.append(movie)
    return user_favorite_movie

    