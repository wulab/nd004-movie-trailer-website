class Movie():
    """A movie with title, storyline, along with its respective box art imagery
    and movie trailer website
    """

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
