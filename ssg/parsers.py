from typing import List
from pathlib import Path
import shutil

class Parser:
    """docstring for Parser."""
    extensions: List[str] = []

    def valid_extension(self, extention):
        if extention in self.extensions:
            return extention

    def parse(self, path, source, dest):
        try:
            self.path = Path(path)
            self.source = Path(source)
            self.dest = Path(dest)
        except NotImplementedError as e:
            print(f"{e!r}")
            raise

    def read(self, path):
        with open(path, mode='rt', encoding='utf-8') as file:
            return file.read()

    def write(self, path, dest, content, ext=".html"):
        full_path = self.dest / path.with_suffix(ext).name
        with open(full_path, mode='wt', encoding='utf-8') as file:
            file.write(content)

    def copy(self, path, source, dest):
        shutil.copy2(path,dest / path.relative_to(source))

class ResourceParser(Parser):
    """docstring for ."""
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path, source, dest):
        self.copy(path, source, dest)
