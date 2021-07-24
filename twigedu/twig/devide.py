def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def input_validation(num):
    try:
        n = int(num)
        if n >= 0:
            return n
        else:
            new_input = input("Enter positive int value")
            return input_validation(new_input)
    except ValueError as e:
        new_input = input("Enter valid int value")
        return input_validation(new_input)

def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False
