import random
import requests

# Set up your OpenAI API key
# Replace with your actual API key
API_KEY = "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"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}",
}


def get_chatgpt_response(prompt):
    # Update with the correct API endpoint
    api_url = "https://api.openai.com/v1/chat/completions"

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "system", "content": "You are a helpful assistant."},
                     {"role": "user", "content": prompt}]
    }

    response = requests.post(api_url, json=data, headers=HEADERS)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None


def get_image_response(prompt):
    # Update with the correct API endpoint
    api_url = "https://api.openai.com/v1/images/generations"

    data = {
        "model": "dall-e-3",
        "prompt": prompt
    }

    response = requests.post(api_url, json=data, headers=HEADERS)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

# Example usage


ethnicities = [
    "Spanish", "German", "French", "Italian"
]

settings = [
    "Bus Stop",
    "Local Coffee Shop",
    "Community Park",
    "Grocery Store",
    "Public Library",
    "Fitness Center",
    "Farmers' Market",
    "Neighborhood Playground",
    "Local Church or Place of Worship"
]

occupations = [
    ["Bus driver", "Commuter", "Student", "Office worker"],
    ["Barista", "Student", "Freelancer", "Business professional"],
    ["Dog walker", "Jogger", "Parent", "Retiree"],
    ["Cashier", "Stock clerk", "Shopper", "Nutritionist"],
    ["Librarian", "Student", "Researcher", "Writer"],
    ["Personal trainer", "Gym-goer", "Fitness instructor"],
    ["Farmer", "Vendor", "Shopper", "Chef"],
    ["Parent", "Child", "Nanny", "Retiree"],
    ["Religious leader", "Worshipper", "Volunteer"]
]


def image_prompt_generator(setting_idx, ethnicity_idx):
    character_idx = random.randint(0, len(occupations[setting_idx]) - 1)
    return ["Generate a pixelart image of a " + settings[setting_idx] + " with a " + ethnicities[ethnicity_idx] + " " + occupations[setting_idx][character_idx], "This is very important, pay attention to every sentence. Imagine you're a game trying to teach an english speaker basic phrases of a new language. Generate a python list of 3 basic questions that a " + ethnicities[ethnicity_idx] + " " + occupations[setting_idx][character_idx] + " would likely ask in that order at a " + settings[setting_idx] + ". Have no extra text at the start or bottom not related to the questions, and their english translations in brackets in the same string as the question."]


import re

def extract_inner_strings(input_string):
    pattern = r'"([^"]*)"'
    inner_strings = re.findall(pattern, input_string)
    return inner_strings