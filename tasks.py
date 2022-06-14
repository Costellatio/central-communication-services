from invoke             import task
from dotenv             import load_dotenv
from os                 import path, getenv, listdir
from distutils.dir_util import copy_tree, remove_tree

from src.services.SerialProcessor import SerialProcessor

load_dotenv()

ROOT_PATH = path.dirname(path.abspath(__file__))
ARDUINO_SOURCE_PATH = f'{ROOT_PATH}/src/arduino'
ARDUINO_LIB_FOLDERS = [
  f'{ARDUINO_SOURCE_PATH}/dependencies',
  f'{ARDUINO_SOURCE_PATH}/sensors',
]

@task
def initialize_project(context):
  context.run('docker-compose up -d')
  context.run('invoke install-dependencies')

@task
def start_serial_processor(_):
  SerialProcessor().listen()

@task
def install_dependencies(_):
  arduino_lib_path = getenv('ARDUINO_LIB_PATH')

  for folder in ARDUINO_LIB_FOLDERS:
    for subfolder in listdir(folder):
      arduino_library_path  = f'{arduino_lib_path}/{subfolder}'
      if path.exists(arduino_library_path):
        remove_tree(arduino_library_path)

    copy_tree(folder, arduino_lib_path)
