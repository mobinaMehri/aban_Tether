from utils.services import MovieServices, PersonServices, CastPivotMovieServices, DirectorPivotMovieServices


def init_data():
    person = PersonServices()
    person.insert('ali', 27)
    person.insert('mobina', 28)
    person.insert('zahra', 29)
    person.insert('hesam', 30)
    person.insert('Max', 35)
    person.insert('Jo', 40)

    movie = MovieServices()
    movie.insert('Inception', 'Drama', '2023-10-01')
    movie.insert('WorldWarZ', 'Action', '2023-10-10')

    cast = CastPivotMovieServices()
    cast.insert(1, 1)
    cast.insert(1, 2)
    cast.insert(2, 3)
    cast.insert(2, 4)

    director = DirectorPivotMovieServices()
    director.insert(1, 4)
    director.insert(2, 5)


cast = CastPivotMovieServices()
cast_result = cast.get_all()
print(cast_result)

director = DirectorPivotMovieServices()
director_result = director.get_all()
print(director_result)
