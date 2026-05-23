from flask import Response
import requests
from datetime import datetime
from flask import Flask, render_template, request, redirect, session
import sqlite3
import joblib
import numpy as np

# Create Flask app
app = Flask(__name__)
app.secret_key = "crop_secret_key"
API_KEY = "c52c11def9b7f89acc0995fbb5c64901"

# Load trained model
model = joblib.load('model/crop_model.pkl')

# Home page
@app.route('/')
def home():
    if 'username' not in session:
           return redirect('/login')
    return render_template(
    'index.html',
    username=session['username']
    )

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    print("Prediction route working")
    city = request.form['city']
    api_temperature = "Not Available"
    api_humidity = "Not Available"
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        weather_data = response.json()
        if 'main' in weather_data:
            api_temperature = weather_data['main']['temp']
            api_humidity = weather_data['main']['humidity']
        else:
            api_temperature = "Not Available"
            api_humidity = "Not Available"
    except:
        pass

    if api_temperature == "Not Available":
            temperature = 25
    else:
            temperature = float(api_temperature)
    if api_humidity == "Not Available":
        humidity = 50
    else:
        humidity =float(api_humidity)

    # Get values from form
    N = float(request.form['N'])
    P = float(request.form['P'])
    K = float(request.form['K'])
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    ph = float(request.form['ph'])
    rainfall = float(request.form['rainfall']) 

    # Prepare data for prediction
    data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

    # Predict crop
    print("Prediction route started")
    prediction = model.predict(data)
    crop = prediction[0]

    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    current_date = datetime.now().strftime("%d-%m-%Y %H:%M")
    cursor.execute(
       "INSERT INTO predictions (username, crop, date) VALUES (?, ?, ?)",
        (session['username'], crop, current_date)
    )
    connection.commit()
    connection.close()

   # Sustainability suggestions
    bio_fertilizer = ""
    bio_predator = ""
    crop_rotation = ""
    sustainability_tip = ""
    sustainability_score= ""
    sustainability_level= ""
    crop_image = ""

    if crop == "rice":
        bio_fertilizer = "Blue Green Algae"
        bio_predator = "Neem Oil Spray"
        crop_rotation = "Pulses"
        sustainability_tip = "Use water conservation techniques"
        sustainability_score = "87"
        sustainability_level = "🟢 Excellent"
        crop_image = "rice.jpg"

    elif crop == "maize":
       bio_fertilizer = "Azotobacter"
       bio_predator = "Trichogramma"
       crop_rotation = "Groundnut"
       sustainability_tip = "Practice crop rotation regularly"
       sustainability_score= "82" 
       sustainability_level = "🟡 Moderate"
       crop_image = "maize.jpg"

    elif crop == "wheat":
        bio_fertilizer = "Azotobacter"
        bio_predator = "Neem Oil Spray"
        crop_rotation = "Legumes"
        sustainability_tip = "Use balanced nitrogen fertilization"
        sustainability_score = "82"
        sustainability_level = "🟢 Excellent"
        crop_image = "wheat.jpg"

    elif crop == "cotton":
        bio_fertilizer = "Azospirillum"
        bio_predator = "Trichogramma"
        crop_rotation = "Groundnut"
        sustainability_tip = "Use drip irrigation to conserve water"
        sustainability_score = "78"
        sustainability_level = "🟡 Moderate"
        crop_image = "cotton.jpg"

    elif crop == "sugarcane":
        bio_fertilizer = "Phosphate Solubilizing Bacteria"
        biopredator = "Neem Cake"
        crop_rotation = "Pulses"
        sustainability_tip = "Maintain proper soil moisture"
        sustainability_score = "84"
        sustainability_level = "🟢 Excellent"
        crop_image = "sugarcane.jpg"

    elif crop == "millet":
        bio_fertilizer = "Azospirillum"
        bio_predator = "Neem Extract"
        crop_rotation = "Pulses"
        sustainability_tip = "Millets require less water and improve sustainability"
        sustainability_score = "90"
        sustainability_level = "🟢 Excellent"
        crop_image = "millet.jpg"

    elif crop == "barley":
        bio_fertilizer = "Azotobacter"
        bio_predator = "Neem Oil"
        crop_rotation = "Beans"
        sustainability_tip = "Use organic compost for better soil fertility"
        sustainability_score = "80"
        sustainability_level = "🟢 Excellent"
        crop_image = "barley.jpg"

    elif crop == "jute":
        bio_fertilizer = "Vermicompost"
        bio_predator = "Trichoderma"
        crop_rotation = "Rice"
        sustainability_tip = "Maintain good drainage during cultivation"
        sustainability_score = "76"
        sustainability_level = "🟡 Moderate"
        crop_image = "jute.jpg"

    elif crop == "pulses":
        bio_fertilizer = "Rhizobium"
        bio_predator = "Neem Seed Kernel Extract"
        crop_rotation = "Wheat"
        sustainability_tip = "Pulses naturally improve soil nitrogen"
        sustainability_score = "92"
        sustainability_level = "🟢 Excellent"
        crop_image = "pulses.jpg"

    elif crop == "coconut":
        bio_fertilizer = "Mycorrhiza"
        bio_predator = "Neem Oil Trap"
        crop_rotation = "Banana"
        sustainability_tip = "Use organic mulching to retain soil moisture"
        sustainability_score = "81"
        sustainability_level = "🟢 Excellent"
        crop_image = "coconut.jpg"

    session['crop'] = crop
    session['api_temperature'] = api_temperature
    session['api_humidity'] = api_humidity
    session['bio_fertilizer'] = bio_fertilizer
    session['bio_predator'] = bio_predator
    session['crop_rotation'] = crop_rotation
    session['sustainability_tip'] = sustainability_tip
    session['sustainability_score'] = sustainability_score

    sustainability_score = int(str(sustainability_score).replace("%", ""))

    # Send result to HTML page
    return render_template(  
    'result.html',
    prediction=crop,
    bio_fertilizer=bio_fertilizer,
    bio_predator=bio_predator,
    crop_rotation=crop_rotation,
    sustainability_tip=sustainability_tip,
    sustainability_score=sustainability_score,
    crop_image=crop_image,
    sustainability_level=sustainability_level,
    api_temperature=api_temperature,
    api_humidity=api_humidity
)

