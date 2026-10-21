# Saachi Varma Y — Developer Portfolio

A personal portfolio website showcasing my projects, technical skills, and journey as a Computer Science Engineering student. Built to bring my work together in one place and provide an easy way to connect with me.

**Live Website:** [portfolio-saachi.vercel.app](https://portfolio-saachi.vercel.app/)

## About

I'm a third-year B.E. Computer Science Engineering student interested in software development, cloud technologies, and AI engineering. This portfolio is an ongoing project where I apply what I learn, experiment with new technologies, and showcase projects I've worked on.

## Tech Stack

**Frontend**
- Vue.js
- HTML5
- CSS3
- JavaScript
- Vite

**Backend**
- Python
- FastAPI
- SMTP email integration for the contact form

**Deployment**
- Vercel — frontend hosting
- Render — backend hosting

## Featured Projects

### WeatherGPT
A conversational AI-powered weather project focused on making weather information and forecasts more accessible.

- **Repository:** [WeatherGPT](https://github.com/Puja105/weathergpt)

### AWS Notes App
A cloud-based notes application exploring AWS services, authentication, storage, and serverless backend integration.

- **Repository:** [AWS Notes App](https://github.com/Kronos1359/aws-notes-app)

### KronShop
An e-commerce project built to explore product management, backend APIs, and cloud-based deployment.

- **Repository:** [KronShop](https://github.com/Kronos1359/kronshop-ecommerce)
- **Live Demo:** [Open KronShop](https://main.d1i3uzv1bh4iey.amplifyapp.com/)

## Features

- Responsive design for desktop and mobile screens
- Animated hero section
- Dedicated sections for projects and technical skills
- Links to project repositories and live demos
- Contact form powered by a FastAPI backend
- Email delivery for contact form submissions
- Separate frontend and backend deployments

## Run Locally

### Prerequisites

- [Node.js](https://nodejs.org/)
- [Python](https://www.python.org/)

### 1. Clone the repository

```bash
git clone <YOUR_PORTFOLIO_REPOSITORY_URL>
cd portfolio
```

Replace the placeholder with the URL of this repository.

### 2. Run the frontend

```bash
cd frontend
npm install
npm run dev
```

Open the local URL printed by Vite, usually `http://localhost:5173`.

### 3. Run the backend

In a separate terminal:

```bash
cd backend
python -m venv venv
```

Activate the virtual environment.

**Windows:**
```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file inside the `backend` directory with the following variables:

```env
SMTP_EMAIL=your_email@gmail.com
SMTP_APP_PASSWORD=your_gmail_app_password
CONTACT_RECEIVER=your_email@gmail.com
```

Use a Gmail App Password where required, rather than your regular Gmail password. Keep `.env` private and never commit credentials to GitHub.

Start the backend:

```bash
uvicorn main:app --reload
```

The backend will usually be available at `http://127.0.0.1:8000`. Interactive API documentation is available at `http://127.0.0.1:8000/docs`.

## Environment Configuration

The backend uses environment variables for email configuration. When deploying, configure these variables in the hosting provider's environment settings instead of committing them to the repository.

For local development, the frontend and backend must be configured to communicate with each other, and the backend's CORS settings must allow the frontend origin.

## What I'm Learning

This project is helping me gain practical experience with:

- Building component-based interfaces using Vue.js
- Styling responsive layouts with CSS
- Designing and developing REST APIs with FastAPI
- Integrating frontend forms with backend services
- Handling environment variables and application configuration
- Deploying applications using Vercel and Render
- Managing projects with Git and GitHub

## Connect With Me

- **GitHub:** [Kronos1359](https://github.com/Kronos1359)
- **LinkedIn:** [Saachi Varma Y](https://www.linkedin.com/in/saachi-y-231915351/)

---

*Built as part of my journey toward becoming a better software developer. Continuously learning, building, and improving.*
