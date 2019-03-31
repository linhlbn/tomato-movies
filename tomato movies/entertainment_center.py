import fresh_tomatoes
import media
#call library media.py and Movie is the class in library
#here are instance variables
kimiNoNawa = media.Movie(
			             "Kimi No Nawa",
                         "When will we meet?",
                         "http://static.hdonline.vn/i/resources/new/film/215x311/2016/05/11/your-name.jpg",
                         "https://www.youtube.com/watch?v=hRfHcp2GjVI")

fiveCmPerSecond = media.Movie(
                              "5 centimeters per second",
                              "The story about the beautiful sadness",
                              "https://khongphaivyvy.files.wordpress.com/2015/04/6011-centimeters-per-second-1920x1080-anime-wallpaper.jpg",
                              "https://www.youtube.com/watch?v=wdM7athAem0")

goblin = media.Movie(
                     "Goblin",
                     "I will find you till the end, my destiny - A cruel romantic sad love story between an immortable goblin and his young bride",
                     "http://images6.fanpop.com/image/photos/40000000/Goblin-Poster-korean-dramas-40081052-346-500.jpg",
                     "https://www.youtube.com/watch?v=U2UrxFwMORE")

youWhoCameFromStars = media.Movie(
                                  "You who came from stars",
                                  "A fiction love story",
                                  "http://image.phimmoi.net/film/587/poster.medium.jpg",
                                  "https://www.youtube.com/watch?v=GHDAsG6yhus")

inception = media.Movie(
                        "Inception",
                        "Describe the Lucid dream theory ",
                        "https://images-na.ssl-images-amazon.com/images/I/51ShRC1YMrL.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

theInternship = media.Movie(
                            "the Internship",
                            "the Internship in Google company",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/e/ed/The-internship-poster.jpg/220px-The-internship-poster.jpg	",
                            "https://www.youtube.com/watch?v=cdnoqCViqUo")

# print(avatar.storyline)                     
# avatar.show_trailer()
movies = [kimiNoNawa, fiveCmPerSecond, goblin, youWhoCameFromStars, inception, theInternship]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGSS)
# print(media.Movie.__doc__)   -> documentation in triple quotes
print(media.Movie.__doc__)
# print(media.Movie.__name__)   -> name of class
# print(media.Movie.__module__)   -> name of module (or library contain class) (media)
