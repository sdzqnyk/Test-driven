
class EntityIdGen:
    __global_entity_id: int = 0
    @staticmethod
    def gen():
        EntityIdGen.__global_entity_id += 1
        return EntityIdGen.__global_entity_id


class Entity:
    def __init__(self):
        self.__id = EntityIdGen.gen()

    def step(self, ti):
        """ 步进.
        :param ti: time information (dt, curr_time) 
        """
        pass

    def is_active(self) -> bool:
        return True
