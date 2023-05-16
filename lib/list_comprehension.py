#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [x for x in num_list if x % 2 == 0]
    return even_numbers
    

def make_exclamation(sentence_list):
    exclamation_generator = (sentence + '!' for sentence in sentence_list)
    return list(exclamation_generator)
