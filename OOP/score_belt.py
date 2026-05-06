SCORES = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
RANKS = 'white yellow orange green blue brown black paneled red'.split()
BELTS = dict(zip(SCORES, RANKS))


class NinjaBelt:

    def __init__(self, score=0):
        self._score = score
        self._last_earned_belt = None

    def _get_belt(self, new_score):
        eligible_scores = [score for score in SCORES if new_score >= score]
        if not eligible_scores:
            return None
        return BELTS[max(eligible_scores)]

    def _get_score(self):
        return self._score

    def message(self, status, score, rank=None):
        if status == 'new_belt':
            return (f'Congrats, you earned {score} points '
                    f'obtaining the PyBites Ninja {rank.title()} Belt')
        return f'Set new score to {score}'


    def _set_score(self, new_score):
        if not isinstance(new_score, int):
            raise ValueError('Score takes an int')

        if new_score < self._score:
            raise ValueError('Cannot lower score')

        current_belt = self._get_belt(self._score)
        new_belt = self._get_belt(new_score)
        self._score = new_score

        if new_belt is not None and new_belt != current_belt:
            self._last_earned_belt = new_belt
            print(self.message('new_belt', new_score, new_belt))
            return

        self._last_earned_belt = current_belt
        print(self.message('new_score', new_score))


    score = property(_get_score, _set_score)
