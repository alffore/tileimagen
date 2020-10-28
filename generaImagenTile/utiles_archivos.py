import pickle


def guardaDI(ddict):
    tid = ddict['id']
    archivo = f'./cache/{tid}.pk'
    with open(archivo, 'wb') as outfile:
        pickle.dump(ddict, outfile)
        outfile.close()
    return


def recuperaDI():
    return
