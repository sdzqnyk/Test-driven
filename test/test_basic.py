
import unittest

from sim import Environment, Entity
class StepEntity(Entity):
    def __init__(self):
        super().__init__()
        self.value : int = 0

    def step(self, ti):
        self.value += 1

class TestEnv(unittest.TestCase):
    def test_create_entity(self):
        obj = Entity()
        self.assertTrue(obj is not None)

        obj2 = Entity()
        self.assertTrue(obj2 is not None)

        self.assertNotEqual(obj.id, obj2.id)

    def test_env(self):
        env = Environment()
                
        obj = env.add(StepEntity())
        self.assertTrue(obj is not None)
        self.assertEqual(len(env.children), 1)
        
        obj2 = env.add(StepEntity())
        self.assertTrue(obj2 is not None)
        self.assertEqual(len(env.children), 2)

        obj3 = env.add(obj)
        self.assertTrue(obj3 is not None)
        self.assertEqual(len(env.children), 2)

        while not env.is_over():
            env.step()
            pass

        self.assertTrue(env.is_over())
        pass

    def test_env2(self):
        env = Environment(dt=0.1)
        env.add(StepEntity())
        while not env.is_over():
            env.step()
        pass



