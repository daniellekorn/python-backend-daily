import json
import os
import time
from pathlib import Path


class MockDatabase:

    def __init__(self, name):
        self.data = {}
        self.name = name
        self.persist_as_json()

    def add_item(self, obj):
        self.data[obj.get('_id_num')] = obj
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

    def persist_as_json(self):
        while True:
            with open(f'{Path(__file__).parent}{os.sep}{self.name}.json', 'w') as f:
                json.dump(self.data, f)
                time.sleep(60)


Users = MockDatabase('users')
Instruments = MockDatabase('instruments')
