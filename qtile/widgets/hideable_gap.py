from libqtile.bar import Gap

class HideableGap(Gap):
    def __init__(self, size: int) -> None:
        super().__init__(size)
        self._saved_size = size

    def is_show(self) -> bool:
        return self._size != 0

    def show(self, is_show: bool = True) -> None:
        if is_show != self.is_show():
            if is_show:
                self._size = self._saved_size
            else:
                self._size = 0
