# Analysis of FINN ADS

An analysis of a dataset of some FINN.no ads

## Running

### First time setup
The project requires python 3.10
```bash
python -m venv venv  # create virtual environment
source venv/bin/activate  # activate venv;  windows: venv/Scripts/activate
pip install .  # install packages and initialize project
```

### Running
```bash
process-ads --file path/to/file [--write]
# OR
python -m finn_ads.main --file path/to/file [--write]
```

Example using ads.txt in the data folder and writing to file adStats.txt
```bash
process-ads --file ./data/ads.txt --write
```

