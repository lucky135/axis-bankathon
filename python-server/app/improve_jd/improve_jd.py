import openai
import os
from dotenv import load_dotenv

load_dotenv()

class ImproveJobDescription():
    def __init__(self) -> None:
        openai.api_key = os.getenv("OPENAI_KEY")

    def clean_response(self, response):
        cleaned_response = response.replace('\n', '').replace('\"', '"')
        print(f'Cleaned response: {cleaned_response}')
        return cleaned_response

    def improveJobDescription(self, prompt, request_id):
        response = openai.ChatCompletion.create(
            model="gpt-4",  
            messages=[
                {
                    'role': 'system',
                    'content': f'my JD is {prompt} and request id is {request_id}. I am trying to provide recommendations to change the Job description, {{"request_id": {request_id}, "score": "score of previous JD", "enhanced_jd": "from the given JD enhance paragraph and maintain the same format as previous JD", "enhanced_score": "score of enhanced JD", "similarity_percentage": "similarity score between old and enhanced JD out of 100%"}} in enhanced JD make sure to add complete previous JD with enhancement. just give output in this form do not give any explanation in output'
                }
            ]
        )
        return response['choices'][0]['message']['content']