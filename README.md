# Saachi Varma Y — Developer Portfolio

My personal developer portfolio, built to showcase my projects, technical skills, and learning journey as a Computer Science engineering student.

**Live website:** [portfolio-saachi.vercel.app](https://portfolio-saachi.vercel.app/)

## About

I'm a third-year B.E. Computer Science student interested in software development, cloud computing, and AI engineering. This portfolio brings together my projects, the technologies I work with, and a way to get in touch.

## Tech Stack

### Frontend
- Vue 3
- JavaScript
- HTML5 and CSS3
- Vite

### Backend
- Python
- FastAPI
- Mangum — adapts FastAPI for AWS Lambda

### Cloud and Deployment
- AWS Lambda — serverless backend execution
- Amazon API Gateway — HTTPS API endpoint
- Vercel — frontend hosting
- Git and GitHub — version control

### Contact Form
The contact form sends messages through a FastAPI endpoint deployed on AWS Lambda. The backend uses Gmail SMTP, with credentials stored in Lambda environment variables.

## Featured Projects

### WeatherGPT
A conversational weather platform designed to make weather information more accessible, with a focus on forecasts, weather risk, and multilingual accessibility.

- **Repository:** [WeatherGPT](https://github.com/Puja105/weathergpt)

### AWS Notes App
A cloud-based notes application built to explore authentication, storage, and serverless AWS services.

- **Repository:** [AWS Notes App](https://github.com/Kronos1359/aws-notes-app)

### KronShop
An e-commerce project exploring full-stack development and AWS deployment.

- **Repository:** [KronShop](https://github.com/Kronos1359/kronshop-ecommerce)
- **Live application:** [Open KronShop](https://main.d1i3uzv1bh4iey.amplifyapp.com/)

## Architecture

The portfolio uses a separate frontend and backend.

```text
Visitor
   |
   v
Vue 3 Frontend (Vercel)
   |
   | HTTPS POST /contact
   v
Amazon API Gateway
   |
   v
AWS Lambda
   |
   v
FastAPI + Mangum
   |
   v
Gmail SMTP
   |
   v
Contact email recipient
```

## Run Locally

### Prerequisites
- Python 3.13
- Node.js and npm
- Git

### 1. Clone the repository

```bash
git clone https://github.com/Kronos1359/Portfolio-Saachi.git
cd portfolio
```

### 2. Start the frontend

```bash
cd frontend
npm install
npm run dev
```

Vite will display the local development URL in the terminal.

### 3. Start the backend locally

Open a separate terminal from the repository root:

```bash
cd backend
py -3.13 -m venv .venv
```

Activate the virtual environment on Windows:

```bash
source .venv/Scripts/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create a local `.env` file in the `backend/` directory with the following variables:

```dotenv
SMTP_EMAIL=your_sender_email
SMTP_APP_PASSWORD=your_gmail_app_password
CONTACT_RECEIVER=your_receiver_email
```

Replace the example values with your own credentials. Never commit this file.

Start the local API:

```bash
uvicorn main:app --reload
```

The FastAPI application should be available at `http://127.0.0.1:8000`.

**Note:** The deployed frontend uses the AWS API Gateway endpoint. To test the contact form locally, configure your local frontend to call your local backend.

## Environment Variables

| Variable | Purpose |
|---|---|
| `SMTP_EMAIL` | Gmail account used to send messages |
| `SMTP_APP_PASSWORD` | Gmail App Password |
| `CONTACT_RECEIVER` | Email address receiving contact messages |

These variables are configured in AWS Lambda for production and in a private `.env` file for local development.

## Deployment

- **Frontend:** deployed on Vercel.
- **Backend:** deployed on AWS Lambda using Mangum.
- **API:** exposed through Amazon API Gateway.
- **CORS:** configured to allow requests from the deployed portfolio origin.

The Lambda deployment ZIP is generated locally and is not committed to the repository.

## What I'm Learning

- Full-stack web development
- REST APIs and backend development
- Cloud deployment and serverless architecture
- Python and JavaScript
- AI and machine learning fundamentals

## Connect

- **Portfolio:** [portfolio-saachi.vercel.app](https://portfolio-saachi.vercel.app/)
- **GitHub:** [Kronos1359](https://github.com/Kronos1359)
- **LinkedIn:** [Saachi Varma Y](https://www.linkedin.com/in/saachi-y-231915351/)

---

Built as a personal project to practise development, deployment, and continuous improvement.
