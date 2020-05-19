class MockDatabase:
    data = {}

    def __init__(self):
        pass

    @classmethod
    def add_item(cls, obj):
        cls.data[obj.get('id_num')] = obj
        return cls.data

    @classmethod
    def delete_item(cls, obj):
        cls.data[obj.get('id_num')] = obj
        return cls.data

    @classmethod
    def update_item(cls, obj):
        cls.data[obj.get('id_num')] = obj
        return cls.data


Users = MockDatabase()
Instruments = MockDatabase()
