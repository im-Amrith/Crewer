# CrewAI Production App

This is a production-ready version of the CrewAI examples, refactored into a modular application.

## Setup

1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2.  Set up environment variables in a `.env` file:
    ```
    GOOGLE_API_KEY=your_gemini_api_key
    SERPER_API_KEY=your_serper_api_key
    ```

## What it does

This application leverages **CrewAI** and **Google Gemini** to orchestrate autonomous AI agents that work together to solve complex tasks. It features three specialized "crews":

1.  **🔍 Job Search Crew**:
    *   **Goal**: Help candidates land their dream job.
    *   **Process**: Analyzes a job posting URL, scrapes the candidate's GitHub and LinkedIn profiles, and uses a personal write-up to generate a **tailored resume** and **interview preparation materials**.
    *   **Agents**: Tech Job Researcher, Personal Profiler, Resume Strategist, Interview Preparer.

2.  **✍️ Content Creation Crew**:
    *   **Goal**: Produce high-quality blog content.
    *   **Process**: Takes a topic as input and orchestrates a team to plan, write, and edit a comprehensive blog post.
    *   **Agents**: Content Planner, Content Writer, Editor.

3.  **🛠️ Support Crew**:
    *   **Goal**: Provide exceptional customer support.
    *   **Process**: Analyzes a customer inquiry and drafts a detailed, helpful response, which is then reviewed by a QA agent for quality and tone.
    *   **Agents**: Senior Support Representative, Support Quality Assurance Specialist.

## Usage

1.  **Start the App**:
    Run the Streamlit frontend:
    ```bash
    streamlit run app.py
    ```

2.  **Select a Crew**:
    Use the sidebar navigation to choose the crew you want to run.

3.  **Provide Inputs**:
    *   **Job Search**: Enter the Job Posting URL, your GitHub URL, LinkedIn URL, and a short personal bio.
    *   **Content Creation**: Enter the topic you want the agents to write about.
    *   **Support**: Enter the Customer Name, Contact Person, and the Inquiry text.

4.  **Run & View Results**:
    Click the "Run" button. The agents will start working, and the final output (tailored resume, blog post, or support response) will be displayed directly in the interface.

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions on how to host this application using Streamlit Community Cloud or Docker.

## Structure

-   `app.py`: Main Streamlit application (Frontend)
-   `src/`: Source code
    -   `crews/`: Contains the different crews (Job Search, Content Creation, Support)
    -   `utils.py`: Utility functions (LLM setup, etc.)
-   `data/`: Data files (resumes, markdown files)
-   `main.py`: CLI Entry point (Alternative)
