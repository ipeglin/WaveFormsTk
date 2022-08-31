from conf.config import global_config, config

# Get config for a specific plot
def get_plot_specific_config(plot_type='') -> dict:
  if (plot_type not in config or plot_type == ''): return {}

  return config[plot_type]

# Get global config options
def get_global_config() -> dict:
  return global_config

# Get plottypes with specified config
def get_available_plot_types() -> list:
  return [plt_type for plt_type in config.keys()]