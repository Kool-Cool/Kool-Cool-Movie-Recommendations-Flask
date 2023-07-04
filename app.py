from flask import Flask , render_template , request 
from model import get_recommendations ,cosine_sim2 ,df2

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html" , movie_title = df2["title"])
    

@app.route('/recommendations', methods=['POST'])
def recommendations():
    # Get the movie title entered by the user
    title = request.form['title']

    # Get the recommendations using the get_recommendations function
    recommended_movies = get_recommendations(title, cosine_sim2)

    # Pass the recommendations to the template for displaying
    return render_template('recommendations.html', title=title, recommendations=recommended_movies)



@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/connect")
def connect():
    return render_template("connect.html")



if __name__ == "__main__":
  app.run(debug=True)