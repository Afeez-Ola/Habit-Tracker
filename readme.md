# Exercise Tracker

Exercise Tracker is a Python script that allows users to track their daily exercises and store the data in a Google Sheets spreadsheet using the Sheety API. It utilizes the nutritionix API to fetch exercise details based on user input.

## Features

- Fetches exercise details from the nutritionix API based on user input
- Stores exercise data including date, time, exercise name, duration, and calories burned in a Google Sheets spreadsheet
- Uses the `python-dotenv` package to load environment variables from an `.env` file
- Provides error handling for API requests and response statuses

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed on your machine
- A valid API key for the nutritionix API
- A Google Sheets spreadsheet with the Sheety API set up for writing data

## Installation

1. Clone this repository to your local machine or download the script file.

2. Install the required Python packages by running the following command:

3. Create an `.env` file in the same directory as the script and add the following variables:

    EXERCISE_APP_ID=<your-nutritionix-app-id>
    EXERCISE_API_KEY=<your-nutritionix-api-key>
    EXERCISE_ENDPOINT=<nutritionix-exercise-endpoint>
    SHEETY_ENDPOINT=<sheety-api-endpoint>
    SHEETY_API=<your-sheety-api-key>
    
    Replace the placeholder values with your actual API keys and endpoints.
4. Run the script using the following command:
    python main.py


## Usage

1. When prompted, enter the exercise you did today.

2. The script will fetch exercise details from the nutritionix API and display them.

3. The exercise data will be stored in the Google Sheets spreadsheet using the Sheety API.

4. Check the console output for confirmation and any errors encountered during the process.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify and adapt the code according to your needs.

Remember to replace the placeholders <your-nutritionix-app-id>, <your-nutritionix-api-key>, <nutritionix-exercise-endpoint>, <sheety-api-endpoint>, and <your-sheety-api-key> with the actual values from your environment.