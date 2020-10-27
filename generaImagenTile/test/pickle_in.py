import pickle

dogs_dict = {'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16}

print(dogs_dict)

filename = 'dogs'
outfile = open(filename, 'wb')
pickle.dump(dogs_dict, outfile)
outfile.close()
