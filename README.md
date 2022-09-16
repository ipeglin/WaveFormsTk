# WaveForms Toolkit v2

## Summary

This is a plotting kit for using Analog Discovery 2 for the courses [ESDA I](https://www.ntnu.edu/studies/courses/TTT4260#tab=omEmnet) and [ESDA II](https://www.ntnu.edu/studies/courses/TTT4265#tab=omEmnet) for [MTELSYS](https://www.ntnu.edu/studies/mtelsys) at NTNU, Trondheim.

## Prerequirements
* Python 2 or 3
* tkinter

## Quick Start

1. Download the intended asset underneath Releases.
3. Navigate to the downloaded folder with terminal or finder / explorer.
4. Run the python script i.e. with `python3 main.py`.

## Features

### Autodetection of Plot Types
If the name of your CSV data file contains the name of your defined plot types, the program will automatically select til plot type, so there is no need for manual input in the terminal.

**Out-of-the-box detection keywords:**
* Scope
* Bode
* Spectrum

### Checking for missing configurations
If a plot is missing important values in its configuration, the program will prompt the user for input. As of now, this check is only limited to plot legends and legend position. However updates to this feature may follow in the near future.

## Usage

### Adding New Plot Types

1. Create plot script in the `plots/` folder.
2. Create relevant config options for the new plot in the `config` variable in `conf/config.py`.
3. Add the plot to the function mapping in `handlers/plothandler.py`

### Configuration

#### Set prefered file paths
Change the global variables in `conf/globals.py` to the default filepaths you want the file selector should open in. You can also set your prefered filetype for storing plots, but `.svg` is strongly recommended.

#### Enable Plot Autosave
To enable automatic plot saving, change the *autoSave* variable in `conf/config.py`
```python3
'autoSave': True
```

#### Logarithmix Scale of X Axis
To enable logarithmic scaling, change the *logarithmicAxisX* variable in `conf/config.py`
```python3
'logarithmicAxisX': True
```

#### Change Config Variables For Plot Type
Change variables in `conf/config.py` to match the data from your plot.

## Authors

* **Ian Philip Eglin** - [ipeglin](https://github.com/ipeglin)
