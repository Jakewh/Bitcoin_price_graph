import pandas as pd
import bar_chart_race as bcr

"""
 ____ _____ ____              _                                  _     
| __ )_   _/ ___|  _ __  _ __(_) ___ ___    __ _ _ __ __ _ _ __ | |__  
|  _ \ | || |     | '_ \| '__| |/ __/ _ \  / _` | '__/ _` | '_ \| '_ \ 
| |_) || || |___  | |_) | |  | | (_|  __/ | (_| | | | (_| | |_) | | | |
|____/ |_| \____| | .__/|_|  |_|\___\___|  \__, |_|  \__,_| .__/|_| |_|
                  |_|                      |___/          |_|          V1
"""

# vstupní data
df = pd.read_csv("/home/jakub/GitHub/Bitcoin_price_graph/data/BTCUSD_day.csv", index_col = "Date"),

bcr.bar_chart_race(
    df = df[:1],
    period_fmt = "% Y, % b % -d ",
    # výstupní soubor
    filename = "/home/jakub/Github/Bitcoin_price_graph/video.mp4",
    # složka s logem BTC
    img_label_folder = "/home/jakub/Github/Bitcoin_price_graph/data/image/",
    # nastavení loga BTC
    fig_kwargs = {  
        "figsize": (26, 15),  # velikost
        "dpi" : 120,  #  dpi
        "facecolor" : "#F8FAFF"  # barva pozadí
    },
    steps_per_period = 50,
    period_length = 1500,
    n_bars = 1647,
    fixed_max = False
)

