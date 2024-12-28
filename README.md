# bouncing_balls
SPY Stats - Bouncing Balls
A simple Python application that visualizes daily open-close price changes of the SPY ETF (S&P 500 index tracker) as bouncing balls, using Pygame for real-time animation. Each ball’s speed and color reflect the magnitude and direction (positive or negative) of the daily price change, and clicking on a ball displays its open-close spread.

Features
Dynamic Visualization:
Each trading day’s data is translated into a ball whose speed is determined by the absolute percentage change in the SPY’s price.
Color Coding:
Green balls represent a positive price change, while red balls represent a negative price change.
Collision Detection:
Balls bounce off one another and the window boundaries in a physically plausible way.
User Interaction:
Click a ball to display the open-close spread for that specific day.
Press Space to pause or unpause the animation.
CSV Data Integration:
Reads data from a CSV file (e.g., Download Data - FUND_US_ARCX_SPY (1).csv), parsing dates, opens, and closes.
Getting Started
Prerequisites
Python 3.x
Pygame library
Install via pip:
bash
Copy code
pip install pygame
Installation
Clone or Download this repository (or copy the script into a local .py file).
Place the CSV Data file (Download Data - FUND_US_ARCX_SPY (1).csv) in the same directory as the Python script.
Run the Script:
bash
Copy code
python bouncing_balls.py
Usage
Start the Application:
The Pygame window opens with a black background. Sixty balls (or as many as there are rows of data up to 60) begin bouncing around.
Click a Ball:
When you click on a ball, the program displays its date and open-close spread in the bottom-left corner of the window.
Click elsewhere to deselect the ball.
Pause and Resume:
Press the Space bar to pause the animation (the balls will stop moving).
Press Space again to resume.
Code Breakdown
Imports & Initialization

Imports pygame, random, csv, and other standard libraries.
Reads SPY data from the CSV file and sets up the display window.
Data Processing

Parses the CSV rows to calculate each day’s open-close difference and percentage change.
Determines maximum and minimum absolute percentage change to set ball speeds proportionally.
Ball Creation

Creates Ball objects with attributes for position, size, color, speed, date, open, and close prices.
Assigns each day’s data to a ball and randomizes its initial position.
Animation Loop

Checks for user events (close window, mouse clicks, spacebar for pause).
Moves and draws balls on the screen, handles collisions between them, and displays a spread message if a ball is selected.
Collision Handling

Balls respond to collisions with each other and with the window boundaries via basic physics calculations.
CSV File Format
The script expects a CSV file with the following headers:

Date (in the format MM/DD/YYYY)
Open (the opening price)
Close (the closing price)
Example:

csv
Copy code
Date,Open,High,Low,Close,Volume
08/25/2023,440.23,445.00,439.59,444.59,102345678
08/24/2023,435.98,441.50,435.52,440.23,123456789
...
(The script only uses Date, Open, and Close columns.)

Contributing
If you want to improve or extend this script (e.g., adding new visual elements or different data sources), feel free to submit pull requests or open issues.

License
This project is provided as-is for educational or personal use. Check the repository or consult the owner for any specific licensing terms.

Enjoy exploring SPY’s daily price changes through an interactive, animated lens!