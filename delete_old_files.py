import os
import time
import shutil
import logging

DELETE_ALWAYS = ('.tor', '.torrent')
DELETE_NEVER = ()
DELETE_AFTER = 24
DELETE_PATH = '/Users/username/Downloads/'

logging.basicConfig(format='%(asctime)s %(message)s', filename='/Users/username/Library/Logs/cleanup.log', level=logging.INFO)

def rotten_file(file):
    name, ext = os.path.splitext(file)
    return (time.time() - os.path.getmtime(DELETE_PATH +
            file) > (DELETE_AFTER*3600))

def precious_file(file):
    name, ext = os.path.splitext(file)
    return ext in DELETE_NEVER

def worthless_file(file):
    name, ext = os.path.splitext(file)
    return ext in DELETE_ALWAYS

# files to evaluate
contents = []

# omit hidden files
for file in os.listdir(DELETE_PATH):
    if not file.startswith('.'):
        contents.append(file)

# begin log
logging.info('Cleaning Directory')

# evaluate all files
for file in contents:
    fullpath = DELETE_PATH + file
    if (not rotten_file(file) and not worthless_file(file)):
        continue
    elif not precious_file(file):
        if os.path.isfile(fullpath):
            os.remove(fullpath)
            logging.info('deleting file %s', file)
        elif os.path.isdir(fullpath):
            shutil.rmtree(fullpath)
            logging.info('deleting directory %s', file)
