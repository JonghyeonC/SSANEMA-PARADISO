import requests
import json


movie_info = []
movie_ids = []
genre_list = []


API_KEY = 'f2afac401b045c95588f9124fd3e1840'
Genre_Url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=ko'
response_1 = requests.get(Genre_Url).json()
genres = response_1.get('genres')
for genre in genres:

    genre_temp = {
        "pk": genre.get('id'),
        "name": genre.get('name')
    }
    genre_data = {
        "pk": genre_temp.get("pk"),
        "model" : "movies.genre",
        "fields" : {
            "name": genre_temp.get("name")
        }
    }
    genre_list.append(genre_data)

with open('movies/fixtures/genre.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(genre_list, indent=4, ensure_ascii=False))

for i in range(1, 10):
    MovieId_Url = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko&page={i}'
    response_2 = requests.get(MovieId_Url).json()
    movies = response_2.get('results')
    for movie in movies:
        movie_ids.append(movie.get('id'))

for index, movie_id in enumerate(movie_ids):
    MovieInfo_Url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=ko'
    MovieCredit_Url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}&language=ko'
    MovieVideo_Url = f'https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={API_KEY}&language=en-US'

    response_3 = requests.get(MovieInfo_Url).json()
    MovieVideo = requests.get(MovieVideo_Url).json()
    response_credit = requests.get(MovieCredit_Url).json()

    credit = response_credit.get('cast')
    crews = response_credit.get('crew')
    videos = MovieVideo.get('results')

    genre_num = []
    for genre in response_3['genres']:
        genre_num.append(genre['id'])

    cast_info = []
    for cast in credit:
        cast_each = {}
        cast_each['id'] = cast['id'],
        cast_each['name'] = cast['name']
        cast_each['profile_path'] = cast['profile_path']
        cast_info.append(cast_each)
    
    crew_info = []
    for crew in crews:
        crew_each = {}
        if crew["job"] == "Director":
            crew_each['id'] = crew["id"] 
            crew_each['name'] = crew["name"] 
            crew_info.append(crew_each)

    video_list = []
    for video in videos:
        video_each = {}
        if video["type"] == "Trailer" and video["site"] == "YouTube":
            video_each['key'] = video['key']
            video_list.append(video_each)

    video_urls = []
    for url in video_list:
        if url:
            video_urls.append(url)

    similar_movies = []
    for i in range(1, 5):
        MovieSimilar_Url = f'https://api.themoviedb.org/3/movie/{movie_id}/similar?api_key={API_KEY}&language=ko&page={i}'
        similar = requests.get(MovieSimilar_Url).json()
        movies = similar.get('results')
        for movie in movies:
            movie_list = {}
            movie_list['id'] = movie['id'],
            movie_list['title'] = movie['title'],
            movie_list['poster_path'] = movie['poster_path']
            similar_movies.append(movie_list)

    movie_data = {
        "pk": index + 1,
        "model" : "movies.movie",
        "fields": {
            "movie_id" : movie_id,
            "title" : response_3['title'],
            "original_title" : response_3.get('original_title'),
            "genres" : genre_num,
            "overview" : response_3.get('overview'),
            "popularity" : response_3.get('popularity'),
            "backdrop_path" : response_3.get('backdrop_path'),
            "poster_path" : response_3.get('poster_path'),
            "country" : response_3.get('production_countries'),
            "release_date" : response_3.get('release_date'),
            "runtime" : response_3.get('runtime'),
            "vote_average" : response_3.get('vote_average'),
            "vote_count" : response_3.get('vote_count'),
            "cast_info" : cast_info,
            "crew_info" : crew_info,
            "video_url" : video_urls,
            "similar_movies" : similar_movies,
        }
    }
    movie_info.append(movie_data)
    genre_num = []
    cast_info = []
    crew_info = []
    video_list = []
    video_url = []
    similar_movies = []

    

with open('movies/fixtures/movie.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(movie_info, indent=4, ensure_ascii=False))