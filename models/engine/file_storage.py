#!/usr/bin/python3
"""Module for class FileStorage"""
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    if class_name == 'BaseModel':
                        module = __import__('models.base_model',
                                            fromlist=[class_name])
                    elif class_name == 'User':
                        module = __import__('models.user',
                                            fromlist=[class_name])
                    elif class_name == 'State':
                        module = __import__('models.state',
                                            fromlist=[class_name])
                    elif class_name == 'City':
                        module = __import__('models.city',
                                            fromlist=[class_name])
                    elif class_name == 'Amenity':
                        module = __import__('models.amenity',
                                            fromlist=[class_name])
                    elif class_name == 'Place':
                        module = __import__('models.place',
                                            fromlist=[class_name])
                    elif class_name == 'Review':
                        module = __import__('models.review',
                                            fromlist=[class_name])

                    cls = getattr(module, class_name)
                    obj = cls(**value)
                    self.new(obj)
        except FileNotFoundError:
            pass
