#--------------------------- Write fixtures ---------------------------
# To regression test our wrappers we need examples. This script 
# generates files. We save these files once, and regression_test.py
# re-generates these files to tests them for identicality with the
# presaved examples (fixtures). If they are found not to be identical 
# it throws up an error. 
#
# The point of this is to check that throughout the changes we make to 
# our package the functionality of this script stays the same
#------------------------------------------------------------------------

import os
import sys
import networkx as nx
             
def recreate_correlation_matrix_fixture(folder):
    ##### generate a correlation matrix in the given folder using #####
    ##### the Whitaker_Vertes dataset                             ##### 
    import BrainNetworksInPython.datasets.NSPN_WhitakerVertes_PNAS2016.data as data
    centroids, regionalmeasures, names, covars, names_308_style = data._get_data()
    from BrainNetworksInPython.wrappers.corrmat_from_regionalmeasures import corrmat_from_regionalmeasures
    corrmat_path = os.getcwd()+folder+'/corrmat_file.txt'
    corrmat_from_regionalmeasures(
        regionalmeasures,
        names, 
        corrmat_path,
        names_308_style=names_308_style)
     
def recreate_network_analysis_fixture(folder, corrmat_path):
    ##### generate network analysis in the given folder using the #####
    ##### data in example_data and the correlation matrix given   #####
    ##### by corrmat_path                                         #####  
    import BrainNetworksInPython.datasets.NSPN_WhitakerVertes_PNAS2016.data as data
    centroids, regionalmeasures, names, covars, names_308_style = data._get_data()
    # It is necessary to specify a random seed because 
    # network_analysis_from_corrmat generates random graphs to 
    # calculate global measures
    import random
    random.seed(2984)
    from BrainNetworksInPython.wrappers.network_analysis_from_corrmat import network_analysis_from_corrmat
    network_analysis_from_corrmat(corrmat_path,
                              names,
                              centroids,
                              os.getcwd()+folder+'/network-analysis',
                              cost=10,
                              n_rand=10, # this is not a reasonable 
                              # value for n, we generate only 10 random
                              # graphs to save time
                              names_308_style=names_308_style)
    
def write_fixtures(folder='/temporary_test_fixtures'): 
    ## Run functions corrmat_from_regionalmeasures and               ##
    ## network_analysis_from_corrmat to save corrmat in given folder ##
    ##---------------------------------------------------------------##
    # if the folder does not exist, create it
    if not os.path.isdir(os.getcwd()+folder):
        os.makedirs(os.getcwd()+folder)
    # generate and save the correlation matrix
    print("generating new correlation matrix") 
    recreate_correlation_matrix_fixture(folder)
    # generate and save the network analysis
    print("generating new network analysis") 
    corrmat_path = 'temporary_test_fixtures/corrmat_file.txt'
    recreate_network_analysis_fixture(folder, corrmat_path)
    
def delete_fixtures(folder):
        import shutil
        print('\ndeleting temporary files')
        shutil.rmtree(os.getcwd()+folder)
    
def hash_folder(folder='temporary_test_fixtures'):
    hashes = {}
    for path, directories, files in os.walk(folder):
        for file in sorted(files):
            hashes[os.path.join(path, file)] = hash_file(os.path.join(path, file))
        for dir in sorted(directories):
            hashes.update(hash_folder(os.path.join(path, dir)))
        break 
    return hashes
    

def hash_file(filename):
    import hashlib
    m = hashlib.sha256()
    with open(filename, 'rb') as f:
        while True:
            b = f.read(2**10) 
            if not b: break
            m.update(b)
    return m.hexdigest()

def generate_fixture_hashes(folder='temporary_test_fixtures'):
    # generate the fixtures
    write_fixtures("/"+folder)
    # calculate the hash
    hash_dict = hash_folder(folder)
    # delete the new files
    delete_fixtures("/"+folder)
    # return hash
    return hash_dict

def current_fixture_name():
    # returns the fixture name appropriate the current versions 
    # of python and networkx
    return "tests/.fixture_hash"+str(sys.version_info[:2])+'networkx_version'+str(nx.__version__)
    
def pickle_hash(hash_dict):
    import pickle
    # when we save we record the python and networkx versions
    with open(current_fixture_name(), 'wb') as f:
        pickle.dump(hash_dict, f)
    
def unpickle_hash():
    import pickle
    # import fixture relevant to the current python, networkx versions
    print('loading fixtures for python version {}, networkx version {}'.format(sys.version_info[:2], nx.__version__))
    with open(current_fixture_name(), "rb" ) as f:
        pickle_file = pickle.load( f )
    return pickle_file

if __name__ == '__main__':
    if input("Are you sure you want to update Brain Networks In Python's test fixtures? (y/n)") == 'y':
        hash_dict = generate_fixture_hashes()
        pickle_hash(hash_dict)