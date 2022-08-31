from handlers.confighandler import get_available_plot_types
from handlers.filehandler import get_file

import globals
import handlers.datahandler as dh
import handlers.plothandler as ph

def check_input(input_num, length) -> bool:
  if (input_num != '' or input_num not in range(0, length + 1)):
    return True

  return False

def get_plt_type(types=[]):

  print('Select plot type')
  for index, plt_type in enumerate(types):
    print(f'[{index}] {plt_type}')
  
  input_num = int(input('Select plot type: '))

  if (check_input(input_num, len(types))):
    return input_num

  return ''

if __name__ == '__main__':
  globals.initialize()

  csv_data = dh.get_csv_data(get_file(filetypes=['csv']))
  if (not csv_data or csv_data == ''): exit()

  available_types = get_available_plot_types()

  selected_plottype = ''
  while(selected_plottype == ''):
    selected_plottype = get_plt_type(available_types)

  ph.plot(available_types[selected_plottype], csv_data)