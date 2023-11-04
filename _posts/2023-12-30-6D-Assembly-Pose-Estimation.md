---
layout: paper
title:  6D Assembly Pose Estimation by Point Cloud Registration for Robot Manipulation  
abstract: A proposed framework for robotic assembling with semantic segmentation of the scene and registering point clouds of local surfaces against target point clouds derived from CAD models in order to detect 6D assembly poses.
tags: [ ]
category: Robotic Manipulation
thumbnail: /images/Assembly_Pose/overall_method.png
jquery: true
slideshow2: true
time: 15
words: 3619
---

## {{ page.title }}

Kulunu Samarawickrama, Gaurang Sharma, Alexandre Angleraud and Roel Pieters

<div>
    <a href="https://github.com/KulunuOS">
      <img src="https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&logoColor=white&link=https://github.com/minoveaz" height="35" alt="Build status"/>
    </a>
    <a href="https://arxiv.org/abs/ARXIV_ID">
      <img src="https://img.shields.io/badge/arXiv-ARXIV_ID-blue" height="35" alt="arXiv badge"/>
    </a>
</div> 

### Abstract

<div style="max-width: 1000px;  text-align: justify;">

<p>The demands on robotic manipulation skills to perform challenging tasks have drastically increased in recent times. To perform these tasks with dexterity, robots require perception tools which understands the scene and extract useful information that transforms to controller inputs. To this end, modern research has introduced various object pose estimation and grasp pose detection methods that yield precise results. Assembly pose estimation is a secondary yet highly desirable skill in robotic assembling since it requires specific information on object placement unlike bin picking and pick and place tasks. However, it has been often overlooked in the research due to complexity in integrating to an agile framework. To address this issue, we propose a simple two step assembly pose estimation method with RGB-D input and 3D CAD models of the associated objects. The framework consists of semantic segmentation of the scene and registering point clouds of local surfaces against target point clouds derived from CAD models in order to detect 6D poses. We show that our method can deliver sufficient accuracy for assembling object assemblies using evaluation metrics and demonstrations.</p>
</div>

### Synthetic Dataset for Object Assemblies

<div>
<figure style="display: flex; justify-content: flex-start; text-align: left;">
  <figure style="width: 50%;">
    <img class="img" src="/images/Assembly_Pose/Algorithm_2.png" style="height: 60%;">
    <figcaption style="text-align: left; line-height: 1.5em; max-width: 400px;">
      <b>Figure 1: Proposed framework for grasp manipulation assembly</b><br>
      Proposed 6D assembly pose estimation method with (A) RGBD Input, (B) Semantic Segmentation module, (C) Target & Source point cloud projection, (D) Point cloud registration, and (E) Local pose transformation
    </figcaption>
  </figure>
  <figure style="width: 58%;">
    <img class="img-animate" src="/images/Assembly_Pose/Nema_result1.png" style="height: 60%">
    <figcaption style="text-align: left; line-width: 1.5em;">
      <b>Figure 2: Another Figure Title</b><br>
      Description for the second figure goes here.
    </figcaption>
  </figure>
</figure>
</div>

### 6D Assembly Pose Estimation

<div style="text-align: center">
<figure style="width: 100%; display: inline-block;">
  <img class="img" src="/images/Assembly_Pose/framework.png">
  <figcaption style="text-align: left; line-height: 1.5em;"><b> Figure 1: Proposed framework for grasp manipulation assembly</b>  <p>roposed 6D assembly pose estimation method with (A) RGBD Input, (B) Sementic Segmentation module, (C)Target & Source point cloud projection, (D) Point cloud registration and (E) Local pose transformation </p></figcaption>
</figure>
</div>

### Results

---
