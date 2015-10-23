# Project: dlx
CC = gcc
BIN = dlx
CFLAGS = -O3 -Wall -std=c99 -march=native -g

SRC = \
    main.c \
    dlx.c \

OBJ = $(patsubst %.c, %.o, $(SRC))

.PHONY: clean

all: $(BIN)

clean:
	rm $(BIN) $(OBJ)

$(BIN): $(OBJ)
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $^
