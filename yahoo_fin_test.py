import numpy as np
import matplotlib.pyplot as plt
from yahoo_fin import stock_info as si

print(si.get_live_price("aapl"))
past_year_data = si.get_data("aapl", start_date='11/25/2017')
plt.plot(past_year_data['close'])
plt.show()
