from sim import Environment, Entity


class StepEntity(Entity):
    def __init__(self, ds=1., da=0.1):
        super().__init__()
        self.value: int = 0
        self.ds = ds
        self.da = da

    def step(self, ti):
        self.value += self.ds

    def access(self, other):
        # for other in others:

        other.value -= self.da


def test_create_entity():
    obj = Entity()
    obj2 = Entity()
    assert (obj.id != obj2.id)


if __name__ == "__main__":
    test_create_entity()


def test_env():
    env = Environment()

    obj = env.add(StepEntity())
    assert (obj is not None)
    assert (len(env.children) == 1)

    obj2 = env.add(StepEntity())
    assert (obj2 is not None)
    assert (len(env.children) == 2)

    # obj3 = env.add(StepEntity())
    # assert (obj3 is not None)
    # assert (len(env.children) == 3)

    while not env.is_over():
        env.step()
        pass

    assert (env.is_over() is True)


def test_env2():
    env = Environment(dt=0.1)
    env.add(StepEntity())
    while not env.is_over():
        env.step()
