import curses

text = """Hello world!
This is a tiny text editor.
Edit me!"""

cursor = 0
display = "|"+text


def draw(screen):
    screen.clear()
    global cursor, display

    # ==========================================================
    # INITIALIZE THE DISPLAY
    #
    # Display the document with the cursor at the current
    # cursor position.
    #
    # Example
    #
    # text    = "Hello"
    # cursor  = 0
    #
    # display = "|Hello"
    #
    # ---------------- TODO ----------------

    # ----------------------------------------

    for row, line in enumerate(display.split("\n")):
        screen.addstr(row, 0, line)

    screen.addstr(
        len(display.split("\n")) + 1,
        0,
        "← → Move   Type Insert   Backspace Delete   Enter New Line   Esc Quit"
    )

    screen.refresh()


def main(screen):
    global text, cursor, display

    cursor = 0

    while True:
        draw(screen)
        key = screen.getch()

        if key == 27:
            break

        # ==========================================================
        # LEFT ARROW
        #
        # Move the cursor one position to the left.
        #
        # Example
        #
        # Before
        # text    = "Hello"
        # cursor  = 3
        # display = "Hel|lo"
        #
        # After
        # text    = "Hello"
        # cursor  = 2
        # display = "He|llo"
        #
        # ---------------- ANSWER ----------------

        elif key == curses.KEY_LEFT:
            if (cursor > 0):
                display = display[:cursor-1] + "|" + display[cursor-1] + display[cursor+1:]
                cursor -= 1

        # ----------------------------------------

        # ==========================================================
        # RIGHT ARROW
        #
        # Move the cursor one position to the right.
        #
        # Example
        #
        # Before
        # text    = "Hello"
        # cursor  = 3
        # display = "Hel|lo"
        #
        # After
        # text    = "Hello"
        # cursor  = 4
        # display = "Hell|o"
        #
        # ---------------- ANSWER ----------------

        elif key == curses.KEY_RIGHT:
            if (cursor < len(display)-1):
                display = display[:cursor] + display[cursor+1] + "|" + display[cursor+2:]
                cursor += 1
        # ----------------------------------------

        # ==========================================================
        # BACKSPACE
        #
        # Delete the character immediately before the cursor.
        #
        # Example
        #
        # Before
        # text    = "Hello"
        # cursor  = 3
        # display = "Hel|lo"
        #
        # After
        # text    = "Helo"
        # cursor  = 2
        # display = "He|lo"
        #
        # ---------------- ANSWER ----------------

        elif key in (8, 127, curses.KEY_BACKSPACE):
            if (cursor != 0):
                display = display[0:cursor-1] + "|" + display[cursor+1:]
                cursor -= 1

        # ----------------------------------------

        # ==========================================================
        # ENTER
        #
        # Insert a newline at the cursor.
        #
        # Example
        #
        # Before
        # text    = "Hello"
        # cursor  = 3
        # display = "Hel|lo"
        #
        # After
        # text    = "Hel\nlo"
        # cursor  = 4
        # display = "Hel\n|lo"
        #
        # ---------------- ANSWER ----------------

        elif key == 10:
            cursor = display.index("|")
            display = display[0:cursor] + "\n|" + display[cursor+1:]
            cursor += 2

        # ----------------------------------------

        # ==========================================================
        # INSERT CHARACTER
        #
        # Insert the typed character at the cursor.
        #
        # Example
        #
        # Before
        # text    = "Hello"
        # cursor  = 3
        # display = "Hel|lo"
        #
        # Typing X
        #
        # After
        # text    = "HelXlo"
        # cursor  = 4
        # display = "HelX|lo"
        #
        # ---------------- ANSWER ----------------

        elif 32 <= key <= 126:
            display = display[:cursor] + chr(key) + "|" + display[cursor+1:]
            cursor += 1

        # ----------------------------------------

        #BONUS: Can you figure out how to select one line up/down by yourself?

        elif key == curses.KEY_UP:
            ls = display.split("\n")
            if ("|" in ls[0]): continue


            for i in range(1, len(ls)):
                if ("|" in ls[i]):
                    row = i
                    break
            ind = ls[row].index("|")

            ls[row] = ls[row][:ind] + ls[row][ind+1:]
            if (ind > len(ls[row-1])-1): ind = len(ls[row-1]) - 1
            ls[row-1] = ls[row-1][:ind] + "|" + ls[row-1][ind:]

            display = "\n".join(ls)
            cursor = display.index("|")

        elif key == curses.KEY_DOWN:
            ls = display.split("\n")
            if ("|" in ls[-1]): continue

            for i in range(0, len(ls)-1):
                if ("|" in ls[i]):
                    row = i
                    break
            ind = ls[row].index("|")

            ls[row] = ls[row][:ind] + ls[row][ind+1:]
            if (ind > len(ls[row+1])-1): ind = len(ls[row+1]) - 1
            ls[row+1] = ls[row+1][:ind] + "|" + ls[row+1][ind:]

            display = "\n".join(ls)
            cursor = display.index("|")

curses.wrapper(main)
