import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    """docstring for ."""
    __delimeter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter,re.MULTILINE)

    @classmethod
    def load(cls, string):
        _, fm, content =  cls.__regex.split(string,2)
        metadata = load(fm, Loader=FullLoader)
        return cls(metadata,content)

    def __init__(self, metadata, content):
        self.data = metadata
        self.data["content"] = content

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        return self.data["type"] if "type" in self.data else None

    @type.setter
    def type(self):
        self.data["type"] = type

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        self.data.__iter__()

    def __len__(self):
        self.data.__len__()

    def __repr__(self):
        data = {}
        for key, value in self.data.items():
            if key != "content":
                value = data[key]
        return str(data)
