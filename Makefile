.PHONY: all clean
CC=clang
CPP=clang++
AR=ar
RANLIB=ranlib
CFLAGS= -g -Wall -Wno-unused-function -O3
C11FLAGS= -g -Wall -Wno-unused-function -std=c++11
SRCDIR = ./src
INCLUDEDIR = -I./include -I.
DEPS = 
LIBS = -lm

PROGRAMS =  radix_sort_demo \
       		quick_sort_demo \
			bubble_sort_demo \
			prime_demo \
			prime_custom_demo

all: $(PROGRAMS)

radix_sort_demo: $(SRCDIR)/radix_sort_demo.cpp
	$(CPP) $(CFLAGS) -o $@ $^ $(INCLUDEDIR) $(LIBS)

quick_sort_demo: $(SRCDIR)/quick_sort_demo.cpp
	$(CPP) $(CFLAGS) -o $@ $^ $(INCLUDEDIR) $(LIBS)

bubble_sort_demo: $(SRCDIR)/bubble_sort_demo.cpp
	$(CPP) $(CFLAGS) -o $@ $^ $(INCLUDEDIR) $(LIBS)

prime_demo: $(SRCDIR)/prime_demo.cpp
	$(CPP) $(CFLAGS) -o $@ $^ $(INCLUDEDIR) $(LIBS)

prime_custom_demo: $(SRCDIR)/prime_custom_demo.cpp
	$(CPP) $(CFLAGS) -o $@ $^ $(INCLUDEDIR) $(LIBS)

clean:
	rm -rf $(PROGRAMS) *.dSYM *.o

