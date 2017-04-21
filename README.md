## katadata.py
***
[class]  
Kata:kataminoの問題のクラス  
[variables]  
name:{str} 問題のID  
range:{list of int} 使用するミノの範囲  
minos:{list of int} 使用するミノのリスト  
***
[class]  
Katas：kataminoの問題リストを取り扱うクラス  
[method]  
append():Kataを追加する  
load_all():インスタンスに全問題を読み込む  
>return:{Katas}  

find_len():現在の問題リストから指定したミノ数を使う問題だけを取り出す
>arg:{int} 使うミノ数  
>return:{Katas}

find_minos():逆検索。指定したminosに一致する問題を探す
>arg:{list of int} minos  
>retrun:{Katas}

find_rminos():補集合逆検索。指定したminosの補集合に一致する問題を探す
>arg:{list of int} minos  
>retrun:{Katas}

find_name():名前に一致するKataを探す
>arg:{str} 問題ID  
>return:{Kata}

***