import numpy as np
import matplotlib.pyplot as plt
import copy

class SimClock:
    """ 仿真时钟. """
    def __init__(self, **kwargs):
        self.start = 0.0
        self.end = 10.0
        self.dt = 1.0
        self.now = 0.0
        self.set_params(**kwargs)

    def set_params(self, **kwargs):
        if 'dt' in kwargs:
            self.dt = float(kwargs['dt'])
        if 'end' in kwargs:
            self.end = float(kwargs['end'])
        if 'start' in kwargs:
            self.start = float(kwargs['start'])

    def step(self):
        self.now += self.dt

    def is_over(self) -> bool:
        return self.now > self.end

    @property
    def time_info(self):
        return self.dt, self.now


class Environment:
    def __init__(self, **kwargs):
        self._entities = []  # List[Entity]
        self._clock = SimClock()
        self.set_params(**kwargs)
        self.step_events = []

    def set_params(self, **kwargs):
        self._clock.set_params(**kwargs)

    @property
    def children(self):
        return self._entities

    def add(self, obj):
        if not self.find(obj):
            self._entities.append(obj)
        return obj

    def find(self, obj):
        return obj if obj in self._entities else None
    
    def step(self):
        self._clock.step()

        # 1.交互
        self.access()
        
        # 2.步进.
        active_objs = [obj for obj in self._entities if obj.is_active()]
        for obj in active_objs:
            obj.step(self._clock.time_info)

        # 3.处理事件.
        for evt in self.step_events:
            evt
    
    def access(self):
        children_copy = copy.deepcopy(self.children)
        for child in self.children:
            others = [obj for obj in children_copy if obj.id != child.id]
            for other in others:
                child.access(other)

    def is_over(self) -> bool:
        # time_is_over = self._clock.is_over()
        # active_objs = [obj for obj in self._entities if obj.is_active()] 
        # return time_is_over or len(active_objs) == 0
        return self._clock.is_over()