#
# Skeleton file for the Python "Bob" exercise.
#


def hey(what):
    answer = ""
    what = what.strip()
    if len(what) == 0:
        answer = "Fine. Be that way!"
    elif what.isupper():
        answer = "Whoa, chill out!"
    elif what[len(what) - 1] == "?":
        answer = "Sure."
    else:
        answer = "Whatever."
    
    return answer