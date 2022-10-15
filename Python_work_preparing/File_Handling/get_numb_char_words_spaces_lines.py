def numb_char(text):
    char_count = 0
    for i in text:
        if((i > ' ') and (i < '~')):
            char_count += 1
    return char_count

def numb_words(text):
    splited_text_lst = text.split()
    word_count = len(splited_text_lst)
    return word_count

def numb_space(text):
    space_counter = 0
    for i in text:
        if(i == ' '):
            space_counter += 1
    return space_counter

def numb_line(text):
    line_counter = 1
    for i in text:
        if(i == '\n'):
            line_counter += 1
    return line_counter

f = open("example_file.txt", "r")
text = f.read()

char_count = numb_char(text)
print("Number of characters is: ", char_count)
word_count = numb_words(text)
print("Number of words is: ", word_count)
space_counter = numb_space(text)
print("Number of spaces is: ", space_counter)
line_counter = numb_line(text)
print("Number of lines is: ", line_counter)