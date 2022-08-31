global_config = {
  'logarithmicAxisX': False,
  'autoSave': False
}

config = {
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
    'legendPos': 'upper right' 
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
    'phaseLegendPos': 'lower right'
  },
}