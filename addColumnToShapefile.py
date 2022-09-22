# %%
import os
import geopandas as gpd
import  numpy as np
from shapely import geometry

#%%
os.chdir(rf'D:\Codebase')

df  = gpd.read_file(r'.\data\roads\roads.shp')
print(df.head()) #print first five rows in dataframe

highway_values  = df.highway.unique()
print(sorted(highway_values))

#%%
conditions = [
	(df['highway'] == 'primary') | (df['highway'] == 'primary_link'),
	(df['highway'] == 'secondary') | (df['highway'] == 'secondary_link'),
	(df['highway'] == 'tertiary') | (df['highway'] == 'tertiary_link'),
	(df['highway'] == 'trunk') | (df['highway'] == 'trunk_link')
]
values = [0,1,2,3]

df['ACCTYPE'] = np.select(conditions, values)

print(df.head())

#%%
#convert dataframe to shapefile
df = gpd.GeoDataFrame(df, geometry= 'geometry')
df.to_file(rf'.\data\roads\roads_edit.shp', driver = 'ESRI Shapefile')
# %%
print(df.head())
ACCTYPE_value = df.ACCTYPE.unique()
print(sorted(ACCTYPE_value))
# %%
