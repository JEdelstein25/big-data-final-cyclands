import pandas as pd
import numpy as np

def chicago_cleaning():
    df = pd.read_csv('/Users/jesseedelstein/Documents/Big Data/cyclands/data/chicago/cycling_safety_chicago.csv')
    df['SEVERITY'] = 0
    df.loc[df['MOST_SEVERE_INJURY'] == 'FATAL', 'SEVERITY'] = 1
    #df.loc[df['MOST_SEVERE_INJURY'] == 'INCAPACITATING INJURY', 'SEVERITY'] = 0
    #df.loc[df['MOST_SEVERE_INJURY'] == 'NONINCAPACITATING INJURY', 'SEVERITY'] = 5
    #df.loc[df['MOST_SEVERE_INJURY'] == 'REPORTED, NOT EVIDENT', 'SEVERITY'] = 3
    #df.loc[df['MOST_SEVERE_INJURY'] == 'NO INDICATION OF INJURY', 'SEVERITY'] = 1
    df['SEVERITY']
    dummies_df = pd.get_dummies(df[['WEATHER_CONDITION','LIGHTING_CONDITION',  'TRAFFIC_CONTROL_DEVICE', 'TRAFFICWAY_TYPE', 'ALIGNMENT', 'ROADWAY_SURFACE_COND', 'INTERSECTION_RELATED_I', 'PRIM_CONTRIBUTORY_CAUSE']])
    df = pd.concat([dummies_df,df[['POSTED_SPEED_LIMIT', 'LANE_CNT', 'SEVERITY']]], axis=1)
    df = df.dropna()
    #df = df[df['SEVERITY'] > 6]
    return df

def denver_cleaning():
    df = pd.read_csv('/Users/jesseedelstein/Documents/Big Data/cyclands/data/denver/cycling_safety_denver.csv')
    df['SEVERITY'] = 0
    df.loc[df['SERIOUSLY_INJURED'] == 1.0, 'SEVERITY'] = 1
    df.loc[df['FATALITIES'] == 1.0, 'SEVERITY'] = 1
    #df.loc[df['MOST_SEVERE_INJURY'] == 'NONINCAPACITATING INJURY', 'SEVERITY'] = 5
    #df.loc[df['MOST_SEVERE_INJURY'] == 'REPORTED, NOT EVIDENT', 'SEVERITY'] = 3
    #df.loc[df['MOST_SEVERE_INJURY'] == 'NO INDICATION OF INJURY', 'SEVERITY'] = 1
    dummies_df = pd.get_dummies(df[['HARMFUL_EVENT_SEQ_1', 'ROAD_LOCATION', 'ROAD_DESCRIPTION', 'ROAD_CONTOUR', 'ROAD_CONDITION', 'TU1_VEHICLE_TYPE', 'TU1_VEHICLE_MOVEMENT', 'TU1_DRIVER_ACTION', 'TU1_DRIVER_HUMANCONTRIBFACTOR', 'TU2_VEHICLE_TYPE', ]])
    df = pd.concat([dummies_df,df[['DISTRICT_ID', 'PEDESTRIAN_IND', 'SEVERITY']]], axis=1)
    df = df.dropna()
    return df
