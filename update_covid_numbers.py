import numpy as np
import pandas as pd

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

untracked_territories = ['AS', 'MP', 'VI', 'PR', 'GU']
df_new = pd.read_csv('https://api.covidtracking.com/v1/states/current.csv')
df_new['state'] = df_new['state'].apply(lambda r: states[r] if r not in untracked_territories else r)
df_new = df_new[~df_new['state'].isin(untracked_territories)].reset_index()
df_new = df_new[['state', 'positive', 'death', 'totalTestResults']]
df_new.columns = ['State', 'Infected', 'Deaths', 'Tested']

df_prod = pd.read_csv('./prod/COVID19_state.csv')
df_prod['Tested'], df_prod['Infected'], df_prod['Deaths'] = df_new['Tested'], df_new['Infected'], df_new['Deaths']
df_prod.to_csv('./prod/COVID19_state.csv', index=False)

