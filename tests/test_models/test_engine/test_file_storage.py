import unittest
import os.path
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    def test_file_path(self):
        model = BaseModel()
        model.save()
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")
        os.remove("file.json")

    def test_all(self):
        storage = FileStorage()
        instances_dic = storage.all()
        self.assertIsNotNone(instances_dic)
        self.assertEqual(type(instances_dic), dict)
        self.assertIs(instances_dic, storage._FileStorage__objects)

    def test_new(self):
        storage = FileStorage()
        storage._FileStorage__objects = {}
        objects = storage._FileStorage__objects
        model = BaseModel()
        storage.new(model)
        self.assertNotEquals(objects[f"{model.__class__.__name__}.{model.id}"], None)

    def test_objects(self):
        FileStorage._FileStorage__objects = {}
        objects = FileStorage._FileStorage__objects
        model = BaseModel()
        model.save()
        self.assertEqual(type(objects), dict)
        os.remove("file.json")

    def test_save_with_reload(self):
        self.assertEqual(os.path.isfile("file.json"), False)
        obj = FileStorage._FileStorage__objects.copy()
        model = BaseModel()
        model.save()
        self.assertNotEqual(obj, FileStorage._FileStorage__objects)
        self.assertEqual(os.path.isfile("file.json"), True)
        os.remove("file.json")

    def test_reload(self):
        model = BaseModel()
        model.save()
        file_path = storage._FileStorage__file_path
        self.assertTrue(os.path.isfile(file_path))
        storage.reload()
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertTrue(key in storage.all().keys())
        reloaded_model = storage.all()[key]
        self.assertEqual(model.id, reloaded_model.id)
        self.assertEqual(model.created_at, reloaded_model.created_at)
        self.assertEqual(model.updated_at, reloaded_model.updated_at)
        os.remove(file_path)