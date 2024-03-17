---
layout: post
title: "Assembling objects with robots"
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

<div align="center">
  <video width="640" height="280" autoplay="true" muted="true" loop="true" style="margin-top: 50px;">
    <source src="https://assets.mixkit.co/videos/preview/mixkit-girl-putting-together-a-figure-with-legos-42182-large.mp4" type="video/mp4" />
  </video>
  <p style="text-align: center; font-size: 12px"> image source: <a href="https://mixkit.co/free-stock-video/girl-putting-together-a-figure-with-legos-42182/">  mixkit.com</a></p>
</div>

As a kid, you probably have had building blocks or puzzels that you put together and build up meaningful assemblies. These toys have a close relationship with the development of cognition in early childhood. As humans our skills develops rapidly with experience as we age until these tasks become so ordinary. However, attempting to endow these cognitive skills in robots is a massive challenge and a major research emphasis in the field of cognitive robotics. Cognitive robotics is a subfield of robotics that focuses on enabling robots to perform cognitive functions with artificial intelligence.

This article is a literature review on the past and recent research related to robotic assembly. It belongs to large reserach domain called "assembly planing" which is jointly studied among fields such as  Computer Aided design(CAD), Manufacturing Industry, Robotics etc. However, the expected research goals, problem definitions and solutions might be different from each other. Though it might not be flawless, the article also attempt to identify, analyze and establish the idea of robotic assembly as a seperate research problem. While AI is a combination of various approaches to address a certain problem, robotic assembling has been also addressed under several methods such as Visual language models, Reinforecement learning, 3D perception and Computer vision etc. 

For the convenience of the reader please follow the organisation and relevant queries of the article below :


| | Section                                  | Questions                                           |
| |------------------------------------------|-----------------------------------------------------|
|1| [The bigger picture](#the-bigger-picture) | - Where does robotic assembly manipulation stand in the bigger picture of process manufacturing? - How is it all connected? |
|2| Assembling as a manipulation task    | - How to define robotic assembly manipulation? - How is it different/similar from assembly process planning? |
|3| Cognition for robotic manipulation   | - How to endow cognitive capabilities for robots to perform assembling? |
|4| State of the Art                     | - What has been studied? - What has been achieved? - Challenges? - Research gaps? - Possible contributions? |


---
### 1. The bigger picture

Assembling is a core aspect in manuifacturing processes. Hence, most of the past studies on object assembling has been from the point of view of process planning in manufacturing industry. The term **Assembly Planning** describes the process of combining several parts to a final product. Assembly Sequence Planning, Assembly line balancing, Assembly Path Planning. The importance of Assembly planning is maintenance, cost and time effectiveness, repair etc. They look at Ap as valuble feedback for design stage of products to achieve above targets in manufacturing process.

However, the intended goals from persepective of cognitive robotics is different. Explain the difference. In above case the process planner ( a human) reveiews ( find more differences) complex constraints such as friction etc. In robotics the robot should take the decisions. This more difficult and might not have solutions all the time. 

probably a diagram explaining the domain

But it is important to observe how humans think and then try to develop robot cognition through the same pattern of thinking. 


### 2. Assembling as a manipulation task

A manipulation task involves primary components such as a single or multiple robotic manipulators, a scene consisting of objects to be manipulated in their initial state and a goal state to be acheived. In certain cases, a human operator could also collaborate with a robot to perform the task.

In an assembly manipulation task, there could be either individual objects or partly assembled objects in the scene. Ideally the robotic manipulator should be a robotic arm with a suitable degrees of freedom and a gripper that is capable of grasping the objects. 

The feasibility of an assembly task depends on several constraints. The objects and final assembly must be within the workspace of the robot. The assembly task should be achievable within the task space of the robot. An assembly sequence must exist to rearrange the objects from their initial state to final state. Furthermore, the robot should be capable of following a motion plan to acheive each step in the sequence.

### Cognition for robotic assembly manipulation

Robotic Manipulation has advanced drastically in the recent times. Availability of higher D0F freedom robots, sensors, computing capabilities and algorithms. Cognition means the capability of the robotic setup to sense and analyze the environment and plan and execute acriopns tp o accomplish goals. such primary goals include grasping, inspecting, painting, welding, assembling etc. The task of robotic assembling is process that extends from grasping. 


### State of the Art



#### Graph Based methods

ASAP and Assemble them all







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

<img src="https://developer-blogs.nvidia.com/wp-content/uploads/2023/05/IndustReal_Simtoreal.gif" align="center"/>

### References

<ol>
<li id="smith2020">
<p>Smith, J. (2020). <em>The Title of the Article</em>. <em>Journal Name</em>.</p>
</li>
</ol>