from handlers.confighandler import get_plot_specific_config, handle_unspecified_config_entries
from handlers.filehandler import get_save_path

# Plots
from plots.bode import bode
from plots.scope import scope
from plots.spectrum import spectrum

# Script mapping to correct plot
def plot(plot_type='', data=[]):
  if (plot_type == ''): return

  plot_configuration = get_plot_specific_config(plot_type) # Get selected plot config
  
  handle_unspecified_config_entries(plot_type, plot_configuration)

  plotting_map = {
    'scope': lambda: scope(data, plot_configuration, save_callback=get_save_path),
    'bode': lambda: bode(data, plot_configuration, save_callback=get_save_path),
    'spectrum': lambda: spectrum(data, plot_configuration, save_callback=get_save_path),
  }

  if (plot_type.lower() not in plotting_map): return print('ERROR: Plot type is not defined. Quitting..')

  return plotting_map[plot_type]()