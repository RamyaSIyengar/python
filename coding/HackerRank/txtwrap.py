import textwrap


# def wrap(string, max_width):
#     wrapper = textwrap.TextWrapper(max_width)
#     print(wrapper)
#     word_list = wrapper.wrap(text=string)
#     print(*word_list, sep='\n')
#
#
#     return *word_list

def wrap(string, max_width):
    # Use the fill method to wrap the text and insert newlines
    wrapped_string = textwrap.fill(string, width=max_width)

    return wrapped_string


print(wrap('ABCDADADXJNKNLNLK', 4))