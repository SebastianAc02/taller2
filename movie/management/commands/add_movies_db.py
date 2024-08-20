from django.core.management.base import BaseCommand
import os 

import json 

class Command(BaseCommand):
    help = "Load movies from movie_desription.json intop the movie model"

    def handle(seld, *args, **kwargs ):
        json_file_path - 'movies.json'

        with open(jsoon_file_path, 'r') as file:
            movies = json.load(file)


            for i in range(100):
                movie = movies[i]
                exist = Movie.objects.filter( title = movie['title']).first()
                if not exist:
                    Movie.objects.create(title = movie['title'],
                    image = 'movie/images/Default.jpg',
                    genre = movie['genre'],
                    year = movie['year'])



                    