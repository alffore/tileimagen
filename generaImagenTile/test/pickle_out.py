# https://www.datacamp.com/community/tutorials/pickle-python-tutorial

import pickle

filename = 'dogs'

infile = open(filename, 'rb')
new_dict = pickle.load(infile)
infile.close()

print(new_dict)
