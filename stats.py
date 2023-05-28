class Stats():
    """отслеживание статистики"""

    def __init__(self):
        """инициализирует статистику"""
        self.reset_stats()
        self.run_game = True
        with open('high_score.txt', 'r') as f:
            self.high_score = int(f.readline())
        self.high_score =0

    def reset_stats(self):
        """статистика изменяющаяся во время игры"""
        self.gun_left = 3
        self.score = 0