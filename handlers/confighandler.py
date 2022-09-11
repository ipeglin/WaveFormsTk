from composables.accessability import parse_correct_legend_position, strip_list_from_none
from composables.validation import get_empty_containers
from conf.config import global_config, config
from handlers.inputhandler import launch_missing_config_form

def get_plot_specific_config(plot_type=''):
  if (plot_type not in config or plot_type == ''): return {}

  return config[plot_type]

def get_global_config():
  return global_config

# Get plottypes with specified config
def get_available_plot_types():
  return [plt_type for plt_type in config.keys()]

# Trigger prompts for user to enter config
def get_missing_config_options(plot_type, missing_configurations):
  print('1b. Getting missing config options:', missing_configurations)
  launch_missing_config_form(current_config=get_plot_specific_config(plot_type), missing_configs=missing_configurations)
  

# Make user input data if config is missing
def handle_unspecified_config_entries(plot_type='', plot_config={}):
  if (plot_type == '' or plot_config == {}): return
  
  missing_configurations = strip_list_from_none([get_empty_containers(name, config) for name, config in plot_config.items()])

  if (missing_configurations != []):
    get_missing_config_options(plot_type, missing_configurations)

  plot_config['legendPos'] = parse_correct_legend_position(plot_config['legendPos'])