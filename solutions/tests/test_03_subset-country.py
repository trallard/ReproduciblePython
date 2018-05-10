import importlib
import pandas.testing as pdt
import pandas as pd
import numpy.testing as npt


country = importlib.import_module('.data.03_country-subset', 'src')

interim_data = "data/interim/2018-05-09-winemag_priceGBP.csv"
processed_data = "data/processed/2018-05-09-winemag_Chile.csv"


def test_get_mean_price():
    """ Function used to test the mean function
    First uses assert to test for equivalence 
    then uses numpy (assert_allclose) to evaluate equality given 
    a tolerance
    """
    # compute the mean using the function
    mean_price = country.get_mean_price(processed_data)
    # equality
    assert mean_price == 20.7865
    # tolerance
    npt.assert_allclose(country.get_mean_price(processed_data), 20.787, rtol = 0.01)

def test_get_country():
    """Function used to verify the return object from the subset function 
    and verify whether this is the same as our base/control dataframe"""
    
    # create the subset and save in df
    df = country.get_country(interim_data, 'Chile')
    
    # use a previously verified dataframe
    base = pd.read_csv(processed_data)
    
    # am I getting a dataframe?
    assert isinstance(df, pd.DataFrame)
    assert isinstance(base, pd.DataFrame)
    
    # checks if our control and the new df are the same
    pdt.assert_frame_equal(df, base)