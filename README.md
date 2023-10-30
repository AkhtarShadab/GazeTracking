# Gaze Tracking with OpenCV and dlib

This project demonstrates gaze tracking using Python, OpenCV, and dlib. It allows you to track a person's gaze direction and record eye-related data.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Files](#files)

## Introduction

This project is designed to track a person's gaze and provides information such as blinking, gaze direction (left, right, center), and pupil coordinates. It also allows you to record and save gaze data.

## Features

- Gaze tracking using OpenCV and dlib.
- Blink detection.
- Gaze direction detection (left, right, center).
- Pupil coordinates tracking.
- Data recording to a CSV file.
- Calibration for binarization threshold value.

## Prerequisites

Before using this code, you need to have the following dependencies installed:

- Python (3.x recommended)
- OpenCV
- dlib
- numpy
- pandas

You can install the necessary dependencies using pip:

```sh
pip install opencv-python-headless dlib numpy pandas
```

## Usage

1. **Clone or Download:** Clone this repository or download the code to your local machine.

2. **Set Up Python Environment:** Create a Python environment and install the required dependencies as mentioned in the "Prerequisites" section.

3. **Select Video Input:** You can use the `video.mp4` file as the input video for gaze tracking, or replace it with your own video.

4. **Run Gaze Tracking:** Execute the `main.py` script to start the gaze tracking and data recording.

    ```bash
    python main.py
    ```

5. **View Gaze Tracking:** The program will display the video with gaze tracking results. To exit the program, press the 'Esc' key.

6. **Recorded Gaze Data:** The recorded gaze data will be saved to `media_2_data.csv` in the current directory.

## Files

- `main.py`: The main script for gaze tracking and data recording.
- `calibration.py`: Calibration class for determining the binarization threshold.
- `eye.py`: Eye class to create and analyze eye frames.
- `gaze_tracking.py`: GazeTracking class to track the user's gaze.
- `pupil.py`: Pupil class for iris detection and pupil position estimation.
