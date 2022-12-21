import spacy
nlp = spacy.load('en_core_web_md')


# movie object
class Movie:
    def __init__(self, name, description, genre='', length=0.0):
        self.name = name
        self.description = description
        self.genre = genre
        self.length = length

    def compare_by_description(self, movie_description):
        self_description = nlp(self.description)
        other_description = nlp(movie_description)
        _similarity = self_description.similarity(other_description)
        return _similarity


# compare movie descriptions for similarities
def find_similar(_movie):
    highest_similarity = 0
    closest_movie = _movie

    for movie_key, movie_value in movies_dictionary.items():
        similarity = _movie.compare_by_description(movie_value.description)
        if similarity > highest_similarity:
            highest_similarity = similarity
            closest_movie = movie_value
            
    return closest_movie.name, highest_similarity


# import movie data
def import_movie_data(movies_data):
    try:
        with open(movies_data, 'r') as movies:
            for line in movies:
                properties = line.split(" :")
                new_movie = Movie(properties[0], properties[1])
                movies_dictionary[new_movie.name] = new_movie
    except (FileNotFoundError, FileExistsError) as error:
        print(error)


# declare variables
movies_file = "movies.txt"
movie_genres = ["action", "comedy", "horror", "drama"]
movies_dictionary = {}
import_movie_data(movies_file)

planet_hulk = Movie("Planet Hulk", "Will he save their world or destroy it? When the Hulk becomes too dangerous for the"
                                   " Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a "
                                   "planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet "
                                   "Sakaar where he is sold into slavery and trained as a gladiator",
                    movie_genres[0], 1.45)

similar_movie, similarity_score = find_similar(planet_hulk)

# output result
print(f"The closest movie to Planet Hulk is {similar_movie}, with a similarity of {similarity_score}")
