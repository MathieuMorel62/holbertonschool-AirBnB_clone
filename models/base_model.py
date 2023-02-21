from datetime import datetime
import uuid


class BaseModel:
    """Defines the attributes and methods for all models."""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
    """Defines the attributes and methods"""
    def __init__(self, *args, **kwargs):
        """Initializes a new instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'update_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Updates the time of the last instance update and saves to storage."""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
