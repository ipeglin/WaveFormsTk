from handlers.confighandler import get_global_config
from typing import List
import matplotlib.pyplot as plt

def scope(data, ctx, save_callback) -> None:
  time: List[float] = [p[0] for p in data]
  ch1: List[float] = [p[1] for p in data]
  ch2: List[float] = [p[2] for p in data]

  plt.plot(time, ch1, '-', color='orange', alpha=1)
  
  if (len(ctx['legends']) == 2):
    plt.plot(time, ch2, '-', color='blue', alpha=1)

  if (get_global_config()['logarithmicAxisX']):
    plt.xscale('log')

  plt.xlabel(f'{ctx["labels"]["x"]["text"]} [{ctx["labels"]["x"]["unit"]}]')
  plt.ylabel(f'{ctx["labels"]["y"]["text"]} [{ctx["labels"]["y"]["unit"]}]')

  plt.legend([f'${legend}$' for legend in ctx["legends"]], loc=ctx["legendPos"])

  if (get_global_config()['autoSave']):
    plt.savefig(save_callback())
  
  plt.show()