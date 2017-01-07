import media
import fresh_tomatoes


toy_story = media.Movie(
    'Toy Story',
    'A story of a boy and his toys that come to life',
    'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
    'https://youtu.be/4KPTXpQehio'
)

avatar = media.Movie(
    'Avatar',
    'A marine on an alien planet',
    'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
    'https://youtu.be/5PSNL1qE6VY'
)

school_of_rock = media.Movie(
    'School of Rock',
    'Using rock music to learn',
    'https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg',
    'https://youtu.be/3PsUJFEBC74'
)

ratatouille = media.Movie(
    'Ratatouille',
    'A rat is a chef in Paris',
    'https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg',
    'https://youtu.be/niD-jahFURU'
)

midnight_in_paris = media.Movie(
    'Midnight in Paris',
    'Going back in time to meet authors',
    'https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg', # NOQA
    'https://youtu.be/FAfR8omt-CY'
)

hunger_games = media.Movie(
    'The Hunger Games',
    'A really real reality show',
    'https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg',
    'https://youtu.be/mfmrPu43DF8'
)

favorite_movies = [
    toy_story, avatar, school_of_rock,
    ratatouille, midnight_in_paris, hunger_games
]

fresh_tomatoes.open_movies_page(favorite_movies)
