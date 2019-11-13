import re

"""
    Sometimes you want a search to be case insensitive.
    re.IGNORECASE or re.I as second arg to re.compile()
"""
robocop = re.compile('robocop', re.I)
print(robocop.search('RoboCop is part man, part machine, all cop').group())
print(robocop.search('ROBOCOP protects the innocent.').group())
print(robocop.search('Al, why does your programming book talk about robocop so much?').group())


"""
    Substituting strings with the sub() method
    Allows you you to pass in direct substitutions that match your regex
    returns a new string with substitutions
    - run sub() method on a compiled regex
    - 1st arg: string to replace your matches
    - 2nd arg: string for the regular expression to sift through
"""

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

# Include matched text as part of replacement text
# \1 \2 \3 - all can access the various groups of text
agentRegex = re.compile(r'Agent (\w)\w*')
print(agentRegex.search('Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.').groups())
print(agentRegex.sub(r'\1***', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))


"""
    Complex Regex on multilines
    re.VERBOSE
    Handle multi line, complicated regex patterns using docstrings
    and passing re.VERBOSE as second argument to .compile()
"""
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # area code
(\s|-|\.)? # separator
\d{3} # first 3 digits
(\s|-|\.) # separator
\d{4} # last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})? # extension
)''', re.VERBOSE)

print(phoneRegex)


"""
    Combining re.IGNOREC ASE, re.DOT ALL , and re.VERBOSE
    USE | bitwise operator as or option as second argument in compile()
"""
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)