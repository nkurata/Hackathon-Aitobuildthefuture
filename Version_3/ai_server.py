##
## EPITECH PROJECT, 2024
## Version_2
## File description:
## ai_server
##

import openai

openai.api_key = "OUR_API_KEY"

def ChatBot(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message['content'].strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        response = ChatBot(user_input)
        print("ChatBot: ", response)
