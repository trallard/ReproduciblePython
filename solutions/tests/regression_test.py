import unittest
import os
import sys

class FixturesTest(unittest.TestCase):

    #------------------- setup and teardown ---------------------------
    @classmethod
    def setUpClass(cls):
        print('\nin set up - this takes about 80 secs')

        from tests.write_fixtures import generate_fixture_hashes, unpickle_hash
        cls.hash_dict_new = generate_fixture_hashes()
        cls.hash_dict_original = unpickle_hash()
        # define dictionary keys for individual files for checking
        folder = 'temporary_test_fixtures'
        cls.corrmat = folder + '/corrmat_file.txt'
        cls.gm = folder + '/network-analysis/GlobalMeasures_corrmat_file_COST010.csv'
        cls.lm = folder + '/network-analysis/NodalMeasures_corrmat_file_COST010.csv'
        cls.rich = folder + '/network-analysis/RICH_CLUB_corrmat_file_COST010.csv'
        
    #--------------------------- Tests --------------------------------
    # Each of these tests checks that ourly newly generated version of
    # file_x matches the fixture version
    
    def test_corrmat_matches_fixture(self):
        # test new correlation matrix against fixture
        print('\ntesting new correlation matrix against fixture')
        self.assertEqual(self.hash_dict_new[self.corrmat],
                        self.hash_dict_original[self.corrmat])

    def test_lm_against_fixture(self):
        # test new local measures against fixture
        print('\ntesting new nodal measures against fixture')
        self.assertEqual(self.hash_dict_new[self.lm],
                        self.hash_dict_original[self.lm])
    
    def test_gm_against_fixture(self):
        # test new global measures against fixture
        print('\ntesting new global measures against fixture')
        self.assertEqual(self.hash_dict_new[self.gm],
                        self.hash_dict_original[self.gm])
    
    def test_rich_against_fixture(self):
        # test rich club against fixture
        print('\ntesting rich club against fixture')
        self.assertEqual(self.hash_dict_new[self.rich],
                        self.hash_dict_original[self.rich])

if __name__ == '__main__':