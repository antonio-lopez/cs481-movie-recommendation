from MovieLoader import MovieLoader
from surprise import SVD
from surprise import accuracy

# produce a test data set of all the movies that the user did not rate already
def UserAntiTestData(selectedUser, trainset):
    fill = trainset.global_mean

    anti_testset = []
    
    u = trainset.to_inner_uid(str(selectedUser))
    
    user_items = set([j for (j, _) in trainset.ur[u]])
    anti_testset += [(trainset.to_raw_uid(u), trainset.to_raw_iid(i), fill) for
                             i in trainset.all_items() if
                             i not in user_items]
    return anti_testset

selectedUser = 672

movieLoad = MovieLoader()

# load movie data
movies = movieLoad.mLDataLoad()

# Get user ratings and append to a seperate list
ratings = movieLoad.getUserRatings(selectedUser)
userLike = []
userDislike = []
for movieRating in ratings:
    if (float(movieRating[1]) > 4.0):
        userLike.append(movieRating)
    if (float(movieRating[1]) < 3.0):
        userDislike.append(movieRating)

print("\nThese are the movies that user ", selectedUser, " liked:")
for movieRating in userLike:
    print(movieLoad.getMovieName(movieRating[0]))
print("\nThese are the movies that the user didn't like:")
for movieRating in userDislike:
    print(movieLoad.getMovieName(movieRating[0]))

print("\nBuilding recommendation algorithm...")
trainSet = movies.build_full_trainset()
recommendAlgo = SVD()
recommendAlgo.fit(trainSet) 
testData = UserAntiTestData(selectedUser, trainSet)
recommend = recommendAlgo.test(testData)

# difference between the predicted rating and the actual rating
accuracy.mae(recommend, verbose=True)
accuracy.rmse(recommend, verbose=True)

movieRecommends = []

print ("\nThese are the recommended movies for the user:")
for userID, movieID, actualRating, estimatedRating, _ in recommend:
    intMovieID = int(movieID)
    movieRecommends.append((intMovieID, estimatedRating))

for recommendations in movieRecommends[:20]:
    print(movieLoad.getMovieName(recommendations[0]))


