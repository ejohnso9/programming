CXX = g++
CXXFLAGS = -Wall -std=c++14 


# hello
hello: hello.o
	$(CXX) $(CXXFLAGS) -o hello hello.o

hello.o: hello.cpp
	$(CXX) $(CXXFLAGS) -c hello.cpp


# hello2
hello2: hello2.o
	$(CXX) $(CXXFLAGS) -o hello2 hello2.o

hello2.o: hello2.cpp
	$(CXX) $(CXXFLAGS) -c hello2.cpp


# example2
example2: example2.o
	$(CXX) $(CXXFLAGS) -o example2 example2.o

example2.o: example2.cpp
	$(CXX) $(CXXFLAGS) -c example2.cpp


# applies to all
clean:
	rm -f hello hello2 example2 *.o
