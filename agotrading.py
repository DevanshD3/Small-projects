from datetime import date
from nsepy import get_history as gh
stk1 = gh(symbol='NIFTY',start=date(2015,1,1),end=date(2015,1,10), index=True)
print(stk1)