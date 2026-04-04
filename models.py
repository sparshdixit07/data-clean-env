import pandas as pd


class RuleBasedModel:
    def __init__(self):
        self.name = "RuleBasedModel"
    
    def predict_action(self, df, task_type):
        if task_type == "easy":
            return self._easy_strategy(df)
        elif task_type == "medium":
            return self._medium_strategy(df)
        elif task_type == "hard":
            return self._hard_strategy(df)
        return "skip"
    
    def _easy_strategy(self, df):
        missing_count = df.isnull().sum().sum()
        if missing_count > 0:
            return "fill_missing_mean"
        return "skip"
    
    def _medium_strategy(self, df):
        non_stripped = False
        for col in df.select_dtypes(include=['object']).columns:
            if (df[col] != df[col].str.strip()).any():
                non_stripped = True
                break
        if non_stripped:
            return "strip_whitespace"
        return "skip"
    
    def _hard_strategy(self, df):
        duplicates = len(df) - len(df.drop_duplicates())
        if duplicates > 0:
            return "drop_duplicates"
        return "skip"
