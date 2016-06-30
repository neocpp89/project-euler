SOURCES=$(wildcard *.c*)
BINARIES=$(foreach x, $(basename $(SOURCES)), $(x))
CFLAGS += -g -Wall -Wextra -O3 -march=native -std=c99
CXXFLAGS += -g -Wall -Wextra -O3 -march=native -std=c++11

.PHONY: all clean
all: $(BINARIES)

clean:
	-rm $(BINARIES)

%: %.c
	$(CC) $(CFLAGS) -o $@ $< -lm

%: %.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<

