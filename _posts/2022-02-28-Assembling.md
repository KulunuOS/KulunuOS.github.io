---
layout: post
title: "Assembling things with robots"
abstract: "How to create a simulation with a realsense camera simulation and a custom gazebo world?"
thumbnail: '/images/assembly.jpg'
tags: [ ]
category: <span id="hashtag">#Assembly</span>  <span id="hashtag">#Perception</span>
jquery: true
slideshow2: true
time: 15
words: 3619

---
## {{ page.title }}

As a kid, you might have had toys that required you to put together and build up meaningful structures. Even though it seems a childish task, would you believe it is a complex problem for highly boasted robotic technology?
is a task that requires cognition. The cognition capabilities for the robots are enabled via concepts such as perception, motion planning and learning algorithms.

This article is organized in gthe following way :

1. Cognition for robotic manipulation
2. Assembling  as a manipulation task
3. State of the Art



### Cognition for robotic manipulation

Robotic Manipulation has advanced drastically in the recent times. Availability of higher D0F freedom robots, sensors, computing capabilities and algorithms. Cognition means the capability of the robotic setup to sense and analyze the environment and plan and execute acriopns tp o accomplish goals. such primary goals include grasping, inspecting, painting, welding, assembling etc. The task of robotic assembling is process that extends from grasping. 


### Assembling as a manipulation task

A manipulation task involves primary components such as a single or multiple robotic manipulators, a scene consisting of objects to be manipulated in their initial state and a goal state to be acheived. In certain cases, a human operator could also collaborate with a robot to perform the task.

In an assembly manipulation task, there could be either individual objects or partly assembled objects in the scene. Ideally the robotic manipulator should be a robotic arm with a suitable degrees of freedom and a gripper that is capable of grasping the objects. 

The feasibility of an assembly task depends on several constraints. The objects and final assembly must be within the workspace of the robot. The assembly task should be achievable within the task space of the robot. An assembly sequence must exist to rearrange the objects from their initial state to final state. Furthermore, the robot should be capable of following a motion plan to acheive each step in the sequence.





### State of the Art
 Most of the earlier works has been on assembly sequence planning for product design and manufacturing.



#### Geometrical methods





1.Methods based on Physics anlysis -- learning to deassemble/asssemble : Things that actually work

<video width="320"  height="240"  autoplay="true" muted="true" loop="true">
<source 
            src="http://asap.csail.mit.edu/static/videos/robot-01235.mp4" 
            type="video/mp4" />
</video>

2.Methods based on Learning Representation SORnet

<img src="https://lh5.googleusercontent.com/NHwjAH-VOvfitUPXCO2aSpHEYJMASYdbldUM_kT1qDfAyy6yXygVDoMLtPf-qW5dxAzqnlblp_tUMrwRVyEjtIKHXeS3eS0ddb5KAGUAI6O1MPIMwifRM-czEWE1LYDD=w1280" width="320" height="240"/>

3. Language based methods CLIPort

4. RL methods