class MockDatabase:

    def __init__(self):
        self.data = {}

    def add_item(self, obj):
        self.data[obj.get('id_num')] = obj
        return self.data

    def delete_item(self, obj_id):
        self.data.pop(obj_id, None)
        return self.data

    def update_item(self, obj_id, field, new_info):
        self.data[obj_id][field] = new_info
        return self.data

    def append_new_item(self, obj_id, field, new_info):
        self.data[obj_id][field].append(new_info)
        return self.data

    def delete_sub_item(self, obj_id, field, sub_item):
        self.data[obj_id][field].remove(sub_item)
        return self.data


Users = MockDatabase()
Instruments = MockDatabase()
