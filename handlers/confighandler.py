from composables.accessability import parse_correct_legend_position, strip_list_from_none
from composables.validation import get_empty_containers
from conf.config import global_config, config
from handlers.inputhandler import launch_missing_config_form

# Get config for a specific plot
def get_plot_specific_config(plot_type=''):
  if (plot_type not in config or plot_type == ''): return {}

  return config[plot_type]

# Get global config options
def get_global_config():
  return global_config

# Get plottypes with specified config
def get_available_plot_types():
  return [plt_type for plt_type in config.keys()]

# Trigger GUI for user to enter config
def get_missing_config_options(plot_type, missing_config):
  print("1b. Getting missing config options:", missing_config)
  
  launch_missing_config_form(current_config=get_plot_specific_config(plot_type), missing_configs=missing_config)
  

# Make user input data if config is missing
def handle_unspecified_enteries(plot_type='', plot_config={}):
  if (plot_type == '' or plot_config == {}): return
  
  missing_config = strip_list_from_none([get_empty_containers(name, config) for name, config in plot_config.items()])

  if (missing_config != []):
    get_missing_config_options(plot_type, missing_config)

  plot_config['legendPos'] = parse_correct_legend_position(plot_config['legendPos'])