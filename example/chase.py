import numpy as np
import matplotlib.pyplot as plt

from sim.sim import Environment, Entity


class Missile(Entity):
    v_m = 10.

    def __init__(self, pos, vel):
        super().__init__()
        self.pos = pos
        self.vel = vel

    def step(self, dt):
        self.pos += self.vel * dt

    def access(self, other):
        self.vel = Missile.v_m * ((other.pos - self.pos) / np.linalg.norm(other.pos - self.pos))
        return self.vel


class Plane(Entity):
    def __init__(self, pos, vel):
        super().__init__()
        self.pos = pos
        self.vel = vel

    def step(self, dt):
        self.pos += self.vel * dt

    def access(self, other):
        return self.vel


class MovableEntity(Entity):
    def __init__(self, pos, vel, policy):
        super().__init__()
        self.pos = pos
        self.vel = vel
        self.policy = policy
        # self.set_param(**kwargs)

    def step(self, dt):
        self.pos += self.vel * dt

    def access(self, other):
        if self.policy == 'Fix':
            return self.vel
        elif self.policy == 'Chase':
            self.vel = Missile.v_m * ((other.pos - self.pos) / np.linalg.norm(other.pos - self.pos))
            return self.vel
        elif self.policy == 'ChaseNearest':
            pass


def print_env(env: Environment):
    print(env.children[0].pos, env.children[1].pos)


def test_missile():
    """ 测试导弹打飞机. """
    env = Environment()
    env.step_events.append(print_env)

    missile = env.add(Missile(pos=np.array([0., 0.]), vel=np.array([10., 10.])))
    plane = env.add(Plane(pos=np.array([0., 2.]), vel=np.array([5., 0.])))

    while not env.is_over():
        env.step()

    dist = np.linalg.norm(plane.pos - missile.pos)
    time_is_over = env.is_over()
    assert (dist < 0.1 or time_is_over)


def test_movable():
    env = Environment()
    env.step_events.append(print_env)

    plane = env.add(MovableEntity(pos=np.array([0., 10.]), vel=np.array([5., 0.]), policy='Fix'))
    missile = env.add(MovableEntity(pos=np.array([0., 0.]), vel=np.array([10., 10.]), policy='Chase'))
    # missile2 = MovableEntity(pos=np.array([]), vel=np.array([]), policy=ChaseNearest())

    while not env.is_over():
        env.step()
    dist = np.linalg.norm(plane.pos - missile.pos)
    time_is_over = env.is_over()
    assert (dist < 0.1 or time_is_over)

if __name__ == '__main__':
    test_missile()
