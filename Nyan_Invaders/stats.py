class Stats():
    """ Отслецивание статистики """

    def __init__(self):
        """ Инициализация статистики """
        self.reset_stats()
        self.run_game = True
        self.high_score = 0

    def reset_stats(self):
        """ real time statistic"""
        self.cat_left = 2
        self.score = 0