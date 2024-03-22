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
  <video width="100%" height="auto" autoplay muted loop style="max-width: 100%; margin-top: 50px;">
    <source src="https://assets.mixkit.co/videos/preview/mixkit-girl-putting-together-a-figure-with-legos-42182-large.mp4" type="video/mp4" />
  </video>
  <p style="text-align: center; font-size: 12px"> image source: <a href="https://mixkit.co/free-stock-video/girl-putting-together-a-figure-with-legos-42182/">  mixkit.com</a></p>
</div>

As a kid, you probably have had building blocks or puzzels that you put together and build up meaningful assemblies. These toys have a close relationship with the development of cognition in early childhood. As humans our skills develops rapidly with experience as we age until these tasks become so ordinary. However, attempting to endow these cognitive skills in robots is a massive challenge and a major research emphasis in the field of cognitive robotics. Cognitive robotics is a subfield of robotics that focuses on enabling robots to perform cognitive functions with artificial intelligence.

This article is a literature review on the past and recent research related to robotic assembly. It belongs to a wide research domain called "assembly planing" which is jointly studied among fields such as  Computer Aided design(CAD), Manufacturing Industry, Robotics etc. However, expected research goals, problem definitions and solutions among the respective fields might be different from each other. This article attempts to identify, analyze and establish the idea of robotic assembly as a seperate research problem. While AI is a combination of various approaches to solve a certain problem autonomously, robotic assembling has been also approached using several methods such as visual language models (SORNET), Reinforecement learning, 3D perception and Computer vision etc. 

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

Cognition can be defined as the capability of the robotic setup to sense and analyze the environment and plan and execute acriopns tp o accomplish goals.Few example for  such primary goals are grasping, inspecting, painting, welding, assembling etc. 

The task of robotic assembling is process that extends from grasping. Additionally following comnponents are closely relhated to the cognition associated with assembling with a robot

1. Assembly sequence planning
2. Assembly pose estimation
3. planning the motion

### State of the Art

### 1. Assembly Sequence planning

A 3D assembly is essentially constrained by the contacts with adjoining parts. Planning an assembly sequence at disassembled state requires defining motion constraints at each assembly step. However, it is easier plan disassembly since the geometric constraints are already defined in the assembled state. Therefore, **Assembly by Disassembly Planning (ADP)** has been a more prominent approache in planning assembly sequences.

Some classical approaches on assembly sequence planning has been extensively reviewed by <a href="#Ghandi2015"> Ghandi et al(2015) </a>. In the absence of sophisticated physics simulators and computational resources, most of these early methods relied on analysing the geometry at the part design level. An attempt at geometrica reasoning about mechanical assembly was presented by <a href="#Latombe1994"> Wilson et al(1994)</a> which uses Non-blocking Diagrams(NDBS) akin to the Motion space concept in robotic motion planning. some more studies present utilizing <a href="#Tseng1999"> connector-based graphs</a> and <a href="#DeMello1990"> AND/OR graphs </a> for assembly sequence planning. These methods suffer when the complexity of the parts in assemblies increase. Furthermore, these methods donot count in external factors which affect assembly such as stability under gravity or friction.

<span id="global_caption_ref"></span>

<div style="margin-top: 20px; margin-bottom: 20px;">
    <div style="display: flex;">
        <div style="flex: 1; margin-right: 10px; margin-top: 70px;">
            <img src="/images/Assembly_Pose/dgb.png" alt="Image 1" style="width: 100%;">
            <p style="text-align: center; font-size: 12px; margin-top: 5px;"> (a) Directional Blocking Diagram</p>
        </div>
        <div style="flex: 1; margin-right: 10px;">
            <img src="/images/Assembly_Pose/ndgb.png" alt="Image 2" style="width: 87%;">
            <p style="text-align: center; font-size: 12px; margin-top: 5px;"> (b) Non-Directional Blocking Diagram (partial)</p>
        </div>
    </div>
    <p style="text-align: center; margin-top: -10px; font-size: 12px"> source: <a href="https://doi.org/10.1016/0004-3702(94)90048-5">  Wilson et al.(1994)</a></p>
</div>


