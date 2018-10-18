import os 

GAME_NAME = "happy_adventure"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAME_DIR = os.path.join(BASE_DIR, GAME_NAME)

DEVELOPMENT = True
DEPLOY = True

IMAGES_PATH = GAME_NAME +"/images/"