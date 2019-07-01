from random_word import RandomWords
import random
"""
this method with generate one random word from list of the
available word 
"""


def gen_word():
    r = RandomWords()
    random_words = r.get_random_words()
    gen_random_number = random.randint(1, len(random_words))
    #print(random_words[gen_random_number])
    random_word = random_words[gen_random_number]
    return random_word
