import sys
sys.path.insert(1, './src/frontend') 
sys.path.insert(1, './src/backend')

from controller import Controller

if __name__ == "__main__": #Controller will only run if main.py is explicitly called through the terminal -- great for modularity reasons
	Controller()
