from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from datetime import datetime, timedelta
import pandas as pd
import os


basepath = os.path.dirname(os.path.abspath(__file__))


# data sourced from BIS, https://data.bis.org/topics/XRU/BIS,WS_XRU,1.0/D.CA.CAD.A?filter=TIMESPAN%3D1972-01-01_2025-01-26


euro_dataframe = pd.read_csv(os.path.join(basepath, "USD_EURO_EUROperUSD.csv"))
yen_dataframe = pd.read_csv(os.path.join(basepath, "./USD_YEN_YENperUSD.csv"))
cad_dataframe = pd.read_csv(os.path.join(basepath, "./USD_CAD_CADperUSD.csv"))
baht_dataframe = pd.read_csv(os.path.join(basepath, "./USD_THB_THBperUSD.csv"))

plt.plot_date(pd.to_datetime(euro_dataframe["TIME_PERIOD:Period"]),euro_dataframe["OBS_VALUE:Value"], linestyle = "solid", label = "EURO/USD", color = "green", marker = None)
plt.plot_date(pd.to_datetime(yen_dataframe["TIME_PERIOD:Period"]),yen_dataframe["OBS_VALUE:Value"]/100, linestyle = "solid", label = "YEN/USCENT", color = "yellow", marker = None)
plt.plot_date(pd.to_datetime(cad_dataframe["TIME_PERIOD:Period"]),cad_dataframe["OBS_VALUE:Value"], linestyle = "solid", label = "CAD/USD", color = "blue", marker = None)
plt.plot_date(pd.to_datetime(baht_dataframe["TIME_PERIOD:Period"]),baht_dataframe["OBS_VALUE:Value"]/20, linestyle = "solid", label = "BAHT/US2CENTs", color = "orange", marker = None)


date_format = mpl_dates.DateFormatter("%b, %d, %Y")
plt.gca().xaxis.set_major_formatter(date_format)

plt.title("EURO, YEN, CAD, BAHT to USD, based in USD ")
plt.xlabel("Time")
plt.ylabel("Rate, CURRENCY/USD")
plt.legend()

plt.show()



