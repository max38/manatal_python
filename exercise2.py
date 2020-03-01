import random


class LotteryContainer(object):
    def __init__(self, number_ball):
        self.number_ball = number_ball
        self.balls = []
        self.reset()

    def reset(self):
        self.balls.clear()
        for i in range(1, self.number_ball+1):
            self.balls.append(i)

    def picking(self, number, sort_number=False):
        if not 0 <= number <= len(self.balls):
            raise ValueError("Number of picking must be between 0 and {}".format(len(self.balls)))
        
        # Version 1
        # picked_list = random.sample(self.balls, k=number)
        # self.balls = list(set(self.balls) - set(picked_list))

        # Version 2
        picked_list = []
        for i in range(0, number):
            idx = random.randrange(len(self.balls))
            picked_list.append(self.balls.pop(idx))
        
        if sort_number:
            picked_list.sort()

        return picked_list


if __name__== "__main__":
    c1 = LotteryContainer(50)
    print(c1.picking(10, True))
    c1.reset()
    print(c1.picking(10))
