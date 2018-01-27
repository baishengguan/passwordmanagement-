# passwordmanagement-
用Python写的一个user-password管理小软件。


如何打包 .py 文件，请参考网站：http://www.pyinstaller.org
1. Install PyInstaller from PyPI: pip install pyinstaller
2. Go to your program’s directory and run: pyinstaller yourprogram.py；实际用的是：pyinstaller -F yourprogram.py

按照上述方式打包运行 .exe 会出现console窗口，命令更改为：pyinstaller -F -w yourprogram.py 即可
