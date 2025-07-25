Weather and Vegetation Status Project
This is a simple Python project that retrieves the current temperature and humidity of a specified city using the Weatherbit API, then analyzes and displays:

Weather condition based on temperature

Vegetation cover estimate based on relative humidity

A simple line chart of temperature and humidity over time

Features
Get city name from user input

Fetch current temperature and humidity using Weatherbit API

Analyze weather status (Hot / Moderate / Cold)

Estimate vegetation growth (Good / Moderate / Poor) based on humidity

Display temperature and humidity in a line chart using matplotlib

Requirements
Python 3.6 or above

Install required packages:

bash
Copy code
pip install requests matplotlib
How to Use
Clone or download the project

Navigate to the project folder

Get your free API key from Weatherbit

Replace the api_key variable in the script with your key

Run the script:

bash
Copy code
python your_script_name.py
Enter the desired city name when prompted

The script will display weather and vegetation status and show a plot

Notes
This script is intended for educational and demonstration purposes.

The vegetation estimation is simplified and based only on relative humidity.

For real-world applications, consider using specialized vegetation or NDVI data sources.

License
This project is licensed under the MIT License.
