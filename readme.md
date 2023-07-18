# Movie Recommendation Code Summary

The provided code snippet performs movie recommendation based on movie metadata using the TMDB Movie Metadata dataset from Kaggle.

## Functionality Overview
1. Libraries and Dependencies
2. Data Loading and Preprocessing
3. TF-IDF Vectorization
4. Cosine Similarity
5. Movie Recommendations
6. Data Parsing and Cleaning
7. Feature Extraction
8. Data Cleaning and Transformation
9. Feature Combination
10. CountVectorizer and Cosine Similarity
11. Movie Recommendation and Indexing
12. Final Recommendation

## Code Snippet
[Code Snippet Link](https://github.com/Kool-Cool/Kool-Cool-Movie-Recommendations-Flask)

## Explanation

The provided code snippet includes several steps to perform movie recommendation. Here's a brief explanation of each step:

1. Libraries and Dependencies: The required libraries such as pandas, numpy, sklearn, and pickle are imported.
2. Data Loading and Preprocessing: Two CSV files, 'tmdb_5000_credits.csv' and 'tmdb_5000_movies.csv', are read into DataFrames df1 and df2, respectively. The columns of df1 are renamed, and then it is merged with df2 based on the 'id' column.
3. TF-IDF Vectorization: The TfidfVectorizer from scikit-learn is used to create a TF-IDF vectorizer object named tfidf. Any missing values (NaN) in the 'overview' column of df2 are replaced with an empty string. Then, the TF-IDF matrix is constructed by fitting and transforming the 'overview' data using tfidf.
4. Cosine Similarity: The cosine similarity matrix is computed using the linear_kernel function from sklearn.metrics.pairwise. This matrix represents the similarity between movies based on their textual descriptions (TF-IDF representation).
5. Movie Recommendations: The get_recommendations function is defined, which takes a movie title as input and returns the top 10 most similar movies based on cosine similarity scores. It uses the cosine similarity matrix and a reverse map of movie titles and indices to find the index of the input movie and retrieve the most similar movies.
6. Data Parsing and Cleaning: The literal_eval function from the ast module is applied to parse stringified features ('cast', 'crew', 'keywords', 'genres') into their corresponding Python objects.
7. Feature Extraction: Functions are defined to extract useful information from the parsed features. For example, the get_director function retrieves the director's name from the 'crew' feature, and the get_list function returns a list of the top three elements from a given feature.
8. Data Cleaning and Transformation: The clean_data function is applied to lowercase all strings and remove spaces from names in the 'cast', 'keywords', 'director', and 'genres' features.
9. Feature Combination: A new feature named 'soup' is created by combining the cleaned 'keywords', 'cast', 'director', and 'genres' features into a single string, separated by spaces. This step helps to capture more relevant information for similarity computation.
10. CountVectorizer and Cosine Similarity: The CountVectorizer from sklearn.feature_extraction.text is imported, and a count matrix is created by fitting and transforming the 'soup' data. The cosine similarity matrix is computed based on the count matrix, representing the similarity between movies using the count-based approach.
11. Movie Recommendation and Indexing: The main DataFrame is reset with a new index, and a reverse mapping of movie titles and indices is constructed. This mapping is used to retrieve the index of the input movie in the recommendation function.
12. Final Recommendation: The get_recommendations function is called with a specific movie title, and it returns the top 10 most similar movies based on either TF-IDF or count-based cosine similarity, depending on the cosine similarity matrix used.

