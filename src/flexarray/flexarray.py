from __future__ import annotations
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
            self._set_item(index, value)

    def __getitem__(self, index) -> Any:
        return self._array[index]

    def __delitem__(self, index) -> None:
        self.pop(index)

    def __iter__(self):
        return iter(self._array)

    def __repr__(self) -> str:
        return f'FlexArray({self.values}'

    def __len__(self) -> int:
        return len(self._array)

    def __add__(self, other) -> FlexArray:
        values = list(self._array) + list(other)
        return FlexArray(values)

    def __mul__(self, i: int) -> FlexArray:
        values = self._array * i
        return FlexArray(values)

    def __bool__(self) -> bool:
        return len(self) != 0

    def __contains__(self, value) -> bool:
        return value in self._array

    def __iadd__(self, value):
        self.append(value)

    def _append_item(self, value) -> None:
        values = list(self._array) + [value]
        self._array = get_array(values)

    def _set_item(self, index, value) -> None:
        values = list(self._array)
        values[index] = value
        self._array = get_array(values)

    def _extend_items(self, values) -> None:
        values = list(self._array) + list(values)
        self._array = get_array(values)

    def _insert_value(self, index, value) -> None:
        values = list(self._array)
        values.insert(index, value)
        self._array = get_array(values)

    def append(self, value) -> None:
        try:
            self._array.append(value)
        except:
            self._append_item(value)

    def extend(self, values) -> None:
        try:
            self._array.extend(values)
        except:
            self._extend_items(values)

    def insert(self, index, value) -> None:
        try:
            self._array.insert(index, value)
        except:
            self._insert_value(index, value)

    def pop(self, index=-1) -> Any:
        """Remove and return item at index (default last)."""
        out = self._array.pop(index)
        self._array = get_array(self._array)
        return out

    def remove(self, value) -> None:
        """Remove first occurrence of value."""
        self._array.remove(value)
        self.array = get_array(self._array)

    def index(self, value) -> int:
        """
        Return first index of value.

        Raises ValueError if the value is not present.
        """
        return self._array.index(value)

    def clear(self) -> None:
        """Remove all items from array."""
        self._array = get_array([])

    def copy(self) -> FlexArray:
        """Return a shallow copy of the FlexArray."""
        return FlexArray(self._array)

    def count(self, value) -> int:
        """Return number of occurrences of value."""
        return self._array.count(value)

    def reverse(self) -> None:
        """Reverse *IN PLACE*."""
        self._array.reverse()
    
    def sort(self, key=None, reverse=False) -> None:
        """Sort the values in ascending order and return None."""
        values = sorted(self._array, key=key, reverse=reverse)
        self._array = get_array(values)