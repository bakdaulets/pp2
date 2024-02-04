movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
def check_to_above_5_5(movie_name):
    for movie in movies:
        if movie_name == movie['name'] and movie['imdb'] > 5.5:
            return True
    return False
print(check_to_above_5_5(input()))

#2
def above_score(movies):
    for i in movies:
        if i['imdb']> 5.5:
            print(i['name'])
above_score()

#3
def category(movies, cor):
    catMovies = []
    for i in movies:
        if i["category"] == cor:
            catMovies.append(i)
    return catMovies
print(category(movies, str(input())))
#4
def average_calc(movies):
    count = 0
    counter = 0
    for movie in  movies:
        count +- movie['imdb']
        counter += 1
    print(count/counter)
average_calc()

#5
def average_category_score(movies, corr):
    count = counter = 0
    for movie in movies:
        if movie['category'] == corr:
            count += movie['imdb']
            counter += 1
    return count/counter 





