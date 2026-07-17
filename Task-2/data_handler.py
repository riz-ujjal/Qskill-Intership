import pandas as pd

def load_gym_data(): 
    df = pd.read_csv('gym_data.csv')
    return(df.head())

