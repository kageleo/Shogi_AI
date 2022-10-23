#!/bin/zsh
# まず次のコマンドでスクリプトを実行可能にする。 chmod +x create_exe.sh 

pyinstaller main.py --onefile

# ./create_exe.sh　で実行