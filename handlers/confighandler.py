from config import global_config, config

def get_plot_specific_config(plot_type='') -> dict:
  if (plot_type not in config or plot_type == ''): return {}

  return config[plot_type]

def get_global_config() -> dict:
  return global_config

def get_available_plot_types() -> list:
  return [plt_type for plt_type in config.keys()]