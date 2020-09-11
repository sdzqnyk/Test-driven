import unittest
import numpy as np
from sim.sim import Environment, Entity


class StepEntity(Entity):
    def __init__(self, pos, vel):
        super().__init__()
        self.pos = pos
        self.vel = vel
        self.value: int = 0

    def step(self, ti):
        self.value += 1
        dt, _ = ti
        self.pos += self.vel * dt

    def access(self, other):
        other.value -= 0.1


def print_env(env: Environment):
    print(env.children[0], env.children[1])


class TestEnv(unittest.TestCase):
    def test_create_entity(self):
        obj = Entity()
        self.assertTrue(obj is not None)

        obj2 = Entity()
        self.assertTrue(obj2 is not None)

        self.assertNotEqual(obj.id, obj2.id)

    def test_env(self):
        env = Environment()

        obj = env.add(StepEntity(pos=np.array([0., 10.]), vel=np.array([5., 0.])))
        # obj = env.add(StepEntity())
        self.assertTrue(obj is not None)
        self.assertEqual(len(env.children), 1)

        obj2 = env.add(StepEntity(pos=np.array([0., 0.]), vel=np.array([10., 10.])))
        # obj2 = env.add(StepEntity())
        self.assertTrue(obj2 is not None)
        self.assertEqual(len(env.children), 2)

        # obj3 = env.add(obj)
        # self.assertTrue(obj3 is not None)
        # self.assertEqual(len(env.children), 2)

        while not env.is_over():
            env.step_events.append(print_env)
            env.step()

        self.assertTrue(env.is_over())

    def test_env2(self):
        env = Environment(dt=0.1)
        env.add(StepEntity(pos=np.array([0., 0.]), vel=np.array([0., 0.])))
        while not env.is_over():
            env.step()
