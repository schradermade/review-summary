from openai import OpenAI
import os
from dotenv import load_dotenv

client = OpenAI()
load_dotenv()


# Set your API key
client.api_key = os.getenv('OPENAI_KEY');

def generate_fake_reviews():
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Write 10 positive reviews for a wireless headphone. Each review should be unique and detailed. put the reviews in JSON format"}
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    review = response.choices[0].message.content.strip()
    return review

# Generate and print a fake review
fake_review = generate_fake_reviews()
print(fake_review)
