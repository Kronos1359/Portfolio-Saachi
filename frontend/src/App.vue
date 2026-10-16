<script setup>
  import ProjectCard from './components/ProjectCard.vue'

  const projects = [
    {
      title: "WeatherGPT",
      description: "A chatbot that is specialized in weather reports.",
      repoUrl: "https://github.com/Puja105/weathergpt/tree/main"
    },
    {
      title: "AWS Notes app",
      description: "A cloud computing notes app that stores your notes and images.",
      repoUrl: "https://github.com/Kronos1359/aws-notes-app"
    },
    {
      title: "KronShop",
      description: "An AWS hosted e-commerce platform that can be used to buy and sell products.",
      repoUrl: "https://github.com/Kronos1359/kronshop-ecommerce",
      liveUrl: "https://main.d1i3uzv1bh4iey.amplifyapp.com/"
    }
  ]
</script>

<template>
  <main class="container">

    <nav class="navbar">
      <a href="#about">About</a>
      <a href="#skills">Skills</a>
      <a href="#projects">Projects</a>
      <a href="#contact">Contact</a>
    </nav>

    <section id="about" class="about">
      <h1>Saachi Varma Y</h1>
      <p class="intro">I'm a 3rd year B.E student majoring in Computer Science</p>
      <a href="https://github.com/Kronos1359">Visit my GitHub</a>
    </section>

    <hr>

    <section id="skills" class="skills">
      <h2>Skills</h2>
      <p> Python, FastAPI, Vue.js, HTML, CSS, JavaScript, Basics of C</p>
    </section>

    <hr>

    <section id="projects" class="projects">
      <h2>Projects</h2>

      <div class="project-grid">
        <ProjectCard
          v-for="project in projects"
          :key="project.title"
          :title="project.title"
          :description="project.description"
          :repoUrl="project.repoUrl"
          :liveUrl="project.liveUrl"
        />
      </div>
    </section>

    <hr>

    <section id="contact" class="contact">
      <h2>Contact me</h2>
      <p>
        <a href = "https://www.linkedin.com/in/saachi-y-231915351/">LinkedIn</a>
      </p>
    </section>
  </main>
</template>



