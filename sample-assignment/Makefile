PROGRAM = stack-prog

all: $(PROGRAM)
	
$(PROGRAM): stack-driver.cc stack.h
	g++ -Wall -o $@ $<

.PHONY: clean
clean:
	rm -f *.o $(PROGRAM)
