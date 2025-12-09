all: 
	g++ -std=c++11 -O3 -Wall p.cpp -lm

s:
	g++ -std=c++11 -O3 -Wall -fsanitize=address p.cpp -lm

dlg:
	g++ -std=c++11 -O3 -Wall -o dlg delaunay2graph.cpp -lm

run:
	./a.out

clean:
	rm -f *.o p
