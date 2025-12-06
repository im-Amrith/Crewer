# Deployment Guide

This guide covers two common ways to deploy your CrewAI Enterprise application: **Streamlit Community Cloud** (easiest) and **Docker** (most flexible/production-ready).

## Option 1: Streamlit Community Cloud (Easiest)

Streamlit offers a free hosting service directly connected to your GitHub repository.

1.  **Push your code to GitHub**:
    *   Initialize a git repo: `git init`
    *   Add files: `git add .`
    *   Commit: `git commit -m "Initial commit"`
    *   Create a new repository on GitHub and push your code.

2.  **Deploy**:
    *   Go to [share.streamlit.io](https://share.streamlit.io/).
    *   Log in with GitHub.
    *   Click "New app".
    *   Select your repository, branch (usually `main`), and main file path (`app.py`).
    *   Click "Deploy".

3.  **Configure Secrets**:
    *   Once deployed, the app will fail initially because it lacks API keys.
    *   Go to your app's dashboard on Streamlit Cloud.
    *   Click the three dots menu (⋮) -> **Settings** -> **Secrets**.
    *   Paste your secrets in TOML format:
        ```toml
        GOOGLE_API_KEY = "your_gemini_key_here"
        SERPER_API_KEY = "your_serper_key_here"
        ```
    *   Save. The app will restart and should work.

## Option 2: Docker (Production)

You can containerize the application and deploy it to any platform that supports Docker (AWS ECS, Google Cloud Run, Azure Container Apps, Render, Railway, etc.).

### 1. Build the Image

```bash
docker build -t crewai-app .
```

### 2. Run Locally

```bash
docker run -p 8501:8501 --env-file .env crewai-app
```

### 3. Deploy to Cloud (Example: Render/Railway)

Most PaaS providers (Platform as a Service) like Render or Railway allow you to deploy directly from a GitHub repo using the Dockerfile.

1.  Push your code to GitHub.
2.  Connect your repository to the service (e.g., create a new Web Service on Render).
3.  The service will detect the `Dockerfile` and build it.
4.  **Important**: Add your Environment Variables (`GOOGLE_API_KEY`, `SERPER_API_KEY`) in the service's dashboard settings.

## Option 3: Hugging Face Spaces

1.  Create a new Space on Hugging Face.
2.  Select "Streamlit" as the SDK.
3.  Upload your files (or connect GitHub).
4.  Go to **Settings** -> **Variables and secrets** and add your API keys.
