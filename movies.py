from csv import reader


def explore_data(dataset, start, end, rows_and_columns=False):
    for i in range(start,end):
        print(dataset[i])
    if(rows_and_columns):
        print(len(dataset))    
    """Explore the elements of a list.
    
    Print the elements of a list starting from the index 'start'(included) upto the index 'end'         (excluded).
    
    Keyword arguments:
    dataset -- list of which we want to see the elements
    start -- index of the first element we want to see, this is included
    end -- index of the stopping element, this is excluded 
    rows_and_columns -- this parameter is optional while calling the function. It takes binary          values, either True or False. If true, print the dimension of the list, else dont.
    """
    
    
        
     


def duplicate_and_unique_movies1(dataset, index_):
    count = 0
    for i in range(len(dataset)):
        if dataset[i][-2] == index_:
            count+=1
            # print(dataset[i])
    return count
def duplicate_and_unique_movies(dataset, index_):
    count = 1
    for i in range(len(dataset)):
        if dataset[i][-2] == index_:
            count+=1
            print(dataset[i])
    return count            
    """Check the duplicate and unique entries.
    
    We have nested list. This function checks if the rows in the list is unique or duplicated based     on the element at index 'index_'.
    It prints the Number of duplicate entries, along with some examples of duplicated entry.
    
    Keyword arguments:
    dataset -- two dimensional list which we want to explore
    index_ -- column index at which the element in each row would be checked for duplicacy 
    
    """
    
    


def movies_lang(dataset, index_, lang_):
    movies_ = []
    for i in range(len(dataset)):
        if dataset[i][index_] == lang_:
            movies_.append(dataset[i])
    explore_data(movies_,0,5)
    """Extract the movies of a particular language.
    
    Of all the movies available in all languages, this function extracts all the movies in a                  particular laguage.
    Once you ahve extracted the movies, call the explore_data() to print first few rows.

    Keyword arguments:
    dataset -- list containing the details of the movie
    index_ -- index which is to be compared for langauges
    lang_ -- desired language for which we want to filter out the movies
    
    Returns:
    movies_ -- list with details of the movies in selected language
    """
    return movies_
    



def rate_bucket(dataset, rate_low, rate_high):
    rated_movies =[]
    for i in range(len(dataset)):
        if float(dataset[i][-4]) >= rate_low and float(dataset[i][-4]) <= rate_high:
            rated_movies.append(dataset[i]) 
              
    """Extract the movies within the specified ratings.
    
    This function extracts all the movies that has rating between rate_low and high_rate.
    Once you ahve extracted the movies, call the explore_data() to print first few rows.
    
    Keyword arguments:
    dataset -- list containing the details of the movie
    rate_low -- lower range of rating
    rate_high -- higher range of rating
    
    Returns:
    rated_movies -- list of the details of the movies with required ratings
    """

    explore_data(rated_movies,0,5)
    return rated_movies




# Read the data file and store it as a list 'movies'
opened_file = open(path, encoding="utf8")
read_file = reader(opened_file)
movies = list(read_file)
# print(movies)


# The first row is header. Extract and store it in 'movies_header'.
movies_header = []
movies_header = movies[0]
# print(movies_header)

# Subset the movies dataset such that the header is removed from the list and store it back in movies
# print(len(movies))
del movies[0]
# print(movies)


# Delete wrong data
# print(movies[4552])
# print('='*50)
del movies[4553]

# Explore the row #4553. You will see that as apart from the id, description, status and title, no other information is available.
# Hence drop this row.



# Using explore_data() with appropriate parameters, view the details of the first 5 movies.

# print(movies_header)
# explore_data(movies,0,5)

# Our dataset might have more than one entry for a movie. Call duplicate_and_unique_movies() with index of the name to check the same.
    
# li = [duplicate_and_unique_movies1(movies,movies[i][-2]) for i in range(len(movies))]

# c = 0
# for i in range(len(li)):
#     if li[i]>1:
#         c = duplicate_and_unique_movies(movies,movies[i][-2])
#         print(c)
# for i in range(len(li)):
#     if li[i]>1:
#         print(i,li[i])

# We saw that there are 3 movies for which the there are multiple entries. 
# Create a dictionary, 'reviews_max' that will have the name of the movie as key, and the maximum number of reviews as values.

reviews_max = {}
for i in range(len(movies)):
    reviews_max[movies[i][-2]] = movies[i][-3]
# print(reviews_max)    
# Create a list 'movies_clean', which will filter out the duplicate movies and contain the rows with maximum number of reviews for duplicate movies, as stored in 'review_max'. 
movies_clean = []
movies_name = []
for i in range(len(movies)):
    if movies[i][-2] not in movies_name:
        if duplicate_and_unique_movies1(movies,movies[i][-2]) == 1:
            movies_clean.append(movies[i])
            movies_name.append(movies[i][-2])
        else:
            lis = []
            for j,jj in reviews_max.items():
                if j == movies[i][-2]:
                    lis.append(jj)
            ma = max(lis)
            movies[i][-3] = ma
            movies_clean.append(movies[i])   
            movies_name.append(movies[i][-2])     






# Calling movies_lang(), extract all the english movies and store it in movies_en.

movies_en = movies_lang(movies_clean,3,'en')
# print(len(movies_en)) 
# count = 0
# for i in range(len(movies_en)):
#     if float(movies_en[i][-4])>8:
#         print(movies_en[i][-2],movies_en[i][-4],movies_en[i][3])
   
high_rated_movies = []
high_rated_movies = rate_bucket(movies_en,8,10)
# print(len(high_rated_movies))
# print(len(high_rated_movies),high_rated_movies[0],high_rated_movies[1])
# explore_data(high_rated_movies,0,5)
# Call the rate_bucket function to see the movies with rating higher than 8.
