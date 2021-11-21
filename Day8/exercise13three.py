#print users name,age,fav_movie,fav_song in dict all value taken by user input
user = {}
name = input('what is your name :')
age = input('what is your age :')
fav_movies = input('Your fav movies seprted by comma :').split()
fav_songs = input('you fav songs seprted by comma :').split()
user['nmae'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_songs'] = fav_songs
print(user)
print("-----------------")
for key,value in user.items():
    print(f"{key}:{value}")
