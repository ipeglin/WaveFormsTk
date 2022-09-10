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
