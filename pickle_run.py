import pickle
from main import get_recommendations

# Load the model (example)
with open('get_recommendations_model.pkl', 'rb') as f:
    loaded_get_recommendations = pickle.load(f)
    
# Use the loaded model  
result = loaded_get_recommendations("The Dark Knight")
print(result)