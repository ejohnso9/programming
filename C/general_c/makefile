CXX = g++
# NB: in general gcc and g++ are *NOT* interchangeable
CXXFLAGS = -Wall -std=c++14 


# hello  (test program)
hello: hello.o
	$(CXX) $(CXXFLAGS) -o hello hello.o

hello.o: hello.cpp
	$(CXX) $(CXXFLAGS) -c hello.cpp

# ej.cpp
ej: ej.o
	$(CXX) $(CXXFLAGS) -o ej ej.o

ej.o: ej.cpp
	$(CXX) $(CXXFLAGS) -c ej.cpp

# applies to all
clean:
	rm -f hello ej *.o
