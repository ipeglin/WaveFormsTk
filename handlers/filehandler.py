try:
  import tkinter
  from tkinter import filedialog
  import globals

  root = tkinter.Tk()
except ImportError:
  import Tkinter
  from Tkinter import filedialog

  root = Tkinter.Tk()

root.withdraw()

def get_file_types(list_of_types = []) -> tuple:
  selected_filetypes = [('All files', '*.*')]
  for filetype in list_of_types:
    if (filetype == '*'): continue

    selected_filetypes.insert(0, (f'{filetype.upper()} files', f'*.{filetype.lower()}'))

  return tuple(selected_filetypes)

def get_save_path(init_dir=''):
  if (init_dir == ''):
    init_dir = globals.DEFAULT_SAVE_FILE_PATH
  return get_file(init_dir=init_dir,prompt_title='Choose a save path for your file', filetypes=[globals.DEFAULT_SAVE_FILETYPE])

def get_file(init_dir='', prompt_title='Please select a file', filetypes=[]) -> str:
  if (init_dir == ''):
    init_dir = globals.DEFAULT_DATA_FILE_PATH

  list_of_filetypes = get_file_types(filetypes)
  return filedialog.askopenfilename(initialdir=init_dir, title=prompt_title, filetypes=list_of_filetypes)

def get_directory(init_dir='') -> str:
  return filedialog.askdirectory(initialdir=init_dir, title='Please select a directory')
