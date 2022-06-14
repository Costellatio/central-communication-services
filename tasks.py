from invoke             import task
from dotenv             import load_dotenv
from os                 import path, getenv, listdir
from distutils.dir_util import copy_tree, remove_tree

from src.services.SerialProcessor import SerialProcessor

load_dotenv()

ROOT_PATH = path.dirname(path.abspath(__file__))
LIB_FOLDERS = [
  'dependencies',
  'sensors',
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
  source_path = f'{ROOT_PATH}/src/arduino'

  for folder in LIB_FOLDERS:
    external_library_path = f'{source_path}/{folder}'

    for subfolder in listdir(external_library_path):
      arduino_library_path  = f'{arduino_lib_path}/{subfolder}'
      if path.exists(arduino_library_path):
        remove_tree(arduino_library_path)

    copy_tree(external_library_path, arduino_lib_path)
