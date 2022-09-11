from handlers.confighandler import get_plot_specific_config, handle_unspecified_enteries
from handlers.filehandler import get_save_path
from plots.bode import bode
from plots.scope import scope
from plots.spectrum import spectrum

# Script mapping to preform correct plot
def plot(plot_type='', data=[]):
  if (plot_type == ''): return

  plot_context = get_plot_specific_config(plot_type) # Get selected plot config
  
  handle_unspecified_enteries(plot_type, plot_context)

  plotting_map = {
    'scope': lambda: scope(data, plot_context, save_callback=get_save_path),
    'bode': lambda: bode(data, plot_context, save_callback=get_save_path),
    'spectrum': lambda: spectrum(data, plot_context, save_callback=get_save_path),
  }

  if (plot_type.lower() not in plotting_map): return print('Plot type is not defined. Quitting..')

  return plotting_map[plot_type]()