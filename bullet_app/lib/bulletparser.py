import re

# tested this regex at http://www.regexr.com
# but it is greedy when using re library,
# need to implement the non-greedy version
pattern = "([\+\-\\\/\s])+"


def parse(text):
    bullet = {}
    # Match the
    signs = text.split(" ")[0]
    bullet["parsedtext"] = text.split(" ", 1)[1:][0]
    print(signs)
    return bullet
