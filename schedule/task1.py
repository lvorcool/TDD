# coding:utf-8
# @Time  : 2020/4/20 17:23
# @Author: Xiawang
# Description:

class Flier(object):
    def __init__(self, report_status):
        self.report_status = report_status

    def fly(self, time):
        action = 'flying'
        self.report_status(time, action)


class Swimmer(object):
    def __init__(self, report_status):
        self.report_status = report_status

    def swim(self, time):
        action = 'swimming'
        self.report_status(time, action)


class Bird(object):

    def report_status(self, time, action):
        print(f"It's {time}, I'm {self.get_name()}, I'm {action}")

    def eat(self, time):
        action = 'eating'
        return self.report_status(time, action)

    def walk(self, time):
        action = 'walking'
        return self.report_status(time, action)

    def perform(self, time):
        action = 'performing'
        return self.report_status(time, action)

    def get_name(self):
        pass


class WildGoose(Bird, Flier, Swimmer):
    def __init__(self):
        Flier.__init__(self, self.report_status)
        Swimmer.__init__(self, self.report_status)

    def get_name(self):
        return 'WildGoose'


class Swallow(Bird, Flier):
    def __init__(self):
        Flier.__init__(self, self.report_status)

    def get_name(self):
        return 'Swallow'


class Penguin(Bird, Swimmer):
    def __init__(self):
        Swimmer.__init__(self, self.report_status)

    def get_name(self):
        return 'Penguin'


wild_goose = WildGoose()
swallow = Swallow()
penguin = Penguin()


class BuildHouse(Bird):
    def __init__(self, bird):
        self.bird = bird

    def builder(self, time):
        action = 'buiding a house'
        self.report_status(time, action)

    def get_name(self):
        return self.bird.get_name()


class Program(Bird):
    def __init__(self, bird):
        self.bird = bird

    def program(self, time):
        action = 'programing'
        self.report_status(time, action)

    def get_name(self):
        return self.bird.get_name()


birds: [Bird] = [wild_goose, swallow, penguin]

time = '7:00'
for bird in birds:
    bird.eat(time)

time = '8:00'
for bird in birds:
    bird.walk(time)

time = '9:00'
for bird in birds:
    bird.perform('9:00')

time = '10:00'
for bird in birds:
    if isinstance(bird, Flier):
        bird.fly(time)

time = '11:00'
for bird in birds:
    if isinstance(bird, Swimmer):
        bird.swim(time)

penguin_build = BuildHouse(penguin)
wild_goose_build = BuildHouse(wild_goose)
time = '13:00'
penguin_build.builder(time)
wild_goose_build.builder(time)

swallow_program = Program(swallow)
wild_goose_program = Program(wild_goose)
time = '14:00'
swallow_program.program(time)
wild_goose_program.program(time)
