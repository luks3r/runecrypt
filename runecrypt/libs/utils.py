#
# Utitlities
#

# Imports
import random

# Shuffle string
def stringShuffle(string, seed):
    random.seed(seed)
    string_list = list(string)
    random.shuffle(string_list)
    return ''.join(string_list)
