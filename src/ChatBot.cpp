/*
** EPITECH PROJECT, 2024
** Hackaton
** File description:
** ChatBot
*/

#include "ChatBot.hpp"
#include <iostream>

ChatBot::ChatBot() {
    faq["What are your hours of operation?"] = "We are open from 9 AM to 5 PM, Monday to Friday.";
    faq["Where are you located?"] = "We are located at 123 Main Street, Anytown, USA.";
    faq["How can I contact customer support?"] = "You can contact us at support@example.com or call us at (555) 123-4567.";
}

std::string ChatBot::getResponse(const std::string& question)
{
    auto it = faq.find(question);
    if (it != faq.end()) {
        return it->second;
    } else {
        return "Sorry, I didn't understand the question.";
    }
}

void ChatBot::run(ChatBot bot)
{
    std::string query;
    std::cout << "Welcome to ChatBot! Type your question below or type 'exit' to quit." << std::endl;
    while (true) {
        std::cout << "You: ";
        std::getline(std::cin, query);

        if (query == "exit") {
            break;
        }
        std::string response = bot.getResponse(query);
        std::cout << "Bot: " << response << std::endl;
    }
}

ChatBot::~ChatBot() {}
