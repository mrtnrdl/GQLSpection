# These functions are generated by ChatGPT (https://chat.openai.com/chat), Dec 15 [2022] Version.
# According to ChatGPT, the code is licensed under MIT license.


def minimize_query(query):
    # Set up a buffer for the minimized query
    minimized = ""

    # Set up a flag to track whether we are inside a comment
    in_comment = False

    # Set up a flag to track whether we are inside a string
    in_single_string = False
    in_double_string = False
    in_string = False

    # Set up a flag to track whether we are inside a whitespace
    in_space = False

    # Set up a flag to track whether the current character is an escaped quote
    escaped = False

    # Iterate over each character in the query
    for i, c in enumerate(query.strip()):
        # If we see the start of a comment and we are not inside a string,
        # set the in_comment flag
        if c == "#" and not in_string:
            in_comment = True

        # Preserve strings verbatim
        if in_string:
            minimized += c
        # Skip comments entirely
        elif not in_comment:
            # Collapse all whitespace into one space character
            if in_space:
                if not c.isspace():
                    minimized += " " + c
            elif not c.isspace():
                minimized += c

        # If we are inside a whitespace, set the in_space flag
        in_space = c.isspace()

        # If we see the end of a comment and we are not inside a string,
        # clear the in_comment flag
        if not in_string and (c == "\n"):
            in_comment = False

        # Toggle the in_*_string flags if we see quote character, unless it's escaped
        if not in_comment and not escaped:
            in_double_string = not in_double_string if c == '"' else in_double_string
            in_single_string = not in_single_string if c == "'" else in_single_string
        in_string = in_single_string or in_double_string

        # Set the escaped flag, if the current character is a backslash
        escaped = (c == "\\")

    # Return the minimized query
    return minimized


def format_comment(string, max_length=60):
    # Split the string into lines
    lines = string.split('\n')

    # Initialize a list to store the formatted lines
    formatted_lines = []

    # Iterate through the lines
    for line in lines:
        # Split the line into words
        words = line.split()

        # Initialize a variable to keep track of the current line
        current_line = ''

        # Iterate through the words
        for word in words:
            # If the current line plus the next word would be too long,
            # append the current line to the list of formatted lines and start a new line
            if len(current_line) + len(word) > max_length:
                formatted_lines.append(current_line)
                current_line = ''

            # If the current line is empty, add the word to the line
            # Otherwise, add a space and the word to the line
            if current_line == '':
                current_line = word
            else:
                current_line += ' ' + word

        # Add the remaining line to the list of formatted lines
        formatted_lines.append(current_line)

    # Return the formatted comment
    return '\n'.join(['# ' + line for line in formatted_lines])


def safe_get_list(dictionary, name):
    """Safely extract list from the dictionary, even if the key does not exist or type is wrong."""
    res = dictionary.get(name, [])

    if type(res) is list:
        return res
    else:
        return []
