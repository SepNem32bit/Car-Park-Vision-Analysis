# Car-Park-Vision-Analysis

This project implements a car park detection system using OpenCV. It processes video footage of a car park to identify and monitor the occupancy of parking spaces in real-time. Additionally, a manual annotation script is provided to select parking spaces for training models.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Real-time Detection](#real-time-detection)
  - [Manual Annotation](#manual-annotation)
- [File Structure](#file-structure)
- [Notes](#notes)
- [License](#license)

## Features
- Real-time car park monitoring
- Detection of free and occupied parking spaces
- Visual indication with colored rectangles
- Display of free space count on the video feed
- Manual annotation tool to select parking spaces

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

Place your video file (carPark.mp4), the car park positions file (CarParkPosition), and the image file (carParkImg.png) in the Data/CarPark Detection directory

## Usage
### Real-time Detection
1. Run the detection script:
Ensure that your video file and positions file are correctly placed as described above. Execute the following command to start the car park detection:

```bash
python Project-CarParkAnalysis.py
```
2. View the results:
The script will open a window displaying the video feed with highlighted parking spaces. Free spaces will be marked in green, and occupied spaces will be marked in red. The number of free spaces will be shown on the video feed.

### Manual Annotation
1. Run the annotation script:
To manually annotate parking spaces, execute the following command:
```bash
python Project-CarParkPick.py
```
2. Annotate parking spaces:
Left-click on the image to add a rectangle representing a parking space.
Right-click inside an existing rectangle to remove it.
The positions will be saved automatically and can be used for training the detection model.

## File Structure
detect_park_spaces.py: Main script for detecting and visualizing parking spaces in the video.
annotate_park_spaces.py: Script for manually annotating parking spaces in an image.
requirements.txt: List of required Python packages.
Data/CarPark Detection/:
carPark.mp4: Sample video file of the car park.
CarParkPosition: Pickle file containing the positions of parking spaces (rectangles).
carParkImg.png: Image file used for manual annotation of parking spaces.
images/: (Optional) Directory for storing any additional images used in the project.

## Notes
File Paths: Ensure that the paths in the scripts for loading the video, image, and position files are correctly set according to your local environment.
Threshold Values: The threshold values used for determining free vs. occupied spaces in Project-CarParkAnalysis.py may need adjustment based on your specific video and parking space characteristics.
Manual Annotation: The manual annotation script (Project-CarParkPick.py) allows you to visually mark parking spaces on an image, which is useful for training and refining the detection model.
