def is_phone_number(text):
    """Function to determine if a given text value is a phone number"""
    text = str(text).strip()
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print(is_phone_number('780-456-2516'))


test_message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

def search_message(message):
    """Search an entire message for the occurance of a phone number"""
    for i in range(len(message)):
        chunk = message[i:i+12]
        if is_phone_number(chunk):
            print(f'Phone number found: {chunk}')
    print('Done.')

search_message(test_message)

