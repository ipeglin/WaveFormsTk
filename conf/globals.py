def initialize():
  global DEFAULT_SAVE_FILE_PATH
  global DEFAULT_DATA_FILE_PATH
  global DEFAULT_SAVE_FILETYPE

  DEFAULT_SAVE_FILETYPE = 'svg' # Prefered filetype for saved plots (SVG recommended)

  HOME_PATH = '' # Default ~ path
  DEFAULT_DATA_FILE_PATH = f'{HOME_PATH}/' # Prefered folder for retrieving data files
  DEFAULT_SAVE_FILE_PATH = f'{HOME_PATH}/' # Prefered folder for saving plots