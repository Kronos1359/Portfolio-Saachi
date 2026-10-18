<script setup>
  import { ref, onMounted } from 'vue'
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

  const displayedName = ref('')

  const name = "Saachi Varma Y"

  onMounted(() => {
    let index = 0

    const timer = setInterval(() => {
      displayedName.value += name[index]
      index++

      if (index >= name.length) {
        clearInterval(timer)
      }
    }, 110)
  })

  const form = ref({
    name: '',
    email: '',
    message: ''
  })

  const statusMessage = ref('')
  const statusType = ref('')
  const isSubmitting = ref(false)
  
  async function submitContactFrom() {
    statusMessage.value = ''
    isSubmitting.value = true

    try {
      const response = await fetch('http://127.0.0.1:8000/contact', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(form.value)
      })

      const data = await response.json()

      if (!response.ok) {
        statusType.value = 'error'
        statusMessage.value = 
          data.detail || 'Your message could not be sent. Please try again.'
        return
      }

      statusType.value = 'success'
      statusMessage.value = 'Your message has been sent successfully!'

      form.value = {
        name: '',
        email: '',
        message: ''
      }
    } catch (error) {
      console.error('Contact form submission failed:', error)
      statusType.value = 'error'
      statusMessage.value =
        'Could not connect to the server. Please try again later.'
    } finally {
        isSubmitting.value = false
    }
  }
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
      <div class="hero-content">
        <p class="hero-greeting">HELLO, I'M</p>
        <h1>
          {{ displayedName }}<span class="typing-cursor">|</span>
        </h1>
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
      </div>

      <div class="hero-animation">
        
      </div>
    </section>

    <hr>

    <section id="skills" class="skills">
      <div class="skill-heading">
        <p class="skills-eyebrow">WHAT I WORK WITH</p>
        <h2>Skills & Technologies</h2>
        <p class="skills-description">
          Technologies I've been learning and using to build projects.
        </p>
      </div>

      <div class="skills-grid">
        <div class="skill-category">
          <h3>Languages</h3>
          <div class="skill-list">
            <span class="skill-item">Python</span>
            <span class="skill-item">Javascript</span>
            <span class="skill-item">C (Basics)</span>
          </div>
        </div>
        <div class="skill-category">
          <h3>Frontend</h3>
          <div class="skill-list">
            <span class="skill-item">HTML</span>
            <span class="skill-item">CSS</span>
            <span class="skill-item">Vue.js</span>
          </div>
        </div>
        <div class="skill-category">
          <h3>Backend & Cloud</h3>
          <div class="skill-list">
            <span class="skill-item">FastAPI</span>
            <span class="skill-item">AWS</span>
            <span class="skill-item">Flask</span>
          </div>
        </div>
      </div>
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
      
      <form class="contact-form" @submit.prevent="submitContactFrom">
        <label for="name">Your name</label>
        <input
          id="name"
          v-model="form.name"
          type="text"
          placeholder="Enter your name"
          required
        />

        <label for="email">Your email</label>
        <input
         id="email"
         v-model="form.email"
         type="email"
         placeholder="you@example.com"
         required
        />

        <label for="message">Your message</label>
        <textarea
          id="message"
          v-model="form.message"
          rows="4"
          placeholder="Write your message here..."
          required
        ></textarea>

        <button
          type="submit"
          class="hero-button"
          :disabled="isSubmitting">
          {{ isSubmitting ? 'Sending...' : 'Send Message' }}
        </button>
      </form>

      <Transition name="toast">
        <div
          v-if="statusMessage"
          class="toast"
          :class="statusType"
          role="status"
          aria-live="polite"
        >
          <span class="toast-message">{{ statusMessage }}</span>

          <button
            type="button"
            class="toast-close"
            aria-label="Close notification"
            @click="statusMessage = ''"
          >
            x
          </button>
        </div>
      </Transition>

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



