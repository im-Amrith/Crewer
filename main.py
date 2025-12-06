import sys
import os

# Add the current directory to sys.path to ensure imports work correctly
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.crews.job_search.job_search_crew import JobSearchCrew
from src.crews.content_creation.content_crew import ContentCreationCrew
from src.crews.support.support_crew import SupportCrew

def main():
    print("Welcome to the CrewAI Production App!")
    print("Please select a crew to run:")
    print("1. Job Search Crew")
    print("2. Content Creation Crew")
    print("3. Support Crew")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        print("\n--- Job Search Crew ---")
        job_posting_url = input("Enter job posting URL: ")
        github_url = input("Enter GitHub URL: ")
        linkedin_url = input("Enter LinkedIn URL: ")
        personal_writeup = input("Enter a short personal writeup: ")
        
        inputs = {
            'job_posting_url': job_posting_url,
            'github_url': github_url,
            'linkedin_url': linkedin_url,
            'personal_writeup': personal_writeup
        }
        
        crew = JobSearchCrew()
        result = crew.kickoff(inputs=inputs)
        print("\n\n########################")
        print("## Here is the result ##")
        print("########################\n")
        print(result)
        
    elif choice == '2':
        print("\n--- Content Creation Crew ---")
        topic = input("Enter the topic for the content: ")
        
        inputs = {
            'topic': topic
        }
        
        crew = ContentCreationCrew()
        result = crew.kickoff(inputs=inputs)
        print("\n\n########################")
        print("## Here is the result ##")
        print("########################\n")
        print(result)
        
    elif choice == '3':
        print("\n--- Support Crew ---")
        customer = input("Enter customer name: ")
        person = input("Enter person name: ")
        inquiry = input("Enter the inquiry: ")
        
        inputs = {
            'customer': customer,
            'person': person,
            'inquiry': inquiry
        }
        
        crew = SupportCrew()
        result = crew.kickoff(inputs=inputs)
        print("\n\n########################")
        print("## Here is the result ##")
        print("########################\n")
        print(result)
        
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
