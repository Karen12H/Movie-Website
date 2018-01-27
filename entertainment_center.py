import fresh_tomatoes
import media

last_holiday = media.Movie("Last Holiday",
                           "A terminally ill woman fulfilling her dreams",
                           "https://upload.wikimedia.org/wikipedia/en/0/0e/Last_holiday.jpg",
                           "https://www.youtube.com/watch?v=fBUcxMNInL8")

the_shawshank_redemption = media.Movie("The Shawshank Redemption",
                                       "A banker sentenced life term prison for crime he did not commit",
                                       "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                                       "https://www.youtube.com/watch?v=6hB3S9bIaco")

zootopia = media.Movie("Zootopia",
                       "A rabbit police solving crime in animal city",
                       "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                       "https://www.youtube.com/watch?v=jWM0ct-OLsM")

the_intern = media.Movie("The Intern",
                         "A retired executive from DEX One applies to a senior citizen intern program",
                         "https://upload.wikimedia.org/wikipedia/en/c/c9/The_Intern_Poster.jpg",
                         "https://www.youtube.com/watch?v=ZU3Xban0Y6A")

warcraft = media.Movie("Warcraft",
                       "Orcs escape from their dying world through a portal to the human realm of Azeroth",
                       "https://upload.wikimedia.org/wikipedia/en/5/56/Warcraft_Teaser_Poster.jpg",
                       "https://www.youtube.com/watch?v=2Rxoz13Bthc")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "A screenwriter mysteriously going back to the 1920s everyday at midnight in Paris",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

movies = [last_holiday, the_shawshank_redemption, zootopia, the_intern, warcraft, midnight_in_paris]
fresh_tomatoes.open_movies_page(movies)
