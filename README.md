# Car-Park-Vision-Analysis

This project implements a car park detection system using OpenCV. It processes video footage of a car park to identify and monitor the occupancy of parking spaces in real-time. The system highlights empty and occupied parking spaces with different colors and displays the count of free spaces.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Notes](#notes)
- [License](#license)

## Features
- Real-time car park monitoring
- Detection of free and occupied parking spaces
- Visual indication with colored rectangles
- Display of free space count on the video feed

## Installation

### Prerequisites

Ensure you have Python 3.x installed on your system. You also need to install the required Python libraries.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/SepNem32bit/car-park-detection.git
   cd car-park-detection
   ```

2. **Set up a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

3. **Install the required packages:**

```bash
pip install -r requirements.txt
```
4. **Download the dataset and model files:**

Place your video file (carPark.mp4) and the car park positions file (CarParkPosition) in the Data/CarPark Detection directory.
