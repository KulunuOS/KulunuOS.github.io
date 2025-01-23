---
layout: about
title: About
banner: /images/tree.jpg
---

<div style="max-width: 750px; margin: 0 auto; padding: 10px; text-align: left; font-family: Arial, sans-serif; line-height: 1.8;">
  <!-- Slideshow Section -->
<div style="max-width: 750px; margin: 0 auto; text-align: center;padding-top: 30px">
  <div class="slideshow" style="width: 85%; height: 400px; margin: 0 auto; overflow: hidden; border-radius: 20px; position: relative;">
    <div class="slideshow-images" style="display: flex; width: 100%; animation: slide 24s infinite;">
      <img src="/images/me1.jpg" alt="Slide 1" style="width: 100%; height: 100%; object-fit: cover; flex-shrink: 0; border-radius: 10px;">
      <img src="/images/me2.jpg" alt="Slide 2" style="width: 100%; height: 100%; object-fit: cover; flex-shrink: 0; border-radius: 10px;">
      <img src="/images/me1.jpg" alt="Slide 3" style="width: 100%; height: 100%; object-fit: cover; flex-shrink: 0; border-radius: 10px;">
    </div>
  </div>
</div>

<style>
  @keyframes slide {
    0%, 20% { transform: translateX(0); }        /* Stay on the first slide */
    25%, 45% { transform: translateX(-100%); }  /* Transition to the second slide */
    50%, 70% { transform: translateX(-200%); }  /* Transition to the third slide */
    75%, 100% { transform: translateX(0); }     /* Smooth return to the first slide */
  }

  /* Slideshow speed */
  .slideshow-images {
    animation: slide 90s infinite; /* Slower and smoother animation (24 seconds total) */
  }

  /* Smoother transitions */
  .slideshow-images img {
    transition: transform 7s ease-in-out;
  }
</style>



  <!-- Profile Info Section -->
 <div style="text-align: center; margin-top: 20px; margin-bottom:0px;">
  <h1 style="margin: 5px 0; color: #333; font-weight: bold; font-size: 1.8rem;">
    Kulunu Samarawickrama
  </h1>
  <p style="margin-top: -5px; font-size: 1rem; color: #444;">
    Doctoral Researcher, Tampere University, Finland
  </p>
</div>


  <div style="max-width: 750px; margin: 0 auto; padding: 20px; text-align: center; font-family: Arial, sans-serif;">
  <nav style="display: flex; justify-content: center; gap: 20px; font-size: 1rem;">
    <a href="https://scholar.google.com/citations?user=KtoK4yAAAAAJ&hl=en&oi=ao" style="text-decoration: none; color: gray;">Google Scholar</a>
    <a href="https://github.com/KulunuOS" style="text-decoration: none; color: gray;">GitHub</a>
    <a href="https://www.linkedin.com/in/kulunuos" style="text-decoration: none; color: gray;">LinkedIn</a>
    <a href="mailto:kulunuds@gmail.com" style="text-decoration: none; color: gray;">Email</a>
  </nav>
    </div>

  <!-- Introduction -->
  <div style="margin-bottom: 30px; text-align: justify;">
    <h2 style="color: gray; font-size: 1.5rem;">Introduction</h2>
    <p>
      I am a doctoral researcher in the 
      <a href="https://research.tuni.fi/cogrob/" style="color: gray;">
        Cognitive Robotics Research Group
      </a> 
      at Tampere University, Finland. My work focuses on advancing 3D perception techniques to empower robotic systems with capabilities like grasping and assembly. I am driven by a desire to bridge the gap between cutting-edge research and its practical applications in industries. My fascination with how machines learn and adapt to their environments stems from years of academic exploration and hands-on experience.
    </p>
  </div>

  <!-- Career Journey -->
  <div style="margin-bottom: 30px; text-align: justify;">
    <h2 style="color: gray; font-size: 1.5rem;">My Journey</h2>

    <h3 style="font-size: 1.2rem; color: #444;">The Mechatronics Engineer</h3>
    <p>
      My academic journey began with a bachelor's degree in mechatronics at the Asian Institute of Technology, Thailand. During this time, I cultivated a strong foundation in mechanics, electronics, and programming. Post-graduation, I delved into the automation industry, working on challenging projects involving industrial robots and vision-based inspection systems. These experiences laid the groundwork for my growing passion for robotics and AI, inspiring me to explore further studies.
    </p>

    <h3 style="font-size: 1.2rem; color: #444;">The Researcher and Developer</h3>
    <p>
      My master’s journey at Tampere University allowed me to specialize in robotics and artificial intelligence. Immersed in courses like computer vision and machine learning, I honed my ability to design and implement intelligent systems. My thesis, focused on 3D perception for robotic manipulation, earned accolades for its innovation and rigor. Today, I channel this expertise into collaborative projects aimed at integrating robotics and AI into real-world applications.
    </p>
  </div>

  <!-- Research Focus -->
  <div style="margin-bottom: 30px; text-align: justify;">
    <h2 style="color: gray; font-size: 1.5rem;">Research Focus</h2>
    <p>
      My PhD research is at the intersection of cognitive science and robotics, where I work on building models that enable robots to think and act intelligently. My focus areas include:
    </p>
    <ul style="list-style-type: disc; margin-left: 20px; font-size: 1rem;">
      <li>Enhancing 3D visual perception for improved object detection and pose estimation</li>
      <li>Developing advanced algorithms for point cloud segmentation and analysis</li>
      <li>Creating synthetic datasets to simulate real-world scenarios for robotic training</li>
      <li>Integrating perception models into robotic systems via ROS for seamless automation</li>
      <li>Establishing robust benchmarks to evaluate model performance and accuracy</li>
    </ul>
  </div>

  <!-- Publications -->
  <div style="margin-bottom: 30px; text-align: justify;">
    <h2 style="color: gray; font-size: 1.5rem;">Publications</h2>
    <ul style="list-style-type: none; padding: 0; font-size: 1rem;">
      <li style="margin-bottom: 15px;">
        <strong>Automatic Dataset Generation From CAD for Vision-Based Grasping</strong><br>
        Ahmad, Samarawickrama, K., Rahtu, E., & Pieters, R. (2021).<br>
        <em>2021 20th International Conference on Advanced Robotics (ICAR)</em>, 715–721.<br>
        <a href="https://doi.org/10.1109/ICAR53236.2021.9659336" style="color: gray;">
          Read more
        </a>
      </li>
      <li style="margin-bottom: 15px;">
        <strong>Sensor-based human–robot collaboration for industrial tasks</strong><br>
        Alexandre Angleraud, Akif Ekrekli, Kulunu Samarawickrama, Gaurang Sharma, Roel Pieters<br>
        <em>Robotics and Computer-Integrated Manufacturing, Volume 86, 2024</em>.<br>
        <a href="https://doi.org/10.1016/j.rcim.2023.102663" style="color: gray;">
          Read more
        </a>
      </li>
    </ul>
  </div>
</div>
