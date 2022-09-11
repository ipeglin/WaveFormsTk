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

def get_empty_containers(name, content):
  if (isinstance(content, dict) and name == 'labels'):
    missing_config = []
    for key, value in content.items():
      if (value != {'text': '', 'unit': ''}): continue
        
      missing_config.append({name: [key]})
    
    if (missing_config != []):
      return missing_config

  if (isinstance(content, list) and content == []):
    return name

  if (isinstance(content, str) and name == 'legendPos' and content == ''):
    return name

def validate_config_entry(entry, entry_type):
  if (entry_type == 'legends' and entry.replace(' ', '') == ''):
    return False

  return True