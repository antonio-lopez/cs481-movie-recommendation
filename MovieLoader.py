import os
import csv
import sys

from surprise import Dataset
from surprise import Reader

class MovieLoader:

    filmIDtoName = {}
    nameToFilmID = {}
    pathOfRatings = './ml-latest-small/ratings.csv'
    pathOfFilms = './ml-latest-small/movies.csv'
    
    def mLDataLoad(self):

        # Look for files relative to the directory we are running from
        os.chdir(os.path.dirname(sys.argv[0]))

        ratingsDS = 0
        self.filmIDtoName = {}
        self.nameToFilmID = {}

        reader = Reader(line_format='user item rating timestamp', sep=',', skip_lines=1)

        ratingsDS = Dataset.load_from_file(self.pathOfRatings, reader=reader)

        with open(self.pathOfFilms, newline='', encoding='ISO-8859-1') as sourceFile:
                filmReader = csv.reader(sourceFile)
                next(filmReader)  #Skip header line
                for row in filmReader:
                    filmID = int(row[0])
                    movieName = row[1]
                    self.filmIDtoName[filmID] = movieName
                    self.nameToFilmID[movieName] = filmID

        return ratingsDS

    def loadClientRatings(self, client):
        clientRatings = []
        hitClient = False
        with open(self.pathOfRatings, newline='') as sourceFile:
            ratingReader = csv.reader(sourceFile)
            next(ratingReader)
            for row in ratingReader:
                clientID = int(row[0])
                if (client == clientID):
                    filmID = int(row[1])
                    rating = float(row[2])
                    clientRatings.append((filmID, rating))
                    hitClient = True
                if (hitClient and (client != clientID)):
                    break

        return clientRatings
    
    def getNameOfFilm(self, filmID):
        if filmID in self.filmIDtoName:
            return self.filmIDtoName[filmID]
        else:
            return ""
        
    def getIDOfFilm(self, filmName):
        if filmName in self.nameToFilmID:
            return self.nameToFilmID[filmName]
        else:
            return 0