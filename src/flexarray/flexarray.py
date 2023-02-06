from toarray import toarray

class FlexArray:
    def __init__(self, data) -> None:
        self._array = toarray(data)

    @property
    def type(self) -> str:
        return self._array.typecode