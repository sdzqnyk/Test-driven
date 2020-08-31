

import unittest

import numpy as np
from sim import Environment, Entity

class Missile(Entity):
    pass

class Plane(Entity):
    
    def __init__(self, pos, v):
        super(Plane, self).__init__(pos)
        self.v = v

    def step(self, dt):
        self.pos += self.v * dt

    def access(self, other):        
        return self.v
    

class MovableEntity(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.position = None
        self.velocity = None

def print_env(env : Environment):
    print(env.children[0].pos, env.children[1].pos)

    pass

class ChaseTest(unittest.TestCase):
    def test_missile(self):
        """ 测试导弹打飞机. """
        env = Environment(dt=0.1)
        env.step_events.append(print_env)

        plane = env.add(Plane(position=np.array([0, 0], velocity=np.array([2, 0]))))
        missile = env.add(Missile(position=np.array([0, -100], speed=10))
        while not env.is_over():
            env.step()
        
        dist = np.linalg.norm(plane.position - missile.position)
        time_is_over = env.is_over()
        self.assertTrue(dist < 0.1 or time_is_over)

    def test_movable(self):
        env = Environment(dt=0.1)
        env.step_events.append(print_env)
        
        plane = MovableEntity(position=0, speed=2, policy=Fix())
        missile = MovableEntity(position=0, speed=2, policy=Chase(plane.id))
        missile2 = MovableEntity(position=0, speed=2, policy=ChaseNearest())
        
        while not env.is_over():
            env.step()
        
if __name__ = '__main__':
    unittest.main()

        

        

