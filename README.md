# Weather and Vegetation Status Project

This is a simple Python project that retrieves the current temperature and humidity of a specified city using the [Weatherbit API](https://www.weatherbit.io/), then analyzes and displays:

- **Weather condition** based on temperature
- **Vegetation cover estimate** based on relative humidity
- A simple **line chart** of temperature and humidity over time

---

## Features

- Get city name from user input  
- Fetch current temperature and humidity using Weatherbit API  
- Analyze weather status (Hot / Moderate / Cold)  
- Estimate vegetation growth (Good / Moderate / Poor) based on humidity  
- Display temperature and humidity in a line chart using `matplotlib`

---

## Requirements

- Python 3.6 or above  
- Install required packages:  
```bash
pip install requests matplotlib
```

## How to Use

1. Clone or download the project  
2. Navigate to the project folder  
3. Get your free API key from [Weatherbit](https://www.weatherbit.io/)  
4. Replace the `api_key` variable in the script with your key  
5. Run the script:  
```bash
python your_script_name.py


