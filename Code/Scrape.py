# =============================================================================
# SCRAPING THE TABLE OF ALBERTA ENERGY EFFICIENCY CONTRACTORS
# https://medium.com/@ageitgey/quick-tip-the-easiest-way-to-grab-data-out-of-a-web-page-in-python-7153cecfca58
#Quick Tip: The easiest way to grab data out of a web page in Python
# =============================================================================

import numpy as np
import pandas as pd

# =============================================================================
# scrape, shorter version
# =============================================================================
url = 'https://www.efficiencyalberta.ca/home-improvement/windows-contractors-list/'

df, = pd.read_html(url)

del(df['Match Weight'])


# =============================================================================
# dupe check
# =============================================================================
sum(df.duplicated(['Business Name'], keep= False))

dupes =df[df.duplicated(['Business Name'], keep= False)]

df['Business Name'].value_counts(dropna=False)


# =============================================================================
# binary variables
# =============================================================================


List_of_Services = ['Windows', 'Insulation', 'Hot Water Tanks', 'DWHR', 'HVAC']

for Service in List_of_Services:
    df[Service] = np.where(df['Services Offered'].str.contains(Service, case=False, flags=0, regex=True),'yes','no')



for Service in List_of_Services:
    print()
    print (Service)
    print(df[Service].value_counts(dropna=False))
    print()


df.to_csv("contractors.csv", index=False)
