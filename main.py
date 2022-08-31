from handlers.confighandler import get_available_plot_types
from handlers.filehandler import get_file
from typing import List, Union

import conf.globals as globals
import handlers.datahandler as dh
import handlers.plothandler as ph

def check_input(input_num, length) -> bool:
  if (input_num != '' and input_num in range(0, length)):
    return True

  return False

def get_plt_type(types=[]) -> Union[int, str]:
  for index, plt_type in enumerate(types):
    print(f'[{index}] {plt_type}')
  
  try:
    input_num: int = int(input('Select plot type: '))
  except ValueError:
    return ''

  if (check_input(input_num, len(types))):
    return input_num

  return ''

def check_plot_type_from_filepath(filepath, plot_types) -> str:
  for plot_type in plot_types:
    if (plot_type.lower() in filepath.lower()):
      print('Plot type detected:', plot_type)
      return plot_types.index(plot_type)

  return ''


if __name__ == '__main__':
  globals.initialize()

  csv_file: str = get_file(filetypes=['csv'])
  csv_data: List[List[float]] = dh.get_csv_data(csv_file)

  if (not csv_data or csv_file == '' or csv_data == []): exit()

  available_types: List[str] = get_available_plot_types()

  selected_plottype: str = check_plot_type_from_filepath(csv_file, available_types)
  while(selected_plottype == ''):
    selected_plottype: Union[int, str] = get_plt_type(available_types)

  ph.plot(available_types[selected_plottype], csv_data)