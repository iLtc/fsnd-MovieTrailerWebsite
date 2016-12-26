import media
import fresh_tomatoes

movieList = [
    [
        "Thunderbirds",
        "http://static.rogerebert.com/uploads/movie/movie_poster/thunderbirds-2004/"
        "large_h2tdVvkuNhZmYk5LIxnyQ2xdXq1.jpg",
        "https://www.youtube.com/watch?v=17Y8iDnRoSc"
    ],
    [
        "Harry Potter and the Deathly Hallows",
        "http://vignette2.wikia.nocookie.net/harrypotter/images/6/65/"
        "Harry-Potter-and-the-Deathly-Hallows-Part-1-poster.jpg/revision/latest?cb=20101001182826",
        "https://www.youtube.com/watch?v=MxqsmsA8y5k"
    ],
    [
        "Divergent",
        "https://upload.wikimedia.org/wikipedia/en/d/d4/Divergent.jpg",
        "https://www.youtube.com/watch?v=Aw7Eln_xuWc"
    ]
]

movies = []

for movie in movieList:
    temp = media.Movie(movie[0], movie[1], movie[2])

    movies.append(temp)

fresh_tomatoes.open_movies_page(movies)