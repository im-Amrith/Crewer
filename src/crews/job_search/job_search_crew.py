import os
from crewai import Agent, Task, Crew
from crewai_tools import (
  FileReadTool,
  ScrapeWebsiteTool,
  MDXSearchTool,
  SerperDevTool
)
from src.utils import get_gemini_llm, get_serper_api_key

class JobSearchCrew:
    def __init__(self):
        self.llm = get_gemini_llm()
        os.environ["SERPER_API_KEY"] = get_serper_api_key()
        
        # Initialize Tools
        self.search_tool = SerperDevTool()
        self.scrape_tool = ScrapeWebsiteTool()
        self.read_resume = FileReadTool(file_path='./data/fake_resume.md')
        self.semantic_search_resume = MDXSearchTool(mdx='./data/fake_resume.md')

    def run(self):
        # Agent 1: Researcher
        researcher = Agent(
            role="Tech Job Researcher",
            goal="Make sure to do amazing analysis on "
                 "job posting to help job applicants",
            tools = [self.scrape_tool, self.search_tool],
            verbose=True,
            backstory=(
                "As a Job Researcher, your prowess in "
                "navigating and extracting critical "
                "information from job postings is unmatched."
                "Your skills help pinpoint the necessary "
                "qualifications and skills sought "
                "by employers, forming the foundation for "
                "effective application tailoring."
            ),
            llm=self.llm
        )

        # Agent 2: Profiler
        profiler = Agent(
            role="Personal Profiler for Engineers",
            goal="Do increditble research on job applicants "
                 "to help them stand out in the job market",
            tools = [self.scrape_tool, self.search_tool,
                     self.read_resume, self.semantic_search_resume],
            verbose=True,
            backstory=(
                "Equipped with analytical prowess, you dissect "
                "and synthesize information "
                "from diverse sources to craft comprehensive "
                "personal and professional profiles, laying the "
                "groundwork for personalized resume enhancements."
            ),
            llm=self.llm
        )

        # Agent 3: Resume Strategist
        resume_strategist = Agent(
            role="Resume Strategist for Engineers",
            goal="Find all the best ways to make a "
                 "resume stand out in the job market.",
            tools = [self.scrape_tool, self.search_tool,
                     self.read_resume, self.semantic_search_resume],
            verbose=True,
            backstory=(
                "With a strategic mind and an eye for detail, you "
                "excel at refining resumes to highlight the most "
                "relevant skills and experiences, ensuring they "
                "resonate perfectly with the job's requirements."
            ),
            llm=self.llm
        )

        # Agent 4: Interview Preparer
        interview_preparer = Agent(
            role="Engineering Interview Preparer",
            goal="Create interview questions and talking points "
                 "based on the resume and job requirements",
            tools = [self.scrape_tool, self.search_tool,
                     self.read_resume, self.semantic_search_resume],
            verbose=True,
            backstory=(
                "Your role is crucial in anticipating the dynamics of "
                "interviews. With your ability to formulate key questions "
                "and talking points, you prepare candidates for success, "
                "ensuring they can confidently address all aspects of the "
                "job they are applying for."
            ),
            llm=self.llm
        )

        # Tasks
        research_task = Task(
            description=(
                "Analyze the job posting URL provided ({job_posting_url}) "
                "to extract key skills, experiences, and qualifications "
                "required. Use the tools to gather content and identify "
                "and categorize the requirements."
            ),
            expected_output=(
                "A structured list of job requirements, including necessary "
                "skills, qualifications, and experiences."
            ),
            agent=researcher,
            async_execution=True
        )

        profile_task = Task(
            description=(
                "Compile a detailed personal and professional profile "
                "using the GitHub ({github_url}) and LinkedIn ({linkedin_url}) URLs, "
                "and personal write-up ({personal_writeup}). Utilize tools to extract and "
                "synthesize information from these sources."
            ),
            expected_output=(
                "A comprehensive profile document that includes skills, "
                "project experiences, contributions, interests, and "
                "communication style."
            ),
            agent=profiler,
            async_execution=True
        )

        resume_strategy_task = Task(
            description=(
                "Using the profile and job requirements obtained from "
                "previous tasks, tailor the resume to highlight the most "
                "relevant areas. Employ tools to adjust and enhance the "
                "resume content. Make sure this is the best resume even but "
                "don't make up any information. Update every section, "
                "inlcuding the initial summary, work experience, skills, "
                "and education. All to better reflrect the candidates "
                "abilities and how it matches the job posting."
            ),
            expected_output=(
                "An updated resume that effectively highlights the candidate's "
                "qualifications and experiences relevant to the job."
            ),
            output_file="tailored_resume.md",
            context=[research_task, profile_task],
            agent=resume_strategist
        )

        interview_preparation_task = Task(
            description=(
                "Create a set of potential interview questions and talking "
                "points based on the tailored resume and job requirements. "
                "Utilize tools to generate relevant questions and discussion "
                "points. Make sure to use these question and talking points to "
                "help the candiadte highlight the main points of the resume "
                "and how it matches the job posting."
            ),
            expected_output=(
                "A document containing key questions and talking points "
                "that the candidate should prepare for the initial interview."
            ),
            output_file="interview_materials.md",
            context=[research_task, profile_task, resume_strategy_task],
            agent=interview_preparer
        )

        job_application_crew = Crew(
            agents=[researcher, profiler, resume_strategist, interview_preparer],
            tasks=[research_task, profile_task, resume_strategy_task, interview_preparation_task],
            verbose=True
        )

        return job_application_crew

    def kickoff(self, inputs):
        crew = self.run()
        return crew.kickoff(inputs=inputs)
