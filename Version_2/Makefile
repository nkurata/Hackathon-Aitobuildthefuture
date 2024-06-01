##
## EPITECH PROJECT, 2024
## Hackaton
## File description:
## Makefile
##

CC		= 	g++

SRC		=	src/main.cpp		\

BINARY	=	ChatBot

OBJ		=	$(SRC:.cpp=.o)

CPPFLAGS	= 	-std=c++20 -Wall -Wextra -I include

LIBS		=	-lcpr -lpthread

all:	$(BINARY)

$(BINARY):$(OBJ)
	$(CC) $(OBJ) -o $(BINARY) $(CPPFLAGS) $(LIBS)

clean:
	rm -f $(OBJ)

fclean:	clean
	rm -f $(BINARY)

re:	fclean all

.PHONY: all clean fclean re
