# bouncing_balls
# SPY Stats - Bouncing Balls

A simple Python application that visualizes daily open-close price changes of the SPY ETF (S&P 500 index tracker) as bouncing balls, using [Pygame](https://www.pygame.org/news) for real-time animation. Each ball’s speed and color reflect the magnitude and direction (positive or negative) of the daily price change, and clicking on a ball displays its open-close spread.

---

## Features

- **Dynamic Visualization**  
  Each trading day’s data is translated into a ball whose speed is determined by the absolute percentage change in the SPY’s price.  
- **Color Coding**  
  Green balls represent a positive price change, while red balls represent a negative price change.  
- **Collision Detection**  
  Balls bounce off one another and the window boundaries in a physically plausible way.  
- **User Interaction**  
  - **Click** a ball to display the open-close spread for that specific day.  
  - Press **Space** to pause or unpause the animation.  
- **CSV Data Integration**  
  Reads data from a CSV file (e.g., `Download Data - FUND_US_ARCX_SPY (1).csv`), parsing dates, opens, and closes.

---

## Getting Started

### Prerequisites
- Python 3.x  
- [Pygame](https://www.pygame.org/wiki/GettingStarted)

Install Pygame via pip:
```bash
pip install pygame
