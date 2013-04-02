# compiler
CC = gcc

# linker
LD = gcc

# compiler flags
CFLAGS = -Wno-deprecated  -c

# linker flags
LDFLAGS =

# used to clean
RM = /bin/rm -f

#program file name
PROG = qgame

SOURCE = model/Model.c model/Board.c model/Loc.c model/Player.c control/Control.c view/Display.c qgame.c
#SOURCE = src/model/*.c src/control/*.c src/view/*.c src/*.c
OBJS = $(SOURCE:.c=.o)

# to compile everything
all: $(SOURCE) $(PROG)

# linking the program
$(PROG): $(OBJS)
	$(LD) $(OBJS) $(LDFLAGS) -o $(PROG)

.c.o:
	$(CC) $(CFLAGS) $< -o $@

# cleanup
clean:
	$(RM) $(PROG) $(OBJS)
