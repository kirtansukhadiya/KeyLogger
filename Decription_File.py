print("This is the decription file")

  # Read a single line
#Data_Encripted = open("received_Decripted_file.txt", 'w')

def process_line(line):
    result = []
    buffer = ""
    inside_brackets = False
    
    for char in line:
        if char == '[':
            inside_brackets = True
            buffer += char
        elif char == ']':
            inside_brackets = False
            buffer += char
            result.append(buffer)  # Add the entire bracketed content
            buffer = ""  # Clear the buffer
        elif inside_brackets:
            buffer += char  # Keep adding chars to buffer if inside brackets
        else:
            if char == 'e':
                print("running")
                result.append('A')
            elif char == '5':
                result.append('B')
            elif char == 'r':
                result.append('C')
            elif char == 'l':
                result.append('D')
            elif char == 'g':
                result.append('E')
            elif char == 'q':
                result.append('F')
            elif char == 'v':
                result.append('G')
            elif char == 'M':
                result.append('H')
            elif char == 'Y':
                result.append('I')
            elif char == 'B':
                result.append('J')
            elif char == 'K':
                result.append('K')
            elif char == 'I':
                result.append('L')
            elif char == '5':
                result.append('M')
            elif char == 'C':
                result.append('N')
            elif char == 'o':
                result.append('O')
            elif char == '1':
                result.append('P')
            elif char == 't':
                result.append('Q')
            elif char == 'n':
                result.append('R')
            elif char == 'i':
                result.append('S')
            elif char == 'T':
                result.append('T')
            elif char == 'f':
                result.append('U')
            elif char == 'j':
                result.append('V')
            elif char == 'W':
                result.append('W')
            elif char == '7':
                result.append('X')
            elif char == 'c':
                result.append('Y')
            elif char == '6':
                result.append('Z')
            elif char == 'p':
                result.append('a')
            elif char == 'D':
                result.append('b')
            elif char == 'F':
                result.append('c')
            elif char == '9':
                result.append('d')
            elif char == 'y':
                result.append('e')
            elif char == 'V':
                result.append('f')
            elif char == 'S':
                result.append('g')
            elif char == 'O':
                result.append('h')
            elif char == 'b':
                result.append('i')
            elif char == 'E':
                result.append('j')
            elif char == 'd':
                result.append('k')
            elif char == 'a':
                result.append('l')
            elif char == 'A':
                result.append('m')
            elif char == 'h':
                result.append('n')
            elif char == 'z':
                result.append('o')
            elif char == 'w':
                result.append('p')
            elif char == 'R':
                result.append('q')
            elif char == 'x':
                result.append('r')
            elif char == 's':
                result.append('s')
            elif char == 'P':
                result.append('t')
            elif char == 'H':
                result.append('u')
            elif char == 'L':
                result.append('v')
            elif char == '3':
                result.append('w')
            elif char == 'u':
                result.append('x')
            elif char == 'X':
                result.append('y')
            elif char == '4':
                result.append('z')
            elif char == 'U':
                result.append('1')
            elif char == 'Q':
                result.append('2')
            elif char == 'G':
                result.append('3')
            elif char == '0':
                result.append('4')
            elif char == 'm':
                result.append('5')
            elif char == 'J':
                result.append('6')
            elif char == 'N':
                result.append('7')
            elif char == 'k':
                result.append('8')
            elif char == '2':
                result.append('9')
            elif char == 'z':
                result.append('0')
            else:
                pass
    

    with open("received_Decrypted_file.txt", 'w') as output_file:
        output_file.write(result)  # Write the final processed string


Data_Received = open("received_file.txt", 'r')
line = Data_Received.readline().strip()