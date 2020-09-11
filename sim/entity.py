class EntityIdGen:
    __global_entity_id: int = 0

    @staticmethod
    def gen():
        EntityIdGen.__global_entity_id += 1
        return EntityIdGen.__global_entity_id


class Entity:
    def __init__(self):
        self.__id = EntityIdGen.gen()

    @property
    def id(self):
        return self.__id

    def step(self, ti):
        """ 步进.
        :param ti: time information (dt, curr_time) 
        """
        # dt, _ = ti
        # self.pos += self.vel * dt
        pass

    def access(self, other):
        """ 根据其他对象，改变自身状态"""
        pass

    def is_active(self) -> bool:

        return True
