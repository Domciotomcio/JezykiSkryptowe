import configparser
import os

CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.ini")

print("ścieżka", CONFIG_FILE)
config = configparser.ConfigParser()
config['DEFAULT'] = {'DanaA': 1,
                     'DanaB': 'b',
                     'DanaC': "abc",
                     'DanaD': "abc"}


with open(CONFIG_FILE, 'rw') as configfile:
    config.write(configfile)
