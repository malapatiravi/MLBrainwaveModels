OBJS = extract.o fileHelp.o missingValues.o
CC = g++
CFLAGS = -Wall -std=c++11 -c $(DEBUG)
LFLAGS = -Wall $(DEBUG)


fileHelp.o: fileHelp.h
	$(CC) $(CFLAGS) fileHelp.cpp
extract.o: extract.h fileHelp.h fileHelp.cpp
	$(CC) $(CFLAGS) extract.cpp
missingValues.o: missingValues.h extract.cpp fileHelp.h fileHelp.cpp
	$(CC) $(CFLAGS) missingValues.cpp


ppp: $(OBJS)
	$(CC)  $(LFLAGS) $(OBJS) -o ppp

clear:
	\rm *.o *~ppp
tar:
	tar cfv p1.tar extract.cpp fileHelp.h fileHelp.cpp missingValues.h missingValues.cpp



