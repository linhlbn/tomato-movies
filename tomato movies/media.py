import webbrowser

class Movie():
    #triple quotes to define my documentation
    """THIS CLASS PROVIDES A WAY TO STORE MOVIE RELATED INFORMATION"""
#Instance/ Instance variables called Toy_story, Avatar. New Function (Constructor) is def init
#Constructor creates space memory for 'new instance' called Toy_story
# init belong to python, self is obj being created (in this case is toy story)
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
#here are data (init ~ constructor) and methods in class
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
