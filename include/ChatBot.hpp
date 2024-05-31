/*
** EPITECH PROJECT, 2024
** Hackaton
** File description:
** ChatBot
*/

#pragma once

#include <string>
#include <unordered_map>

class ChatBot {
    public:
        ChatBot();
        ~ChatBot();
        std::string getResponse(const std::string& question);
        void run(ChatBot bot);
    private:
        std::unordered_map<std::string, std::string> faq;

};
