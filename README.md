# casl2-comment-generator
CASLⅡコメント自動生成プログラムです。\
入力されたcasファイルに形式的なコメントを付けて出力します。

入力ファイル例:
```
A   DC  10
B   DS  3
SMPL    START   MAIN
MAIN    LAD GR1,5    
    LD  GR1,A
    RET
    END
```
出力ファイル例:
```
A   DC  10  <A><-10
B   DS  3   ;allocate 3 words for B
SMPL    START   MAIN
MAIN    LAD GR1,5    ;GR1<-5
    LD  GR1,A   ;GR1<-(A)
    RET
    END
```