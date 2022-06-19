from dotenv import dotenv_values

class Env:
  _env = None

  @staticmethod
  def get(name):
    if Env._env == None:
      _env = dotenv_values()

    return _env[name]
