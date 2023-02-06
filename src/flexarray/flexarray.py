from typing import Any
from toarray import get_array
from array import array

class FlexArray:
    def __init__(self, data) -> None:
        self._array = get_array(data)

    @property
    def type(self) -> str:
        if type(self._array) is array:
            return self._array.typecode
        else:
            return 'o'

    @property
    def values(self) -> list:
        return list(self._array)

    def __setitem__(self, index, value) -> None:
        try:
            self._array[index] = value
        except:
            self.set_item(index, value)

    def __getitem__(self, index) -> Any:
        return self._array[index]

    def __iter__(self):
        return iter(self._array)

    def __repr__(self) -> str:
        return f'FlexArray({self.values}'

    def append_item(self, value) -> None:
        values = list(self._array) + [value]
        self._array = get_array(values)

    def set_item(self, index, value) -> None:
        values = list(self._array)
        values[index] = value
        self._array = get_array(values)

    def extend_items(self, values) -> None:
        values = list(self._array) + list(values)
        self._array = get_array(values)

    def append(self, value) -> None:
        try:
            self._array.append(value)
        except:
            self.append_item(value)

    def extend(self, values) -> None:
        try:
            self._array.extend(values)
        except:
            self.extend_items(values)
