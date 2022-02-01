import pandas as pd
import bar_chart_race as bcr
import os

"""
 ____ _____ ____              _                                  _     
| __ )_   _/ ___|  _ __  _ __(_) ___ ___    __ _ _ __ __ _ _ __ | |__  
|  _ \ | || |     | '_ \| '__| |/ __/ _ \  / _` | '__/ _` | '_ \| '_ \ 
| |_) || || |___  | |_) | |  | | (_|  __/ | (_| | | | (_| | |_) | | | |
|____/ |_| \____| | .__/|_|  |_|\___\___|  \__, |_|  \__,_| .__/|_| |_|
                  |_|                      |___/          |_|          V1
"""

# vstupní data
os.chdir("/home/jakub/GitHub/Bitcoin_price_graph/data")  # složka s csv souborem
data = pd.read_csv("BTCUSD_day.csv")  # název csv souboru

# příprava dat
cols = ["Date", "BTCUSD"]  # vybrané sloupce tabulky
Subsetdf = data[cols]  # zobrazení pouze vybraných sloupců v grafu
Subsetdf.set_index("Date", inplace = True)

# nastavení grafu
bcr.bar_chart_race(
    df = Subsetdf,  # data pro graf
    filename = "/home/jakub/GitHub/Bitcoin_price_graph/BTCUSD.mp4",  # výstupní soubor
    img_label_folder = "/home/jakub/GitHub/Bitcoin_price_graph/data",  # složka s obrázkem btc
    title = "Vývoj ceny BTC/USD 2015 - 2020",  # titulek grafu
    fixed_max = True,  # zastavení pohybu osy y
    colors = ["#EBB326"]  # žlutooranžová barva grafu
)