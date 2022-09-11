from ssl import VerifyFlags
from composables.validation import check_input

def get_plt_type(types=[]):
  for index, plt_type in enumerate(types):
    print(f'   [{index}] {plt_type}')
  
  try:
    input_num = int(input('   Select plot type (number): '))
  except ValueError:
    return ''

  if (check_input(input_num, len(types))):
    return input_num

  return ''

# Remove elements of type None from list
def strip_list_from_none(container):
  return [element for element in container if (element != None)]

def separate_string_to_list(string):
  return [substring for substring in string.replace(', ', ',').split(',')]

def parse_correct_legend_position(pos):
  if (pos == ''): return 'best'
  
  horisontals = ['left', 'right']
  verticals = ['upper', 'lower']

  try:
    y, x = pos.lower().split(' ')
  except ValueError:
    return 'best'

  if (x.lower() in horisontals and y.lower() in verticals): 
    return pos

  return 'best'