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

This article is a literature review on the past and recent research related to robotic assembly. It belongs to a wide research domain called "assembly planing" which is jointly studied among fields such as  Computer Aided design(CAD), Manufacturing Industry, Robotics etc. However, expected research goals, problem definitions and solutions among the respective fields might be different from each other. This article attempts to identify, analyze and establish the idea of robotic assembly as a seperate research problem. While AI is a combination of various approaches to solve a certain problem autonomously, robotic assembling has been also approached using several methods such as visual language models, Reinforecement learning, 3D perception and Computer vision etc. 

**However, the major emphasis of this article is robotic assembly manipulation via 3D pereception**.
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

<figure align="center" style="padding-top: 20px; padding-bottom: 20px;">
  <img src="https://developer-blogs.nvidia.com/wp-content/uploads/2023/05/IndustReal_Simtoreal.gif"/>
  <figcaption>  <p style="text-align: center; font-size: 12px"> source: <a href="https://developer.nvidia.com/blog/transferring-industrial-robot-assembly-tasks-from-simulation-to-reality/">  Transferring Industrial Robot Assembly Tasks from Simulation (NVIDIA Isaac) to Real</a></p> </figcaption>
</figure>

### Cognition for robotic assembly manipulation

Robotic Manipulation has advanced drastically in the recent times. Availability of higher D0F freedom robots, sensors, computing capabilities and algorithms. Cognition means the capability of the robotic setup to sense and analyze the environment and plan and execute acriopns tp o accomplish goals. such primary goals include grasping, inspecting, painting, welding, assembling etc. The task of robotic assembling is process that extends from grasping. 

explain the steps: sequence planning, pose , motion planning etc

### State of the Art

### 1. Assembly Sequence planning

The process of assembly sequence planning is a highly constrained problem. However, it is easier to define the constraints when the assembly is in assembled state. Therefore, **Assembly by Disassembly Planning (ADP)** has been the most go-to approaches when planning assembly sequences. They also fall under graph based methods

Explain the historical methods from review paper here >> emphasize the use of geometrical analysis.
then go to <a href="#Ghandi2015">Ghandi et al(2015)</a> "assemble them all" and mention about use of physics simulations for cheching collision. and they dont consider stability, gravity etc 

Introduc ASAP which formulate the disassembly graph as a GNN solution.

Multi-level reasoning paper as a transformer based solution -- is also a ADP solution.



### 2. Assembly Pose estimation


3. Motion planning


#### Graph Based approaches









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
<li id="Ghandi2015" class="highlightable">
<p>Ghandi, S., & Masehian, E. (2015). <em>Review and taxonomies of assembly and disassembly path planning problems and approaches</em>. <em>Computer-Aided Design, 67–68, 58–86. https://doi.org/10.1016/j.cad.2015.05.001
</em>.</p>
</li>

<li id="Tian2022">
<p>Tian, Y., Xu, J., Li, Y., Luo, J., Sueda, S., Li, H., Willis, K. D. D., & Matusik, W. (2022). <em>Assemble Them All</em>. <em>ACM Transactions on Graphics, 41(6). https://doi.org/10.1145/3550454.3555525
</em>.</p>
</li>

<li id="Tian2023)">
<p>Tian, Y., Willis, K. D. D., Omari, B. al, Luo, J., Ma, P., Li, Y., Javid, F., Gu, E., Jacob, J., Sueda, S., Li, H., Chitta, S., & Matusik, W. (2023) <em> ASAP: Automated Sequence Planning for Complex Robotic Assembly with Physical Feasibility</em>. <em>http://arxiv.org/abs/2309.16909
</em>.</p>
</li>

<li id="Zhu2023)">
<p>Zhu, X., Jha, D. K., Romeres, D., Sun, L., Tomizuka, M., & Cherian, A. (2023) <em> Multi-level Reasoning for Robotic Assembly: From Sequence Inference to Contact Selection</em>. <em> http://arxiv.org/abs/2312.10571
</em>.</p>
</li>

