from composables.accessability import get_plt_type
from composables.validation import check_plot_type_from_filepath
from handlers.confighandler import get_available_plot_types
from handlers.filehandler import get_file
from typing import List, Union

import conf.globals as globals
import handlers.datahandler as dh
import handlers.plothandler as ph

if __name__ == '__main__':
  globals.initialize()

  print('1. Select data file in finder / explorer')
  csv_file: str = get_file(prompt_title='Please select your WaveForms data file', filetypes=['csv'])
  csv_data: List[List[float]] = dh.get_csv_data(csv_file)

  if (not csv_data or csv_file == '' or csv_data == []): exit()

  available_types: List[str] = get_available_plot_types()
  selected_plottype: str = check_plot_type_from_filepath(csv_file, available_types)

  while(selected_plottype == ''):
    print('2. Select plot type')
    selected_plottype: Union[int, str] = get_plt_type(available_types)

  ph.plot(available_types[selected_plottype], csv_data)