@app.route('/register', methods=['GET', 'POST'])

def register():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        connection = sqlite3.connect('users.db')

        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )

        connection.commit()

        connection.close()

        return redirect('/login')

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])

def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        connection = sqlite3.connect('users.db')

        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()

        connection.close()

        if user:

            session['username'] = username

            return redirect('/')

        else:
            return "Invalid Username or Password"

    return render_template('login.html')
@app.route('/logout')

def logout():

    session.pop('username', None)

    return redirect('/login')

@app.route('/history')

def history():

    if 'username' not in session:
        return redirect('/login')

    connection = sqlite3.connect('users.db')

    cursor = connection.cursor()

    cursor.execute(
        "SELECT username, crop, date FROM predictions WHERE username=?",
        (session['username'],)
    )

    data = cursor.fetchall()

    connection.close()

    return render_template(
        'history.html',
        history=data
    )

@app.route('/download_report')

def download_report():

    report = f"""
Crop Recommendation Report

Predicted Crop: {session.get('crop')}

Temperature: {session.get('api_temperature')} °C

Humidity: {session.get('api_humidity')} %

Bio Fertilizer: {session.get('bio_fertilizer')}

Bio Predator: {session.get('bio_predator')}

Crop Rotation: {session.get('crop_rotation')}

Sustainability Tip: {session.get('sustainability_tip')}

Sustainability Score: {session.get('sustainability_score')}
"""

    return Response(
        report,
        mimetype="text/plain",
        headers={
            "Content-Disposition":
            "attachment;filename=crop_report.txt"
        }
    )

# Run app
if __name__ == '__main__':
    app.run(debug=True)