import re
from typing import Dict, Tuple


class Directory:
    FOLDER_REGX = r'^[a-zA-Z0-9_-]+$'

    def __init__(self, data: Dict = None):
        if data is None:
            data = {}
        self.dir = data

    def list(self) -> str:
        return self._output_dir()

    def delete(self, path: str) -> str:
        dist, name = self._get_dist_from_path(path, False)
        self._delete(dist, name)
        return f'DELETE {path}'

    def create(self, path: str) -> str:
        dist, name = self._get_dist_from_path(path, True)
        self._create(dist, name)
        return f'CREATE {path}'

    def move(self, from_path: str, to_path: str) -> str:
        from_dist, from_name = self._get_dist_from_path(from_path, False)
        to_dist, to_name = self._get_dist_from_path(to_path + "/" + from_name, True)
        self._create(to_dist, to_name, from_dist[from_name])
        self._delete(from_dist, from_name)
        return f'MOVE {from_path} {to_path}'

    def _create(self, dist: Dict, key: str, value: Dict = None) -> None:
        if value is None:
            value = {}
        dist[key] = value

    def _delete(self, dist: Dict, key: str) -> None:
        del dist[key]

    def _get_dist_from_path(self, path: str, new: bool = False) -> Tuple[Dict, str]:
        paths = path.split("/")
        curr = self.dir
        for k, name in enumerate(paths):
            is_filename = k == (len(paths) - 1)
            if not bool(re.match(self.FOLDER_REGX, name)):
                raise Exception(f'Invalid folder name {name} in the {path}')
            if not is_filename:
                if name not in curr.keys():
                    raise Exception(f'Can not found {name} in the {path}')
                curr = curr[name]
            else:
                if new:
                    if name in curr.keys():
                        raise Exception(f'Existing name {name} in the {path}')
                else:
                    if name not in curr.keys():
                        raise Exception(f'Can not found {name} in the {path}')
                return curr, name

        raise Exception('Should not reach here.')

    def _output_dir(self) -> str:
        return self._output_str(self.dir)

    def _output_str(self, data: Dict, prefix: str = '') -> str:
        output = ''
        # Sort before output
        data = dict(sorted(data.items()))
        for key, sub_data in data.items():
            output += f'{prefix}{key}\n'
            output += self._output_str(sub_data, prefix + '  ')
        return output
