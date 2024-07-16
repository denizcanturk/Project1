# -*- encoding: utf-8 -*-
import sys
import io
from projectLibs.stokkontrolformu import StokKontrolFormu

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


if __name__ == "__main__":
    app = StokKontrolFormu()
    app.mainloop()
