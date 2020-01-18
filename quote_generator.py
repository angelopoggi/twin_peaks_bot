###########################
#Random Gordon Cole Generator
#By: Angelo Poggi
#angelo@poggi.work
#
#
############################

import random

def cole_quote():
    quote_tuple = []
    with open('quotes.txt', 'r') as quotes:
        for line in quotes:
            quote_tuple.append(line)
        random_quote = random.choice(quote_tuple)
        return random_quote