Later on, a study called <a href="#Tian2022"> "assemble them all"</a> expolits a physics-simulator for assembly sequence planning and assembly motion path planning (ASP) while checking the collsion between parts. Their sequence planner runs a bredth-first tree seach (BFS) to find a disassembly sequence while checking collisons. while this was an efficient for small assemblies the complexity increased exponentially with number of parts involved. They also attempted the problem assuming the assembly and parts were in mid air and did not consider factors such as stability, gravity or friction. 

<a href="#Tian2023"> ASAP.(2023)</a> is a recent study which adress all the shortcoming mentioned in above method. Their study considers the feasibiltty in assembly sequence planning with suitable assembly poses which are stable under gravity. This is an important  consideration when implementing a sequence planner for a practical problem such as roboric assembly. Furthermore, they formulate the tree search algorithm to a Graph Neural Network (GNN) that learns on the pointclouds of input parts and infer the next part to be disassemnbled. However, the approach doesn't seem to be robust against the number of parts in the assembly; meaning the GNN has to be trained for each set of assemblies with similar number of parts.


<div style="flex: 1; margin-right: 10px;">
    <img src="http://asap.csail.mit.edu/static/images/SearchTree.jpg" style="width: 100%;">
    <p style="text-align: center;font-size: 12px; margin-top: 5px;"> (b) Disassembly tree </p>
    <p style="text-align: center; margin-top: -10px; font-size: 12px"> source: <a href="http://asap.csail.mit.edu/">  ASAP:Automated Sequence Planning for Complex Robotic Assembly with Physical Feasibility</a></p>
</div>

 <a href="#Zhu2023b"> Zhu et al.(2023)</a> introduced a transformer based solution based on ADP.(still under analysis)



### 2. Assembly Pose estimation

There is a classification of approaches: 

Generalized approaches : trained on a category of objects can predict on any assembly in the category
example : can assemble chairs/tables/lamps of any shape. 

Few contradictions in the literature. Although some work claim that they dont use any prior semantic knowledge but models are conditioned on a category that represents some sort of semantic knowledge abouty the assembly.
Some generative methods learns on a set of points given that they belong to category ( conditioned) can do it on an unseen part! <a href="#Huang2020"> Huang et al.(2020)</a>. uses GNNs to learn the features and relationships between parts.(furniture assenbly)

A similar work  <a href="#Harish2022"> RGL-NET.(2022)</a> focus on progressive part assembly, meaning that starting from any stage the robot can continue to complete the assembly (furniture assenbly)
Another study <a href="#Zhang2022"> Zhang et al.(2022)</a> presents the capability to estimate assembly poses when the number of input parts is arbitrary or assembly is in mid-process. based an instance endcoded tranformer approach. a (furniture assenbly)

Another approach <a href="#Chen2022">Neural shape mating</a>  which learns to mate two parts to an assembly. Although this work is limited to two objects, it works well when the two pointcloud splits are very noisy and exceeds GNNs in performance in such situations.
A true category agnostic model. works well with unseen categories. also robust to unseen cut types

Final approach <a href="#Li2023"> Rearrangement planning</a> is to assemble a known target with unseen part point clouds. they do this by estimating pointclouds to a segmented version of target pointcloud. then the pose of the assembled part is estimated as transformation from the given part to target segment. this is called a general part assembly transfomer. 




Specialized approach : trained to predict only on one assembly : similar to generic object pose assembly? or pointcloud registration methods?





### 3. Motion planning


### References

<ol>

<li id="Latombe1994">
  <p>Wilson, R. H., & Latombe, J. C. (1994). <em>Geometric reasoning about mechanical assembly</em>. Artificial Intelligence, 71(2). <a href="https://doi.org/10.1016/0004-3702(94)90048-5">https://doi.org/10.1016/0004-3702(94)90048-5</a></p>
</li>

<li id="Tseng1999">
  <p>Tseng H-E, Li R-K. A novel means of generating assembly sequences using the connector concept. J Intell Manuf 1999;10:423–35. <a href="insert_URL_here">Link</a></p>
</li>

<li id="Ghandi2015" class="highlightable">
  <p>Ghandi, S., & Masehian, E. (2015). <em>Review and taxonomies of assembly and disassembly path planning problems and approaches</em>. <em>Computer-Aided Design, 67–68, 58–86. <a href="https://doi.org/10.1016/j.cad.2015.05.001">https://doi.org/10.1016/j.cad.2015.05.001</a></em>.</p>
</li>

