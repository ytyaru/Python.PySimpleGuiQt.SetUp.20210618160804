# ラズパイではPySimpleGUIQtが使えない

　Raspberry PI では PySimpleGUIQt を実行できなかった。原因は`pip install PySide2`できないため。

　それぞれのライブラリは以下のように下のものを参照している。

* PySimpleGUIQt
	* PySide2
		* Python
		* C/C++
			* Qt

　だがRaspberry PIは`pip install PySide2`できないため、PySimpleGUIQtが実行できなかった。

## ラズパイで`pip install PySide2`できない

　原因はPySide2のARM版ビルドがないから。

　Raspberry PIのCPUはARMアーキテクチャである。ARM用にビルドされたPySide2のファイルが存在しないのが原因らしい。情報源は以下URL。

* [why-do-i-keep-getting-errors-when-i-try-to-install-pyside2-on-windows-pc](https://stackoverflow.com/questions/58743664/why-do-i-keep-getting-errors-when-i-try-to-install-pyside2-on-windows-pc)
* [installing-pyside2-on-raspberry-pi](https://forum.qt.io/topic/112813/installing-pyside2-on-raspberry-pi/2)

　補足。実行ファイルはCPUアーキテクチャごとに異なるバイナリが必要になる。CPUに合わせたバイナリ実行ファイルが必要だ。ところがPySide2にはARM用バイナリがない。そのためARMのCPUをもったラズパイで`pip install PySide2`を実行すると以下エラーになってしまう。

```sh
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Collecting PySide2
  Could not find a version that satisfies the requirement PySide2 (from versions: )
No matching distribution found for PySide2
```

## ラズパイの`apt`でPySide2をインストールする

　ラズパイでは`pip`でPySide2をインストールできない。それは先述のとおり。しかし、`apt`でインストールすることはできるようだ。詳細は[setup.sh](setup.sh)参照。

### `apt`でインストールしたPySide2ではPySimpleGUIQtから参照できない

　PySimpleGUIQtからPySide2を参照したコードを書いて実行すると、以下のようなエラーになってしまう。

```python
import PySimpleGUIQt as sg
...
```
```sh
ImportError: No module named PySide2.QtWidgets
```

　ただし、PySide2を直接参照するコードを書いて実行すると成功する。

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import exit, argv
from PySide2.QtWidgets import QApplication, QLabel

def Main():
    app = QApplication(argv)
    label = QLabel("Hello World")
    label.show()
    exit(app.exec_())

if __name__ == '__main__':
    Main()
```

　このことから、PySimpleGUIQtからPySide2を参照する点に問題があるとわかる。その原因は、`pip`でPySide2をインストールができず、やむなく`apt`でインストールしたせいだろう。

　結論。ラズパイではPySimpleGUIQtが使えない。理由はPySide2のARM用バイナリがないせいでPySimpleGUIQtがPySide2を参照できないため。

