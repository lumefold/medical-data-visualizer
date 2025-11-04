import unittest
import medical_data_visualizer
import pandas as pd
import os

class TestMedicalDataVisualizer(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.df = medical_data_visualizer.df
        cls.draw_cat_plot = medical_data_visualizer.draw_cat_plot
        cls.draw_heat_map = medical_data_visualizer.draw_heat_map
    
    def test_data_import(self):
        self.assertIsInstance(self.df, pd.DataFrame)
        self.assertGreater(len(self.df), 0)
    
    def test_overweight_column(self):
        self.assertIn('overweight', self.df.columns)
        self.assertTrue(self.df['overweight'].dtype in [int, bool])
    
    def test_normalized_data(self):
        self.assertTrue(set(self.df['cholesterol'].unique()).issubset({0, 1}))
        self.assertTrue(set(self.df['gluc'].unique()).issubset({0, 1}))
    
    def test_cat_plot_function(self):
        fig = self.draw_cat_plot()
        self.assertIsNotNone(fig)
    
    def test_heat_map_function(self):
        fig = self.draw_heat_map()
        self.assertIsNotNone(fig)

if __name__ == '__main__':
    unittest.main()