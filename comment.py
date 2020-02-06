def generate_output(is_valid, message):
    file = open("output.txt", "w")
    if is_valid:
        file.write("Yes")
    else:
        file.write("No\n" + message)
    file.close()

def comment_recognizer():
    with open('input.txt') as f:
        lines = f.read()
        # Handle cases where input does not start with '/*'
        if (lines[:2] != '/*'):
            generate_output(False, "Error: illegal comment")
            return
        output = ['/*']
        comment_ended = False
        counter = 0
        rest_of_comment = lines[2:]
        error_message = ""

        for c in rest_of_comment:
            if (comment_ended):
                generate_output(False, error_message)
                return
            counter += 1
            
            if len(output) > 2:
                if (output[-3] == '"' and output[-2] == '*' and output[-1] == '/' and c != '"'):
                    error_message = "Error: extra characters " + "‘" + rest_of_comment[counter-1:] + "’"
                    comment_ended = True
                if (output[-2] != '"' and output[-1] == '*' and c == '/'):
                    error_message = "Error: extra characters " + "‘" + rest_of_comment[counter:] + "’"
                    comment_ended = True
                if (output[-3] == '/' and output[-2] == '"' and output[-1] == '*' and c == '/'):
                    error_message = "Error: extra characters " + "‘" + rest_of_comment[counter:] + "’"
                    comment_ended = True
                if (counter == len(rest_of_comment) and c == '*'):
                    generate_output(False, "Error: unclosed comment")
                    return
            output.append(c)
        generate_output(True, "")

comment_recognizer()
