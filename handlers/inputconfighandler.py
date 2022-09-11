from composables.accessability import parse_correct_legend_position, separate_string_to_list
from composables.validation import validate_config_entry

def get_input_prompt(config_name, config_type):
  if (isinstance(config_type, list)): return input(f'{config_name.capitalize()} (separer med komma): ')

  return input(f'{config_name.capitalize()}: ')

def format_input_by_type(input_string, target):
  if (input_string == ''): return print('Empty input_string:', input_string, target)

  if (isinstance(target, list)):
    return separate_string_to_list(input_string)

  if (isinstance(target, str)):
    return input_string


def launch_missing_config_form(current_config, missing_configs = []):
  if (missing_configs == []): return

  for config in missing_configs:
    target = current_config[config]
    config_input = get_input_prompt(config, target)

    if (config == 'legendPos'):
      current_config[config] = parse_correct_legend_position(config_input)

    elif (validate_config_entry(config_input, config)):
      current_config[config] = format_input_by_type(config_input, target)
      