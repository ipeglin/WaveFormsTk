from handlers.confighandler import get_global_config
import matplotlib.pyplot as plt

def bode(data, ctx, save_callback) -> None:
  frequency = [p[0] for p in data]
  ref_voltage = [p[1] for p in data]
  amplitude_response = [p[2] for p in data]

  plt.xlabel('Frekvens [Hz]')
  
  if (ctx['inlucdePhaseResponse']):
    phase_response = [p[3] for p in data]

    fig, axs = plt.subplots(2, sharex=True)

    color = 'tab:blue'
    axs[0].set_ylabel("Amplituderespons [dB]", color=color)
    axs[0].plot(frequency, ref_voltage, "-", color="tab:orange", label=ctx["legends"][0])
    axs[0].plot(frequency, amplitude_response, "-", color=color, label=ctx["legends"][1])
    axs[0].legend(loc=ctx['legendPos'])
    axs[0].tick_params(axis="y", labelcolor=color)

    color = 'tab:green'
    axs[1].set_ylabel("Vinkel [deg $^\circ$]", color=color)
    axs[1].plot(frequency, phase_response, "-", color=color, label="Faserespons")
    axs[1].legend(loc=ctx["phaseLegendPos"])
    axs[1].tick_params(axis="y", labelcolor=color)

    fig.tight_layout()
  
  else:
    plt.plot(frequency, ref_voltage, "-", color="orange")
    plt.plot(frequency, amplitude_response, "-", color="blue")

    plt.ylabel("Amplituderespons [dB]")
    plt.legend([f'${legend}$' for legend in ctx["legends"]], loc=ctx["legendPos"])

  if (get_global_config()['logarithmicAxisX']):
    plt.xscale('log')

  if (get_global_config()['saveFigure']):
    plt.savefig(save_callback())

  plt.show()
