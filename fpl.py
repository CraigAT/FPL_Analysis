#!/usr/bin/env python
"""
Fantasy Premier League - Statical Analysis
---
Use the FPL API to gather some data from the FPL site and do some data analysis

"""

__author__      = "Craig Thomas"
__copyright__   = "Copyright 2018, Craig Thomas"
__version__     = "0.1"


import urllib.request, json

if __name__ == '__main__':      #code to execute if called from command-line

    with urllib.request.urlopen("https://fantasy.premierleague.com/drf/bootstrap-static") as url:
        data = json.loads(url.read().decode())
        for players in data["elements"]:
            print(players["web_name"])

