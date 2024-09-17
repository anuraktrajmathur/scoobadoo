# Lab2024

## Project Info
- [Python 3.11.2](https://www.python.org/downloads/release/python-3112/)
- [Poetry](https://python-poetry.org/ ) as packages manager

## Folder Structure
- config
   - configuration.yml
- frank_manager
  - threads...
- sensors_actuators
  - classes....
- utils
- main

## Usage
### Install poetry and dependeces
```
sudo apt install -y python3-poetry build-essential libcap-dev libatlas-base-dev ffmpeg libopenjp2-7 libcamera-dev libkms++-dev libfmt-dev libdrm-dev libjpeg-dev libtiff5-dev  cmake git pkg-config libtiff-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libgtk-3-dev gfortran python3-dev qt5-qmake qtbase5-dev qtbase5-dev-tools qttools5-dev-tools libhdf5-103  
```

### Copy library for picamera2 in python library folder
```
sudo cp -r /usr/lib/python3/dist-packages/libcamera /usr/lib/python3.11   
sudo cp -r /usr/lib/python3/dist-packages/pykms /usr/lib/python3.11   
```

### Create - activate virtual environment and install library 
```
mkdir frank  
cd ./frank  
python -m venv frank_venv  
source frank_venv/bin/activate  
poetry install   
```
### Downgrade numpy library 
```
pip uninstall numpy  
pip install numpy==1.24.2  
```
### Check if venv is activated and after run main
```
python ./main.py
```


# Library

This first version of the AS3 submarine will be equipped with 2 DC brushless motors managed by the Engine class, an ultrasonic proximity sensor positioned on the bottom of the submarine to measure the distance from the seabed and managed by the Proximity class, and finally, a Raspberry Pi camera managed within the Camera class.


## `Engine` Class

### Overview

The `Engine` class is designed to manage the operations of two engines (left and right). It allows starting and stopping of the engines with a specified power percentage.

### Methods

- ### `start_left(power_percentage: int)`
  Starts the left engine with a specified power percentage in the range [-100, +100].
  
  - **Parameters:**
    - `power_percentage` (int): The power percentage to apply to the left engine.

- ### `start_right(power_percentage: int)`
  Starts the right engine with a specified power percentage in the range [-100, +100].
  
  - **Parameters:**
    - `power_percentage` (int): The power percentage to apply to the right engine.

- ### `stop_left()`
  Stops the left engine.

- ### `stop_right()`
  Stops the right engine.

## `Proximity` Class

### Overview

The `Proximity` class is designed to interact with proximity sensors, specifically retrieving distance measurements from the bottom sensor. This class initializes the sensor and provides a method to obtain the latest distance data.

### Methods

- ### `get_btm_distance()`
  Retrieves the latest distance measurement from the bottom proximity sensor.
  - **Returns:**
    - The most recent distance value from the ground



## `Camera` Class

What do you want to read here? It's the class you need to develop  (⌐■_■)