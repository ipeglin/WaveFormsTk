from handlers.confighandler import get_global_config
import matplotlib.pyplot as plt

def spectrum(data, ctx, save_callback) -> None:
  if (len(data) != 5):
    return print('ERROR: Missing data columns in CSV file.\nAs of now, WaveFormsTk only supports fully detailed datafiles for spectrum (5 Columns with frequency, channels and their phases).')
    
  try:
    frequency = [p[0] for p in data]
    ref_voltage = [p[1] for p in data]
  except IndexError:
    return print('ERROR: Insufficient data in CSV file for Spectrum plot')

  has_voltage_change = True

  try:
    voltage_change = [p[3] for p in data]
  except IndexError:
    has_voltage_change = False

  plt.plot(frequency, ref_voltage, '-', color='orange', alpha=0.85)

  if (ctx['includeVoltageChange'] and has_voltage_change):
    plt.plot(frequency, voltage_change, '-', color='blue')

  plt.xlabel(f'{ctx["labels"]["x"]["text"]} [{ctx["labels"]["x"]["unit"]}]')
  plt.ylabel(f'{ctx["labels"]["y"]["text"]} [{ctx["labels"]["y"]["unit"]}]')

  plt.legend([f'${legend}$' for legend in ctx['legends']], loc=ctx['legendPos'])

  if (get_global_config()['autoSave']):
    plt.savefig(save_callback())
  
  plt.show()