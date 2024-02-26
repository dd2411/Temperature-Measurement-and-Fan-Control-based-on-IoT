# Temperature Measurement and Fan Control based on IoT

This project implements an IoT solution to measure temperature using a DHT11 sensor and control a fan based on the temperature readings. It utilizes Arduino, Raspberry Pi, an LCD display, and a fan.

## Components
- DHT11 sensor
- Arduino Uno
- Raspberry Pi-3
- LED Display
- Fan

## Setup and Usage
1. **Hardware Setup:**
   - Connect the DHT11 sensor to the Arduino board.
   - Connect the LCD to the Arduino board.
   - Connect the fan to the Arduino board.
   - Ensure proper connections with the Raspberry Pi for IoT functionalities.

2. **Software Setup:**
   - Install the necessary libraries for the DHT11 sensor and the LCD.
   - Upload the provided Arduino code to the Arduino board.

3. **Operation:**
   - Upon setup, the system initializes and displays a welcome message on the LCD.
   - The DHT11 sensor continuously measures the temperature.
   - The Arduino board adjusts the fan speed based on the temperature readings using PWM.
   - The temperature readings along with the fan speed are displayed on the LCD.

## Code Explanation

1. Libraries
   
DHT.h and DHT_U.h: These libraries are used for interfacing with the DHT temperature and humidity sensor.
LiquidCrystal.h: This library allows communication with LCDs.

2. Global Variables and Definitions:

DHTTYPE: Specifies the type of DHT sensor being used (DHT11 in this case).
dht_dpin: Specifies the digital pin to which the DHT sensor is connected.
PWM: Specifies the PWM pin connected to control the fan speed.
degree[]: Defines a custom character representing the degree symbol for the LCD.

3. Setup Function:

Initializes the LCD, creates the custom character for the degree symbol, and prints some welcome messages.
Initializes the DHT sensor.

4. Loop Function:

Reads the temperature from the DHT sensor.
-Prints the temperature on the LCD along with the degree symbol.
-Adjusts the fan speed based on the temperature:
-The fan is turned off if the temperature is less than 26°C.
-Fan speed is adjusted in steps based on temperature increments.
-If the temperature exceeds 29°C, the fan runs at full speed.
-Delays for 3 seconds before repeating the loop.
