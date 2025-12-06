import streamlit as st
import sys
import os

# Add the current directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.crews.job_search.job_search_crew import JobSearchCrew
from src.crews.content_creation.content_crew import ContentCreationCrew
from src.crews.support.support_crew import SupportCrew

st.set_page_config(page_title="CrewAI Enterprise", page_icon="🚀", layout="wide")

# Custom CSS for a cleaner look
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6
    }
    .sidebar .sidebar-content {
        background: #ffffff
    }
    h1 {
        color: #1f2937;
    }
    .stButton>button {
        background-color: #2563eb;
        color: white;
        border-radius: 6px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🚀 CrewAI Enterprise")
    st.markdown("### Automated Multi-Agent Workflows")
    st.markdown("---")
    
    st.header("Select Workflow")
    crew_selection = st.radio(
        "Choose a specialized crew:",
        ("Job Search Assistant", "Content Studio", "Customer Support Hub"),
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    with st.expander("⚙️ Configuration"):
        st.text_input("Gemini API Key", type="password", help="Override .env setting")
        st.text_input("Serper API Key", type="password", help="Override .env setting")
        st.checkbox("Enable Verbose Mode", value=True)

    st.markdown("### 📚 Resources")
    st.markdown(
        """
        - [Documentation](https://docs.crewai.com)
        - [GitHub Repository](https://github.com/joaomdmoura/crewAI)
        """
    )
    
    st.markdown("---")
    st.caption("© 2025 CrewAI Enterprise. v1.0.0")

# Main Content
if crew_selection == "Job Search Assistant":
    st.title("🔍 Job Search Assistant")
    st.markdown("### Accelerate your career with AI-driven insights")
    st.markdown("Our agents analyze job postings and your profile to generate tailored resumes and interview prep materials.")
    st.markdown("---")

    with st.form("job_search_form"):
        col1, col2 = st.columns(2)
        with col1:
            job_posting_url = st.text_input("Job Posting URL", placeholder="https://company.com/careers/job-id")
            github_url = st.text_input("GitHub Profile URL", placeholder="https://github.com/username")
        with col2:
            linkedin_url = st.text_input("LinkedIn Profile URL", placeholder="https://linkedin.com/in/username")
            
        personal_writeup = st.text_area("Personal Bio & Goals", placeholder="Briefly describe your background, key skills, and what you are looking for...", height=150)
        
        submitted = st.form_submit_button("🚀 Launch Job Search Crew")

    if submitted:
        if not job_posting_url or not github_url or not linkedin_url or not personal_writeup:
            st.error("Please fill in all required fields.")
        else:
            with st.spinner("🤖 Agents are working... Analyzing job, profiling candidate, and strategizing..."):
                try:
                    inputs = {
                        'job_posting_url': job_posting_url,
                        'github_url': github_url,
                        'linkedin_url': linkedin_url,
                        'personal_writeup': personal_writeup
                    }
                    crew = JobSearchCrew()
                    result = crew.kickoff(inputs=inputs)
                    st.success("✅ Job Search Analysis Completed!")
                    st.markdown("### 📄 Results")
                    st.markdown(result)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

elif crew_selection == "Content Studio":
    st.title("✍️ Content Studio")
    st.markdown("### Create engaging, high-quality content at scale")
    st.markdown("Orchestrate a team of planners, writers, and editors to produce polished blog posts on any topic.")
    st.markdown("---")

    with st.form("content_creation_form"):
        topic = st.text_input("Content Topic", placeholder="e.g., The Impact of Generative AI on Software Development")
        submitted = st.form_submit_button("✨ Generate Content")

    if submitted:
        if not topic:
            st.error("Please enter a topic.")
        else:
            with st.spinner("🤖 Agents are working... Planning, writing, and editing content..."):
                try:
                    inputs = {'topic': topic}
                    crew = ContentCreationCrew()
                    result = crew.kickoff(inputs=inputs)
                    st.success("✅ Content Generation Completed!")
                    st.markdown("### 📝 Final Draft")
                    st.markdown(result)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

elif crew_selection == "Customer Support Hub":
    st.title("🛠️ Customer Support Hub")
    st.markdown("### Deliver exceptional support with AI precision")
    st.markdown("Draft comprehensive, empathetic, and accurate responses to complex customer inquiries.")
    st.markdown("---")

    with st.form("support_form"):
        col1, col2 = st.columns(2)
        with col1:
            customer = st.text_input("Customer / Company Name", placeholder="e.g., Acme Corp")
        with col2:
            person = st.text_input("Contact Person", placeholder="e.g., Jane Doe")
            
        inquiry = st.text_area("Customer Inquiry", placeholder="Paste the full text of the customer's email or message here...", height=150)
        
        submitted = st.form_submit_button("📨 Draft Response")

    if submitted:
        if not customer or not person or not inquiry:
            st.error("Please fill in all required fields.")
        else:
            with st.spinner("🤖 Agents are working... Researching and drafting response..."):
                try:
                    inputs = {
                        'customer': customer,
                        'person': person,
                        'inquiry': inquiry
                    }
                    crew = SupportCrew()
                    result = crew.kickoff(inputs=inputs)
                    st.success("✅ Response Drafted Successfully!")
                    st.markdown("### 📧 Proposed Response")
                    st.markdown(result)
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
