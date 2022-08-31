from handlers.confighandler import get_plot_specific_config
from handlers.filehandler import get_save_path
from plots.bode import bode
from plots.scope import scope
from plots.spectrum import spectrum

def plot(plot_type='', data=[]) -> None:
  if (plot_type == ''): return

  plot_context = get_plot_specific_config(plot_type)

  plotting_map = {
    'scope': lambda: scope(data, plot_context, save_callback=get_save_path),
    'bode': lambda: bode(data, plot_context, save_callback=get_save_path),
    'spectrum': lambda: spectrum(data, plot_context, save_callback=get_save_path),
  }

  if (plot_type.lower() not in plotting_map): return print('Escaping')

  return plotting_map[plot_type]()