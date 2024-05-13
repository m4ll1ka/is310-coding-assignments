favorite_movies =[
    {
        "name": "The Matrix I",
        "release_year": 1999,
        "sequels": ["The Matrix II", "The Matrix III", "The Matrix IV"]
    },
    {
        "name": "Star Wars IV",
        "release_year": 1977,
        "sequels": ["Star Wars V", "Star Wars VI", "Star Wars VII", "Star Wars VIII", "Star Wars IX"],
        "prequels": ["Star Wars I", "Star Wars II", "Star Wars III"]
    }
]

# print(favorite_movies)
# total_fav_movies = len(favorite_movies)
# print("How many total favorite movies do we have?", total_fav_movies)
# print(type(favorite_movies), type(favorite_movies[0]))

print('Enter your favorite movie of the last year:')
recent_favorite_movie = input()
print('Your favorite movie is of the last year:', recent_favorite_movie)