import re

phoneRegex = re.compile(r'''(
    (\d{3}|(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)


# TODO Create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a=zA=Z]{2,4})
    )''', re.VERBOSE)

# TODO Find matches to clipboard text

# TODO Copy results to clipboard