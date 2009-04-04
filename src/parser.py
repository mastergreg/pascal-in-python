from ply import lex
from tokens import *

# A string containing ignored characters (spaces and tabs).
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]


# Build the lexer
lex.lex()

# Get the input
data = raw_input()

lex.input(data)

# Tokenize
while 1 :
        tok = lex.token()
        if not tok :
                break
        print tok

def t_VAR(t):
    r'[a-zA-Z_][\w_]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t