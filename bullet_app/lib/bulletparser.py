import re

# raw string to hold the pattern to avoid backslash weirdness
# when parsing string in re.
pattern = r"([\+\-\\\/\s])+"


def parse(text):
    """ Returns a dictionary containing:
        bullet_dict = {"positive": 1             # integer
                       "negative": 3             # integer
                       "parsed_text": "text"     # string
                       }
    """
    # Match the beginning of the text for bullet signs ("+" or "-".)
    pattern_match = re.match(pattern, text)

    if pattern_match is not None:
        signs = pattern_match.group(0)

        # Strip + and - out of string and give them
        # scores based on occurrences in string.
        # Max a score can be is 5.
        bullet_dict = {"positive":    min(signs.count("+"), 5),
                       "negative":    min(signs.count("-"), 5),
                       "parsed_text": text[len(signs):]
                       }

    # Else add a single positive score
    else:
        bullet_dict = {"positive":    1,
                       "negative":    0,
                       "parsed_text": text}

    return bullet_dict
