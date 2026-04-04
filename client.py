from env import DataCleanEnv
from models import RuleBasedModel


class Client:
    def __init__(self, task_type):
        self.env = DataCleanEnv(task_type)
        self.model = RuleBasedModel()
        self.task_type = task_type
        self.total_reward = 0.0
    
    def run(self, max_steps=10):
        self.env.reset()
        self.total_reward = 0.0
        
        for step in range(max_steps):
            action = self.model.predict_action(self.env.df, self.task_type)
            df, reward, completed = self.env.step(action)
            self.total_reward += reward
            
            if completed:
                break
        
        return self.total_reward, self.env.df
    
    def get_score(self):
        return self.total_reward
