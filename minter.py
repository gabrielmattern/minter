import mintapi

import getpass
import pickle
import os
import subprocess
import sys

def get_credentials():
    store = 'mypswd.p'
    if os.path.exists(store):
        creds = pickle.load(open(store, "rb" ) )
        print("read from file")
    else:
        user = raw_input("Mint Username:")
        passwd = raw_input("Mint Password [%s]:" % getpass.getuser())
        creds = [user, passwd]
        pickle.dump(creds,open(store, "wb" ))
    return creds


if __name__ == "__main__":
    
    get_credentials()

