---
layout: post
title: "Moveit Hand-Eye Calibration Example"
abstract: "How to create a simulation with a realsense camera simulation and a custom gazebo world?"
thumbnail: '/images/hand_eye.jpg'
tags: [ ]
category: Robotic Manipulation
jquery: true
slideshow2: true
time: 15
words: 3619

---
## {{ page.title }}


## Pre-requisites

1. Install Moveit ROS package : https://ros-planning.github.io/moveit_tutorials/doc/getting_started/getting_started.html
2. Moveit installs ROS configuration for Franka Panda Roboty by Default to the same Catkin workspace (Panda Moveit Configuration). If you are using a different robot , you need to prepare the relevant robot configuration.
3. Install move it calibration package to the same catkin workspace and follow the steps: 


## Calibration step
1. launch franka ros control in terminal 1 

```
    $  cd ~/ws_moveit &&  source devel/setup.bash
    $  roslaunch panda_moveit_config franka_control.launch robot_ip:=130.230.36.115 load_gripper:=true use_rviz:=true
```
```
    $  roslaunch realsense2_camera rs_camera.launch align_depth:=True color_width:=1280 color_height:=720 color_fps:=30
```

Follow the steps in tutorial : https://ros-planning.github.io/moveit_tutorials/doc/hand_eye_calibration/hand_eye_calibration_tutorial.html .
Create the Aruco Marker and re-measure marker size and marker seperation and update the values. continue steps in the tutorial

remember to check markers are accurately detected in the RVIZ. if not move the robot so that it does! (see gifs)

at the end of the tutorial you will have a generated a launch file >> handeye_calibration.launch

Launch the calibration file in a new terminal

```
    $  cd ~/ws_moveit &&  source devel/setup.bash
    $  cd ~/ws_moveit/src/panda_moveit_config/launch/
    $  roslaunch handeye_calibration_23_March.launch    ## use the latest calibration
```

## tf2_tools for rescue
rostopic echo /tf_static does not publish camera transformations.
The link we need to get the extrinsic parameters of the camera is camera_color_optical_frame. other frames are incorrect. you can print the transformation with the help of tf2_tools 

to get the cam_2_world ( camera pose in world coordinates)

```
    $  cd ~/tf2_tools  &&  source devel/setup.bash
    $  rosrun tf2_tools echo2.py panda_link0 camera_color_optical_frame
```
to see the transformation open a new terminal and run
```
    $  rostopic echo /Cam_2_World
```