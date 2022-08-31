try:
  # Python3
  import tkinter
  from tkinter import filedialog
  import conf.globals as globals
  from typing import Tuple, List

  root = tkinter.Tk()
except ImportError:
  # Python2
  import Tkinter
  from Tkinter import filedialog
  import conf.globals as globals
  from typing import Tuple, List

  root = Tkinter.Tk()

root.withdraw() # Hide client

# Get list of filetypes to allow in finder / explorer
def get_file_types(list_of_types = []) -> Tuple[Tuple[str]]:
  selected_filetypes: List = [('All files', '*.*')]
  for filetype in list_of_types:
    if (filetype == '*'): continue

    selected_filetypes.insert(0, (f'{filetype.upper()} files', f'*.{filetype.lower()}'))

  return tuple(selected_filetypes)

# Get the save path for autosaved plot
def get_save_path(init_dir='') -> str:
  if (init_dir == ''):
    init_dir: str = globals.DEFAULT_SAVE_FILE_PATH
  
  save_dir: str = filedialog.askdirectory(initialdir=init_dir, title='Select where to save the file')
  save_name: str = ''
  while (save_name == ''):
    save_name: str = input('Name of saved plot: ')
  
  return f'{save_dir}/{save_name}.{globals.DEFAULT_SAVE_FILETYPE}'

# Get filepath with finder / explorer
def get_file(init_dir='', prompt_title='Please select a file', filetypes=[]) -> str:
  if (init_dir == ''):
    init_dir: str = globals.DEFAULT_DATA_FILE_PATH

  list_of_filetypes: Tuple[Tuple[str]] = get_file_types(filetypes)
  return filedialog.askopenfilename(initialdir=init_dir, title=prompt_title, filetypes=list_of_filetypes)

# Get directory path with finder / explorer
def get_directory(init_dir='') -> str:
  return filedialog.askdirectory(initialdir=init_dir, title='Please select a directory')