<li id="Tian2022">
  <p>Tian, Y., Xu, J., Li, Y., Luo, J., Sueda, S., Li, H., Willis, K. D. D., & Matusik, W. (2022). <em>Assemble Them All</em>. <em>ACM Transactions on Graphics, 41(6). <a href="https://doi.org/10.1145/3550454.3555525">https://doi.org/10.1145/3550454.3555525</a></em>.</p>
</li>

<li id="Tian2023a">
  <p>Tian, Y., Willis, K. D. D., Omari, B. al, Luo, J., Ma, P., Li, Y., Javid, F., Gu, E., Jacob, J., Sueda, S., Li, H., Chitta, S., & Matusik, W. (2023). <em>ASAP: Automated Sequence Planning for Complex Robotic Assembly with Physical Feasibility</em>. <a href="http://arxiv.org/abs/2309.16909">http://arxiv.org/abs/2309.16909</a>.</p>
</li>

<li id="Zhu2023)">
  <p>Zhu, X., Jha, D. K., Romeres, D., Sun, L., Tomizuka, M., & Cherian, A. (2023) <em> Multi-level Reasoning for Robotic Assembly: From Sequence Inference to Contact Selection</em>. <a href="http://arxiv.org/abs/2312.10571">http://arxiv.org/abs/2312.10571</a>.</p>
</li>

<li id="Zhang2022">
  <p>Zhang, R., Kong, T., Wang, W., Han, X., & You, M. (2022). <em>3D Part Assembly Generation with Instance Encoded Transformer</em>. IEEE Robotics and Automation Letters, 7(4). <a href="https://doi.org/10.1109/LRA.2022.3188098">https://doi.org/10.1109/LRA.2022.3188098</a>.</p>
</li>

<li id="Narang2022">
  <p>Narang, Y., Storey, K., Akinola, I., Macklin, M., Reist, P., Wawrzyniak, L., Guo, Y., Moravanszky, A., State, G., Lu, M., Handa, A., & Fox, D. (2022). <em>Factory: Fast Contact for Robotic Assembly</em>. Robotics: Science and Systems. <a href="https://doi.org/10.15607/RSS.2022.XVIII.035">https://doi.org/10.15607/RSS.2022.XVIII.035</a>.</p>
</li>

<li id="Huang2020">
  <p>Huang, J., Zhan, G., Fan, Q., Mo, K., Shao, L., Chen, B., Guibas, L., & Dong, H. (2020). <em>Generative 3D part assembly via dynamic graph learning</em>. Advances in Neural Information Processing Systems, 2020-December.</p>
</li>

<li id="Wu2023">
  <p>Wu, R., Tie, C., Du, Y., Zhao, Y., & Dong, H. (2023). <em>Leveraging SE(3) Equivariance for Learning 3D Geometric Shape Assembly</em>. <a href="http://arxiv.org/abs/2309.06810">http://arxiv.org/abs/2309.06810</a>.</p>
</li>

<li id="Chen2022">
  <p>Chen, Y. C., Li, H., Turpin, D., Jacobson, A., & Garg, A. (2022). <em>Neural Shape Mating: Self-Supervised Object Assembly with Adversarial Shape Priors</em>. Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition, 2022-June. <a href="https://doi.org/10.1109/CVPR52688.2022.01239">https://doi.org/10.1109/CVPR52688.2022.01239</a>.</p>
</li>

<li id="Li2023">
  <p>Li, Y., Zeng, A., & Song, S. (2023). <em>Rearrangement Planning for General Part Assembly</em>. <a href="https://general-part-assembly.github.io/">https://general-part-assembly.github.io/</a>.</p>
</li>

<li id="Harish2022">
  <p>Harish, A. N., Nagar, R., & Raman, S. (2022). <em>RGL-NET: A Recurrent Graph Learning framework for Progressive Part Assembly</em>. Proceedings - 2022 IEEE/CVF Winter Conference on Applications of Computer Vision, WACV 2022. <a href="https://doi.org/10.1109/WACV51458.2022.00072">https://doi.org/10.1109/WACV51458.2022.00072</a>.</p>
</li>

<li id="DeMello1990">
  <p>Homem De Mello LS, Sanderson AC. AND/OR graph representation of assembly plans. IEEE Trans. Robot. Autom. 1990;6:188–99. <a href="insert_URL_here">Link</a></p>
</li>



</ol>








