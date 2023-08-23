<<<<<<< HEAD
import json
import openai
import random
from token_counter import num_tokens_from_messages

def clean_text(prompt):
    pass


def remove_randomly(prompt, t):
    # Check if the input prompt is already shorter than the desired length
    if len(prompt) <= 2048:
        return prompt

    # Convert the prompt to a list of characters for easy manipulation
    prompt_list = list(prompt)

    # Repeat the removal process t times
    for i in range(t):
        if len(prompt_list) <= 2048:
            break  # Stop if the prompt is already at or below 2048 characters
        # Generate a random index to remove a character
        index_to_remove = random.randint(0, len(prompt_list) - 1)
        # Remove the character at the random index
        prompt_list.pop(index_to_remove)

    # Convert the list back to a string
    result = ''.join(prompt_list)
    
    return result

def generate_interview_questions(candidate_profile, job_description):
    # Load the OpenAI API key from a JSON file
    with open('config.json') as f:
        config = json.load(f)
        openai.api_key = config["OPENAI_API_KEY"]

    # Customize the prompt for interview question generation
    prompt = f"Generate 5 interview question for a candidate with the following profile based on the job decription. Ask basic questions to understand the candidate and their experience level:\nCandidate Profile: {candidate_profile}\nJob Description: {job_description}\nQuestions:"
    print(len(prompt)/5)    
    messages=[
            {
                "role":"user",
                "content": prompt
            },
        ]
    t = num_tokens_from_messages(messages, 'gpt-3.5-turbo-0613')
    print(f"{t} prompt tokens counted by num_tokens_from_messages().")
    if t>2048:
        prompt = remove_randomly(prompt, t)
    messages=[
            {
                "role":"user",
                "content": prompt
            },
        ]
    # Use GPT-3.5 to generate interview questions
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",  # You can use other GPT-3 models too
        messages=[
            {
                "role":"user",
                "content": prompt
            },
        ],
        temperature=0.1,
        max_tokens=4096-t,
        stop=None  # Let the model generate until the specified max tokens
    )

    
    # Extract and return the generated questions
    #generated_questions = response.choices[0].text.strip()
    generated_questions = response['choices'][0]['message']['content'].strip()
=======
import json
import openai
import random
from token_counter import num_tokens_from_messages

def clean_text(prompt):
    pass


def remove_randomly(prompt, t):
    # Check if the input prompt is already shorter than the desired length
    if len(prompt) <= 2048:
        return prompt

    # Convert the prompt to a list of characters for easy manipulation
    prompt_list = list(prompt)

    # Repeat the removal process t times
    for i in range(t):
        if len(prompt_list) <= 2048:
            break  # Stop if the prompt is already at or below 2048 characters
        # Generate a random index to remove a character
        index_to_remove = random.randint(0, len(prompt_list) - 1)
        # Remove the character at the random index
        prompt_list.pop(index_to_remove)

    # Convert the list back to a string
    result = ''.join(prompt_list)
    
    return result

def generate_interview_questions(candidate_profile, job_description):
    # Load the OpenAI API key from a JSON file
    with open('config.json') as f:
        config = json.load(f)
        openai.api_key = config["OPENAI_API_KEY"]

    # Customize the prompt for interview question generation
    prompt = f"Generate 5 interview question for a candidate with the following profile based on the job decription. Ask basic questions to understand the candidate and their experience level:\nCandidate Profile: {candidate_profile}\nJob Description: {job_description}\nQuestions:"
    print(len(prompt)/5)    
    messages=[
            {
                "role":"user",
                "content": prompt
            },
        ]
    t = num_tokens_from_messages(messages, 'gpt-3.5-turbo-0613')
    print(f"{t} prompt tokens counted by num_tokens_from_messages().")
    if t>2048:
        prompt = remove_randomly(prompt, t)
    messages=[
            {
                "role":"user",
                "content": prompt
            },
        ]
    # Use GPT-3.5 to generate interview questions
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",  # You can use other GPT-3 models too
        messages=[
            {
                "role":"user",
                "content": prompt
            },
        ],
        temperature=0.1,
        max_tokens=4096-t,
        stop=None  # Let the model generate until the specified max tokens
    )

    
    # Extract and return the generated questions
    #generated_questions = response.choices[0].text.strip()
    generated_questions = response['choices'][0]['message']['content'].strip()
>>>>>>> b6fc4fd756b59f698b9ba36ea36750d87054a22c
    return generated_questions