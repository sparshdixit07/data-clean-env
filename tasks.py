import pandas as pd
import numpy as np


class Task:
    def __init__(self, name, task_type):
        self.name = name
        self.task_type = task_type
    
    def generate_data(self):
        raise NotImplementedError
    
    def get_actions(self):
        raise NotImplementedError
    
    def check_completion(self, df):
        raise NotImplementedError


class EasyTask(Task):
    def __init__(self):
        super().__init__("Easy Task - Fill Missing Values", "easy")
    
    def generate_data(self):
        data = {
            'name': ['Alice', 'Bob', None, 'David', None],
            'age': [25, None, 30, None, 35],
            'score': [85.0, 90.0, None, 88.0, 92.0]
        }
        return pd.DataFrame(data)
    
    def get_actions(self):
        return ['fill_missing_mean', 'fill_missing_forward', 'skip']
    
    def check_completion(self, df):
        return df.isnull().sum().sum() == 0


class MediumTask(Task):
    def __init__(self):
        super().__init__("Medium Task - Standardize Strings", "medium")
    
    def generate_data(self):
        data = {
            'product': ['  apple  ', 'banana ', ' orange', '  grape  ', 'melon'],
            'category': [' fruit ', 'fruit', 'fruit ', ' fruit', 'fruit']
        }
        return pd.DataFrame(data)
    
    def get_actions(self):
        return ['strip_whitespace', 'lowercase', 'skip']
    
    def check_completion(self, df):
        for col in df.select_dtypes(include=['object']).columns:
            if (df[col] != df[col].str.strip()).any():
                return False
        return True


class HardTask(Task):
    def __init__(self):
        super().__init__("Hard Task - Remove Duplicates", "hard")
    
    def generate_data(self):
        data = {
            'id': [1, 2, 2, 3, 1],
            'value': ['x', 'y', 'y', 'z', 'x']
        }
        return pd.DataFrame(data)
    
    def get_actions(self):
        return ['drop_duplicates', 'drop_duplicates_subset', 'skip']
    
    def check_completion(self, df):
        return len(df) == len(df.drop_duplicates())
