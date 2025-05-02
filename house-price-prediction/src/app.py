from flask import Flask, request, jsonify, render_template_string
import pickle
from pathlib import Path

app = Flask(__name__)

# Load model
model_path = Path(__file__).parent.parent / "models" / "model.pkl"
model = pickle.load(open(model_path, "rb"))

# HTML Form Template
HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>House Price Predictor</title>
    <style>
        body { font-family: Arial; max-width: 500px; margin: auto; padding: 20px }
        input { width: 100%; padding: 8px; margin: 5px 0 }
        button { background: #4CAF50; color: white; padding: 10px; border: none; width: 100% }
    </style>
</head>
<body>
    <h1>🏠 House Price Prediction</h1>
    <form method="POST" action="/">
        <label>Median Income:</label>
        <input type="number" step="0.1" name="income" value="3.0" required>
        
        <label>House Age:</label>
        <input type="number" name="age" value="25" required>
        
        <label>Rooms per House:</label>
        <input type="number" step="0.1" name="rooms_per_house" value="5" required>
        
        <button type="submit">Predict Price</button>
    </form>
    {% if prediction %}
    <h2>Result: €{{ prediction }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            # Get form data
            income = float(request.form['income'])
            age = float(request.form['age'])
            rooms = float(request.form['rooms_per_house'])
            
            # Make prediction
            predicted_price = model.predict([[income, age, rooms]])[0]
            return render_template_string(HTML_FORM, prediction=round(predicted_price, 0))
            
        except Exception as e:
            return render_template_string(HTML_FORM, prediction=f"Error: {str(e)}")
    
    return render_template_string(HTML_FORM)

if __name__ == '__main__':
    app.run(debug=True, port=5000)