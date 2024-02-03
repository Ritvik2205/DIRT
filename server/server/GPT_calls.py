import requests
import string

def get_chatgpt_response(prompt, gpt_character):
    api_url = "https://api.openai.com/v1/chat/completions"


    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "system", "content": gpt_character},
                     {"role": "user", "content": prompt}]
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None
    
    

def rate_answer(question, answer, setting, language, occupation,):
    
    # if check_english(answer):
    #     prompt = f"Imagine you're a game trying to teach an english speaker basic phrases of a new language, {language}. Given the question {question}, the player answered {answer}. Give advice to someone who is clearly new to {language} on how you would phrase their answer in {language}, imagining that you're the {language} speaking {occupation} who asked the initial question. Answer in English, and exclude any unnecessary text"
    # else:
    prompt = f"The language you're trying to teach is {language}.Given the question {question}, do you think {answer} is a relevant and understandable answer? Give the answer a rating out of 10, keeping in mind they're a basic speaker of the language, and shouldn't yet know the intricacies of or how to formulate complex sentences of the language. Phrase the answer in a way such that it sounds like a {language} {occupation} character who's speaking mainly English is replying to the answer at a {setting}, and giving constructive criticism to someone who is clearly new to {language}."
    
    gpt_character = "You're a game trying to teach an english speaker basic phrases of a new language"
    
    return get_chatgpt_response(prompt, gpt_character)


# def check_english(answer):
#     prompt = f"Is this phrase {answer} in English or another language? Only answer 'yes' or 'no', that's it, no grammar or extra characters, just yes or no"
#     gpt_character = "Helpful assistant"
    
#     is_english = get_chatgpt_response(prompt, gpt_character).upper()
#     translator = str.maketrans("", "", string.punctuation)
#     is_english = is_english.translate(translator)
#     print("is english: " + is_english)
#     if is_english == "YES":
#         return True
#     return False


response = rate_answer("Quel est votre arrêt? (What is your stop?)", "le centre ville", "Bus Stop", "French", "Bus Driver")
print(response)