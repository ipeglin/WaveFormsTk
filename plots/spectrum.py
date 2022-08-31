from handlers.confighandler import get_global_config
from typing import List
import matplotlib.pyplot as plt

def spectrum(data, ctx, save_callback) -> None:
  frequency: List[float] = [p[0] for p in data]
  ref_voltage: List[float] = [p[1] for p in data]
  plt.plot(frequency, ref_voltage, '-', color='orange', alpha=0.85)

  if (ctx['includeVoltageChange']):
    voltage_change: List[float] = [p[3] for p in data]
    plt.plot(frequency, voltage_change, '-', color='blue')

  plt.xlabel(f'{ctx["labels"]["x"]["text"]} [{ctx["labels"]["x"]["unit"]}]')
  plt.ylabel(f'{ctx["labels"]["y"]["text"]} [{ctx["labels"]["y"]["unit"]}]')

  plt.legend([f'${legend}$' for legend in ctx["legends"]], loc=ctx["legendPos"])

  if (get_global_config()['autoSave']):
    plt.savefig(save_callback())
  
  plt.show()