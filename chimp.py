# Import Modules
import os, pygame
from pygame.locals import *

if not pygame.font: print "Warning, fonts disabled"
if not pygame.mixer: print "Warning, sound disabled"

# functions to create our resources
def load_image(name, colorKey=None):
	fullname = os.path.join('data', name)
	try:
		