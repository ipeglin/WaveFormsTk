from typing import Dict

global_config: Dict = {
  'logarithmicAxisX': False,
  'autoSave': False # Always save plots on run
}

# Preferences for each plot type
config: Dict = {
  'scope': {
    'labels': {
      'x': {
        'text': 'Tid',
        'unit': 's'
      },
      'y': {
        'text': 'Spenning',
        'unit': 'V'
      }
    },
    'legends': [
      'v_1', 'v_2'
    ],
    'legendPos': 'upper right'
  },
  'bode': {
    'includePhaseResponse': True,
    'legends': [
      'v_1', 'v_2'
    ],
    'legendPos': 'upper right',
    'phaseLegendPos': 'lower right'
  },
  'spectrum': {
    'includeVoltageChange': True,
    'labels': {
      'x': {
        'text': 'Frekvens',
        'unit': 'Hz'
      },
      'y': {
        'text': 'Amplituderespons',
        'unit': 'dB'
      }
    },
    'legends': [
      'Inngangsignal', 'Utgangssignal'
    ],
    'legendPos': 'upper right',
  },
}