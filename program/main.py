import pandas as pd
import bar_chart_race as bcr
import os

"""
  ____                  _                     _          
 / ___|_ __ _   _ _ __ | |_ ___    _ __  _ __(_) ___ ___ 
| |   | '__| | | | '_ \| __/ _ \  | '_ \| '__| |/ __/ _ \
| |___| |  | |_| | |_) | || (_) | | |_) | |  | | (_|  __/
 \____|_|   \__, | .__/ \__\___/  | .__/|_|  |_|\___\___|
            |___/|_|              |_|                    
                       _     
  __ _ _ __ __ _ _ __ | |__  
 / _` | '__/ _` | '_ \| '_ \ 
| (_| | | | (_| | |_) | | | |
 \__, |_|  \__,_| .__/|_| |_|V1
 |___/          |_|          

"""

# vstupní data
os.chdir("/home/jakub/GitHub/Bitcoin_price_graph/data")  # složka s csv souborem
data = pd.read_csv("crypto.csv")  # název csv souboru

# příprava dat
cols = ["Date", "BTCUSD", "ETHUSD", "LTCUSD"]  # vybrané sloupce tabulky
Subsetdf = data[cols]  # zobrazení pouze vybraných sloupců v grafu
Subsetdf.set_index("Date", inplace = True)

# nastavení grafu
bcr.bar_chart_race(
    df = Subsetdf,  # data pro graf
    filename = "/home/jakub/GitHub/Bitcoin_price_graph/crypto.mp4",  # výstupní soubor
    img_label_folder = "/home/jakub/GitHub/Bitcoin_price_graph/data",  # složka s logem crypta
    title = "Zaokrouhlený vývoj ceny 2015 - 2020",  # titulek grafu
    fixed_max = True,  # zastavení pohybu osy y
    colors = ["#EBB326", "#3395ff", "#242527" ]  # barva grafu
)
