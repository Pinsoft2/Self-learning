filter:
	clang -ggdb3 -gdwarf-4 -O0 -Qunused-arguments -std=c11 -Wall -Werror -Wextra -Wno-gnu-folding-constant -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow -lm -o filter filter.c helpers.c


# CC = clang
# CFLAGS = -ggdb3 -gdwarf-4 -O0 -Qunused-arguments -std=c11 -Wall -Werror -Wextra -Wno-gnu-folding-constant -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow
# LDFLAGS = -lm

# filter: filter.o helpers.o
# 	$(CC) $(CFLAGS) -o filter filter.o helpers.o $(LDFLAGS)

# filter.o: filter.c helpers.h
# 	$(CC) $(CFLAGS) -c filter.c

# helpers.o: helpers.c helpers.h
# 	$(CC) $(CFLAGS) -c helpers.c

# clean:
# 	rm -f filter *.o

# .PHONY: clean