class RecordScore():
    """Class to track a game's maximum score"""
    def __init__(self):
        self.current_score = None

    def __call__(self, score):
        if self.current_score is None or score > self.current_score:
            self.current_score = score
        return self.current_score
