import random
import requests

def get_chatgpt_response(prompt):
    api_url = "https://api.openai.com/v1/chat/completions"  # Update with the correct API endpoint

    # Set up your OpenAI API key
    api_key = "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"  # Replace with your actual API key

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "system", "content": "Imagine you're a game trying to teach an english speaker basic phrases of a new language."},
                     {"role": "user", "content": prompt}]
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

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
    return ["Generate a pixelart image of a " + settings[setting_idx] + " with a " + ethnicities[ethnicity_idx] + " " + occupations[setting_idx][character_idx], "This is very important, pay attention to every sentence. Generate a python list of 3 basic questions that a " + ethnicities[ethnicity_idx] + " " + occupations[setting_idx][character_idx] + " would likely ask in that order at a " + settings[setting_idx] + ".  Only return the python list and no added text, and their english translations in brackets in the same string as the question."]


# Ask GPT if the answer is in English or not. Could ask like f"Is this phrase {answer} in English or another language? Only answer yes or no, that's it". If it isn't:

#Template for question rating: f"Imagine you're a game trying to teach an english speaker basic phrases of a new language, {language}.Given the question {question}, do you think {answer} is a relevant and understandable answer? Give the answer a rating out of 10, keeping in mind they're a basic speaker of the language, and shouldn't yet know the intricacies of or how to formulate complex sentences of the language. 
# Phrase the answer in a way such that it sounds like a {language} speaking {occupation} character is replying to the answer at a Bus Stop, and giving constructive criticism to someone who is clearly new to {language}."


#If it is:

#f"Imagine you're a game trying to teach an english speaker basic phrases of a new language, {language}. Given the question {question}, the player answered {answer}. Give advice to someone who is clearly new to {language} on how you would phrase their answer in {language}, imagining that you're the {language} speaking {occupation} who asked the initial question. Answer in English, and exclude any unnecessary text"

#  Tutorial: Choose language. Could have an input box saying "What language would you like to learn tdoay?"