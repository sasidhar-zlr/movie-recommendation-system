import pickle
import pandas as pd
from main import get_recommendations  # If needed by your pickled object
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the pickled function or model
with open('get_recommendations_model.pkl', 'rb') as f:
    loaded_get_recommendations = pickle.load(f)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    
    # Validate input
    if not data or 'title' not in data:
        return jsonify({"error": "No movie title provided."}), 400

    movie_title = data['title']

    try:
        # Call the unpickled recommendation function, which returns a DataFrame
        df = loaded_get_recommendations(movie_title)
        recommendations = df.to_dict()
        print(recommendations)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    # Return the data in JSON format
    return jsonify({"recommendations": recommendations})

if __name__ == '__main__':
    # Run in debug mode for development
    app.run(debug=True, host='0.0.0.0', port=5000)
