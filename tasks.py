from invoke             import task
from dotenv             import load_dotenv
from os                 import path, getenv, listdir
from distutils.dir_util import copy_tree, remove_tree

load_dotenv()

EXTERNAL_ARDUINO_LIBRARY_FOLDERS = [
  'helpers',
  'sensors',
]

ROOT_PATH = path.dirname(path.abspath(__file__))

@task
def initialize_project(context):
  context.run('docker-compose up -d')
  context.run('invoke update-arduino-library')

@task
def update_arduino_library(_):
  arduino_library_folder_path = getenv('ARDUINO_LIBRARY_FOLDER_PATH')
  arduino_source_path         = ROOT_PATH + '/src/arduino'

  for folder in EXTERNAL_ARDUINO_LIBRARY_FOLDERS:
    external_library_path = arduino_source_path + '/' + folder

    for subfolder in listdir(external_library_path):
      arduino_library_path  = arduino_library_folder_path + '/' + subfolder
      if path.exists(arduino_library_path):
        remove_tree(arduino_library_path)

    copy_tree(external_library_path, arduino_library_folder_path)

@task
def run_influx_service(context):
  context.run('python3 ' + ROOT_PATH + '/src/services/influx.py')
