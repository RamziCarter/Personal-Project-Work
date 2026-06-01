#Ramzi Carter Jr.
#05/26/2026

# End to end ML project
#This data is a modified version of a dataset from username:Ageron on github
#He modified the dataset which another user originally got from the now closed
#StatLib repository. This dataset appeared in a paper from 1997 titled: Sparse Spatial Autoregressions
#It was published in a statistics and probability letters journal using CA 1990 census data

#----------------------------------

#Clarifications
#Data set contains one row per block; a block is the smallest geographical group that the census publishes sample data (300-6000 people)
#207 values were removed at random from the total_bedrooms column and an ocean_proximity category was added to discuss categorical data
#block group was confusing for some in the terminology so they were renamed to districts

#MAE(Mean absolute Error) L1 norm, RMSE(Root Mean Square Error) L2 norm

#Script to download the data
from pathlib import Path
import pandas as pd
import tarfile
import urllib.request

def load_housing_data():
    tarball_Path = Path("datasets/housing.tgz")
    if not tarball_Path.is_file():
        Path("datasets").mkdir(parents=True, exist_ok=True)
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        urllib.request.urlretrieve(url, tarball_Path)
        with tarfile.open(tarball_Path) as housing_tarball:
            housing_tarball.extractall(path="datasets")
    return pd.read_csv("datasets/housing/housing.csv")

housing = load_housing_data()





