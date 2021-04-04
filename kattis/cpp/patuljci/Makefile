
main: main.o
	g++ main.o -o main

main.o: main.cpp
	g++ -c main.cpp

clean: 
	rm main *.o

test:
	./main < test1.txt
	./main < test2.txt
