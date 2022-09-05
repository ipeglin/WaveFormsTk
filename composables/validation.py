def check_input(input_num, length) -> bool:
  if (input_num != '' and input_num in range(0, length)):
    return True

  return False

def check_plot_type_from_filepath(filepath, plot_types) -> str:
  for plot_type in plot_types:
    if (plot_type.lower() in filepath.lower()):
      print('Plot type detected:', plot_type)
      return plot_types.index(plot_type)

  return ''