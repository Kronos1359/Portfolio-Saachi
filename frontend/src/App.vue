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

    <section id="about" class="about hero">
      <p class="hero-greeting">HELLO, I'M</p>
      <h1>Saachi Varma Y</h1>
      <h2>Computer Science Engineering Student</h2>
      <p class="hero-description">
        I build projects with Python, Vue.js, and cloud technologies
        while exploring software development and AI.
      </p>

      <div class="hero-actions">
        <a href="#projects" class="hero-button">View My Projects</a>
        <a 
          href="https://github.com/Kronos1359"
          target="_blank"
          rel="noopener noreferrer"
          class="hero-button secondary-button"
          >
          GitHub Profile
        </a>
      </div>
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
      <h2>Get in Touch</h2>
      <p>Have a question or want to work together? Send me a message.</p>
      
      <form class="contact-form" @submit.prevent>
        <label for="name">Your name</label>
        <input
          id="name"
          type="text"
          placeholder="Enter your name"
          required
        />

        <label for="email">Your email</label>
        <input
         id="email"
         type="email"
         placeholder="you@example.com"
         required
        />

        <label for="message">Your message</label>
        <textarea
          id="message"
          rows="5"
          placeholder="Write your message here..."
          required
        ></textarea>

        <button type="submit" class="hero-button">
          Send Message
        </button>
      </form>

      <p>
        Or find me on
        <a
          href = "https://www.linkedin.com/in/saachi-y-231915351/"
          target="_blank"
          rel="noopener noreferer">
          LinkedIn
        </a>
      </p>
    </section>
  </main>
</template>



