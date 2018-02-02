import webbrowser #Allows open of web page

class Movie():
    """Class describing information contains in a movie.
    The __init__ is a constructor. It is called when instances within Class Movie() are create.
    Instance is object inside the class associated with instance self.
    Instances in Class Movie() are movie_title, movie_storyline, poster_image_url, trailer_youtube_url.
    Self is a keyword refers to instance (i.e.movie title: Zootopia)
    Args:
        title(str): movie's title
        storyline(str): movie's storyline
        poster_image_url(url): movie's poster image link
        trailer_youtube_url(url): movie's trailer link from youtube
    """
    def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_youtube_url):
        self.title = movie_title #instance variable
        self.storyline = movie_storyline #instance variable
        self.poster_image_url = poster_image_url #instance variable
        self.trailer_youtube_url = trailer_youtube_url #instance variable

    def show_trailer(self):
        """Shows movie's youtube trailer from clicked movie on website"""
        webbrowser.open(self.trailer_youtube_url)
        #opens a web page, allows listed movie trailers linked from youtube
        #play on website.
