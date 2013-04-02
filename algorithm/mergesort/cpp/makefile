CC=g++
CFLAGS=-c

all: test

test: test.o ms.o arrayPrinter.o rlist.o sizeReader.o msPrinty.o
	$(CC) test.o ms.o arrayPrinter.o rlist.o sizeReader.o msPrinty.o -o test

test.o: test.cpp
	$(CC) $(CFLAGS) test.cpp

ms.o: ms.cpp
	$(CC) $(CFLAGS) ms.cpp

rlist.o: rlist.cpp
	$(CC) $(CFLAGS) rlist.cpp

arrayPrinter.o:	arrayPrinter.cpp
	$(CC) $(CFLAGS) arrayPrinter.cpp

sizeReader.o: sizeReader.cpp
	$(CC) $(CFLAGS) sizeReader.cpp

msPrinty.o: msPrinty.cpp arrayPrinter.h
	$(CC) $(CFLAGS) msPrinty.cpp

clean:
	rm *.o test ../lists-cpp.txt

rmo:
	rm *.o
