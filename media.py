import webbrowser

class Movie:
    """This is movie class

    Attributes:
        movie_title (str): The title of the movie
        poster_image (str): The url address of the poster
        trailer_youtube (str): The url of the trailer on youtube
    """

    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)