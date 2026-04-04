import pandas as pd
from tasks import EasyTask, MediumTask, HardTask


class DataCleanEnv:
    def __init__(self, task_type):
        self.task_type = task_type
        self.task = self._get_task(task_type)
        self.df = None
        self.original_df = None
        self.step_count = 0
        self.completed = False
    
    def _get_task(self, task_type):
        if task_type == "easy":
            return EasyTask()
        elif task_type == "medium":
            return MediumTask()
        elif task_type == "hard":
            return HardTask()
        else:
            raise ValueError(f"Unknown task type: {task_type}")
    
    def reset(self):
        self.df = self.task.generate_data().copy()
        self.original_df = self.df.copy()
        self.step_count = 0
        self.completed = False
        return self.df
    
    def step(self, action):
        if action == "skip":
            reward = 0.0
        elif self.task_type == "easy":
            reward = self._apply_easy_action(action)
        elif self.task_type == "medium":
            reward = self._apply_medium_action(action)
        elif self.task_type == "hard":
            reward = self._apply_hard_action(action)
        else:
            reward = 0.0
        
        self.step_count += 1
        
        if self.task.check_completion(self.df) and not self.completed:
            reward = 1.0
            self.completed = True
        
        return self.df, reward, self.completed
    
    def _apply_easy_action(self, action):
        if action == "fill_missing_mean":
            for col in self.df.select_dtypes(include=[float, int]).columns:
                self.df[col] = self.df[col].fillna(self.df[col].mean())
            return 0.5
        elif action == "fill_missing_forward":
            self.df = self.df.fillna(method='ffill')
            return 0.5
        return 0.0
    
    def _apply_medium_action(self, action):
        if action == "strip_whitespace":
            for col in self.df.select_dtypes(include=['object']).columns:
                self.df[col] = self.df[col].str.strip()
            return 0.5
        elif action == "lowercase":
            for col in self.df.select_dtypes(include=['object']).columns:
                self.df[col] = self.df[col].str.lower()
            return 0.3
        return 0.0
    
    def _apply_hard_action(self, action):
        if action == "drop_duplicates":
            self.df = self.df.drop_duplicates().reset_index(drop=True)
            return 0.5
        elif action == "drop_duplicates_subset":
            self.df = self.df.drop_duplicates(subset=['id']).reset_index(drop=True)
            return 0.5
        return 0.0
