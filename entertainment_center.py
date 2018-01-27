import fresh_tomatoes
import media

last_holiday = media.Movie("Last Holiday","A terminally ill woman fulfilling her dreams",
                           "https://en.wikipedia.org/wiki/Last_Holiday_(2006_film)#/media/File:Last_holiday.jpg",
                           "https://www.youtube.com/watch?v=fBUcxMNInL8")

the_shawshank_redemption = media.Movie("The Shawshank Redemption","A banker sentenced life term prison for crime he did not commit",
                                       "https://en.wikipedia.org/wiki/The_Shawshank_Redemption#/media/File:ShawshankRedemptionMoviePoster.jpg",
                                       "https://www.youtube.com/watch?v=6hB3S9bIaco")

zootopia = media.Movie("Zootopia","A rabbit police solving crime in animal city",
                       "https://en.wikipedia.org/wiki/Zootopia#/media/File:Zootopia.jpg",
                       "https://www.youtube.com/watch?v=jWM0ct-OLsM")

the_intern = media.Movie("The Intern","A retired executive from DEX One applies to a senior citizen intern program",
                         "https://en.wikipedia.org/wiki/The_Intern_(2015_film)#/media/File:The_Intern_Poster.jpg",
                         "https://www.youtube.com/watch?v=ZU3Xban0Y6A")

warcraft = media.Movie("Warcraft","Orcs escape from their dying world through a portal to the human realm of Azeroth",
                       "https://en.wikipedia.org/wiki/Warcraft_(film)#/media/File:Warcraft_Teaser_Poster.jpg",
                       "https://www.youtube.com/watch?v=2Rxoz13Bthc")

midnight_in_paris = media.Movie("Midnight in Paris","A screenwriter mysteriously going back to the 1920s everyday at midnight in Paris",
                                "https://en.wikipedia.org/wiki/Midnight_in_Paris#/media/File:Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

movies = [last_holiday, the_shawshank_redemption, zootopia, the_intern, warcraft, midnight_in_paris]
fresh_tomatoes.open_movies_page(movies)