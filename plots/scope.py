from handlers.confighandler import get_global_config
import matplotlib.pyplot as plt

def scope(data, ctx, save_callback) -> None:
  try:
    time = [p[0] for p in data]
    ch1 = [p[1] for p in data]
  except IndexError:
    return print('ERROR: Insufficient data in CSV file for scope plot')

  has_two_channels = True
  
  try:
    ch2 = [p[2] for p in data]
  except IndexError:
    has_two_channels = False

  plt.plot(time, ch1, '-', color='orange', alpha=1)
  
  if (len(ctx['legends']) == 2 and has_two_channels):
    plt.plot(time, ch2, '-', color='blue', alpha=1)

  if (get_global_config()['logarithmicAxisX']):
    plt.xscale('log')

  plt.xlabel(f'{ctx["labels"]["x"]["text"]} [{ctx["labels"]["x"]["unit"]}]')
  plt.ylabel(f'{ctx["labels"]["y"]["text"]} [{ctx["labels"]["y"]["unit"]}]')

  plt.legend([f'${legend}$' for legend in ctx['legends']], loc=ctx['legendPos'])

  if (get_global_config()['autoSave']):
    plt.savefig(save_callback())
  
  plt.show()