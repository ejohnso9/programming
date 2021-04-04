
all: nasty.o
	g++ nasty.o -o nasty

nasty.o: nasty.cpp
	g++ -c nasty.cpp

clean: 
	rm nasty *.o

test:
	./nasty < 1.in
