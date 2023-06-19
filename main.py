import requests
from datetime import datetime
from dotenv import dotenv_values

# Load environment variables from .env file
env_vars = dotenv_values('.env')

# Set the required environment variables
APP_ID = env_vars['EXERCISE_APP_ID']
API_KEY = env_vars['EXERCISE_API_KEY']
EXERCISE_ENDPOINT = env_vars["EXERCISE_ENDPOINT"]
SHEETY_ENDPOINT = env_vars["SHEETY_ENDPOINT"]
SHEETY_API = env_vars["SHEETY_API"]

# Get the current date and time
now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Get exercise input from user
exercise_input = input("What exercise did you do today: ")

# Make a request to the exercise endpoint
exercise_parameters = {
    "query": exercise_input
}
exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
response = requests.post(EXERCISE_ENDPOINT, exercise_parameters, headers=exercise_headers).json()

# Extract exercise details from the response
exercises = []
durations = []
calories = []
for exercise in response["exercises"]:
    exercises.append(exercise["user_input"])
    durations.append(exercise["duration_min"])
    calories.append(exercise["nf_calories"])

# Prepare data for Sheety API
sheety_parameters = {
    "workout": {
        "date": now.split()[0].title(),
        "time": now.split()[1].title(),
        "exercise": exercises[0].title(),
        "duration": durations[0],
        "calories": calories[0]
    }
}
headers = {
    'Authorization': f'Bearer {SHEETY_API}',
    'Content-Type': 'application/json'
}

# Make a POST request to Sheety API to add the workout data
data_post = requests.post(url=SHEETY_ENDPOINT, json=sheety_parameters, headers=headers)

# Check the response status
if data_post.status_code == 200:
    print('Workout data added successfully!')
else:
    print('Error:', data_post.text)

# Print exercise details for testing
print(response, exercises, durations, calories)
