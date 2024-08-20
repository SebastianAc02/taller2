import pandas as pd
import json
import os

print("Current working directory:", os.getcwd())
print("Files in this directory:", os.listdir())

try:
    df = pd.read_csv('/Users/sebastianacosta/development/p1/Taller-PI1-20241/movies_initial.csv')
    df.to_json('movies.json', orient='records')
    
    with open('movies.json', 'r') as file:
        movies = json.load(file)
    
    for i in range(1):  # Changed to 1 since you're breaking after first iteration
        movie = movies[i]
        print(movie)
    
    print('success')
except FileNotFoundError:
    print("Error: 'movies_initial.csv' not found. Please check the file location.")
except Exception as e:
    print(f"An error occurred: {e}")