<li id="Zhang2022">
<p>Zhang, R., Kong, T., Wang, W., Han, X., & You, M. (2022). <em>3D Part Assembly Generation with Instance Encoded Transformer</em>. IEEE Robotics and Automation Letters, 7(4). [https://doi.org/10.1109/LRA.2022.3188098](https://doi.org/10.1109/LRA.2022.3188098).</p>
</li>

<li id="Tian2023a">
<p>Tian, Y., Willis, K. D. D., Omari, B. al, Luo, J., Ma, P., Li, Y., Javid, F., Gu, E., Jacob, J., Sueda, S., Li, H., Chitta, S., & Matusik, W. (2023). <em>ASAP: Automated Sequence Planning for Complex Robotic Assembly with Physical Feasibility</em>. [http://arxiv.org/abs/2309.16909](http://arxiv.org/abs/2309.16909).</p>
</li>

<li id="Tian2022">
<p>Tian, Y., Xu, J., Li, Y., Luo, J., Sueda, S., Li, H., Willis, K. D. D., & Matusik, W. (2022). <em>Assemble Them All</em>. ACM Transactions on Graphics, 41(6). [https://doi.org/10.1145/3550454.3555525](https://doi.org/10.1145/3550454.3555525).</p>
</li>

<li id="Narang2022">
<p>Narang, Y., Storey, K., Akinola, I., Macklin, M., Reist, P., Wawrzyniak, L., Guo, Y., Moravanszky, A., State, G., Lu, M., Handa, A., & Fox, D. (2022). <em>Factory: Fast Contact for Robotic Assembly</em>. Robotics: Science and Systems. [https://doi.org/10.15607/RSS.2022.XVIII.035](https://doi.org/10.15607/RSS.2022.XVIII.035).</p>
</li>

<li id="Huang2020">
<p>Huang, J., Zhan, G., Fan, Q., Mo, K., Shao, L., Chen, B., Guibas, L., & Dong, H. (2020). <em>Generative 3D part assembly via dynamic graph learning</em>. Advances in Neural Information Processing Systems, 2020-December.</p>
</li>

<li id="Wu2023">
<p>Wu, R., Tie, C., Du, Y., Zhao, Y., & Dong, H. (2023). <em>Leveraging SE(3) Equivariance for Learning 3D Geometric Shape Assembly</em>. [http://arxiv.org/abs/2309.06810](http://arxiv.org/abs/2309.06810).</p>
</li>

<li id="Zhu2023b">
<p>Zhu, X., Jha, D. K., Romeres, D., Sun, L., Tomizuka, M., & Cherian, A. (2023). <em>Multi-level Reasoning for Robotic Assembly: From Sequence Inference to Contact Selection</em>. [http://arxiv.org/abs/2312.10571](http://arxiv.org/abs/2312.10571).</p>
</li>

<li id="Chen2022">
<p>Chen, Y. C., Li, H., Turpin, D., Jacobson, A., & Garg, A. (2022). <em>Neural Shape Mating: Self-Supervised Object Assembly with Adversarial Shape Priors</em>. Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition, 2022-June. [https://doi.org/10.1109/CVPR52688.2022.01239](https://doi.org/10.1109/CVPR52688.2022.01239).</p>
</li>

<li id="Li2023">
<p>Li, Y., Zeng, A., & Song, S. (2023). <em>Rearrangement Planning for General Part Assembly</em>. [https://general-part-assembly.github.io/](https://general-part-assembly.github.io/).</p>
</li>

<li id="Harish2022">
<p>Harish, A. N., Nagar, R., & Raman, S. (2022). <em>RGL-NET: A Recurrent Graph Learning framework for Progressive Part Assembly</em>. Proceedings - 2022 IEEE/CVF Winter Conference on Applications of Computer Vision, WACV 2022. [https://doi.org/10.1109/WACV51458.2022.00072](https://doi.org/10.1109/WACV51458.2022.00072).</p>
</li>

</ol>








