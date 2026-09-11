# CUHC Fantasy Player Uploader

A small Selenium script that logs into the Fantasy Club Hockey admin page and adds every player listed in a CSV file.

## Setup

### 1. Create a virtual environment

Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
```

### 2. Install the requirements

```bash
pip install -r requirements.txt
```

Google Chrome must also be installed. Selenium downloads the matching driver automatically.

### 3. Set your login details

Copy `.env.example` to `.env` and fill in `WEBSITE_ADDRESS`, `EMAIL_ADDRESS` and `PASSWORD` for the admin account you want to use.

## Player CSVs

Put the players in the CSV for the right club:

| File | Players |
| --- | --- |
| `cumhc_players.csv` | Men's players (CUMHC) |
| `cuwhc_players.csv` | Women's players (CUWHC) |

Both files use the same format as the current ones: a header row followed by one player per line, with the columns `name`, `team` and `position`. Columns are matched by header, so their order does not matter.

`position` must be lowercase and one of `goalkeeper`, `defender`, `midfielder` or `attacker`. Anything else is entered as an attacker.

Example:

```csv
name,team,position
Issy Cutts,Rovers,goalkeeper
Charlotte Bruce,Rovers,defender
Abi Falkous,Nomads,midfielder
Amy Garrod,Nomads,attacker
```

## Running

`main.py` loads the file named in `get_data()` (currently `bdoty_players.csv`). Change that filename to `cumhc_players.csv` or `cuwhc_players.csv` depending on which squad you are uploading, then run:

```bash
python main.py
```

A Chrome window opens, logs in, and adds each player in turn.
