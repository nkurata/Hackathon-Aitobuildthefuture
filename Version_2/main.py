##
## EPITECH PROJECT, 2024
## Hackathon-Aitobuildthefuture
## File description:
## main
##

import json
from difflib import get_close_matches

def load_database(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_database(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent = 2)

def find_best_answer(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n = 1, cutoff = 0.6)
    return matches[0] if matches else None

def get_answer(question: str, database: dict) -> str | None:
    for q in database["questions"]:
        if q["question"] == question:
            return q["answer"]

def ChatBot():
    database: dict = load_database('database.json')
    while True:
        user_input: str = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break

        best_answer: str | None = find_best_answer(user_input, [q["question"] for q in database["questions"]])
        if best_answer:
            answer: str = get_answer(best_answer, database)
            print (f"Bot: {answer}")
        else:
            print("Bot: I don't know that, can you tell me the answer so I'll be able to response next time !")
            new_answer: str = input("Type the answer or 'skip' to skip: ")
            if new_answer.lower() != 'skip':
                database["questions"].append({"question": user_input, "answer": new_answer})
                save_database("database.json", database)
                print("Bot: Thanks! I got better thanks to you!")

if __name__ == "__main__":
    ChatBot()