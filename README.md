# WaveForms Toolkit v2

## Summary

This is a plotting kit for using Analog Discovery 2 for the courses [ESDA I](https://www.ntnu.edu/studies/courses/TTT4260#tab=omEmnet) and [ESDA II](https://www.ntnu.edu/studies/courses/TTT4265#tab=omEmnet) for [MTELSYS](https://www.ntnu.edu/studies/mtelsys) at NTNU, Trondheim.

## Quick Start

1. Clone repository with `git clone 
git@github.com:ipeglin/WaveFormsTk.git`
2. Navigate to your repo with `cd ./WaveFormsTk/`
3. Select wanted branch with `git checkout BranchName` *(optional)*
4. Run program with `python3 main.py`

## Usage

### Add New Plot Types

1. Create plot script in the `plots/` folder.
2. Create relevant config options for the new plot in the `config` variable in `conf/config.py`.
3. Add the plot to the function mapping in `handlers/plothandler.py`

### Configuration

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
