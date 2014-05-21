import os
import tempfile


def _tmp_dir():
    tmp_root = "/tmp/perutest"
    os.makedirs(tmp_root, mode=0o777, exist_ok=True)
    return tempfile.mkdtemp(dir=tmp_root)


def create_dir(path_contents_map=None):
    dir = _tmp_dir()
    if path_contents_map is None:
        return dir
    for path, contents in path_contents_map.items():
        full_path = os.path.join(dir, path)
        full_parent = os.path.dirname(full_path)
        if not os.path.isdir(full_parent):
            os.makedirs(full_parent)
        with open(full_path, "w") as f:
            f.write(contents)
    return dir


def read_dir(dir):
    contents = {}
    for subdir, _, files in os.walk(dir):
        for file in files:
            path = os.path.normpath(os.path.join(subdir, file))
            with open(path) as f:
                content = f.read()
            relpath = os.path.relpath(path, dir)
            contents[relpath] = content
    return contents