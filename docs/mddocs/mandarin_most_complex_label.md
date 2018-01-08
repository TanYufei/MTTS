### 本项目自行设计的上下文标注（最复杂版本）(todo)

暂时未完成设计，请参考hts label中复杂的重音标注格式

此版本包括了
* 重音标注（以及相关的上下文属性集）

设计时尽可能考虑了扩展性，如需要在某一层级上改变，在层级之后为新的属性添加新的序号即可，本项目使用语料库为单句格式，因此没有段落层。

备注：
* 语调短语层保留为将来所需
* @&#$! 符号用于区分同一层级中不同类型的上下文标注
* 如果前后位置的基元不存在的话，用xx代替，例如 xx^sil-w+o=sh 

层级      |   标注格式
--------- | --------------
声韵母层  |  p1^p2-p3+p4=p5
声调层    |  /A:a1-a2-a3@a4-a5-a6
字/音节层 |  /B:b1-b2@b3-b4&b5-b6#b7-b8
词层      |  /C:c1-c2-c3@c4-c5-c6&c7-c8
韵律词层  |  /D:d1-d2-d3@d4-d5-d6&d7-d8
韵律短语层 |  /E:e1-e2-e3@e4-e5-e6&e7-e8-e9#e10-e11-e12$e13-e14!e15-e16-e17
语调短语层 |  /F:
语句层     |  /G:g1-g2-g3-g4-g5

标号  |  含义
---- | ----
p1  |  前前基元
p2  |  前一基元
p3  |  当前基元
p4  |  后一基元
p5  |  后后基元
---- | ----
a1  |  前一音节/字的声调
a2  |  当前音节/字的声调
a3  |  后一音节/字的声调
a4  |  前一音节/字是否重音
a5  |  当前音节/字是否重音
a6  |  后一音节/字是否重音
---- | ----
b1  |  当前音节/字到语句开始字的距离
b2  |  当前音节/字到语句结束字的距离
b3  |  当前音节/字在词中的位置（正序）
b4  |  当前音节/字在词中的位置（倒序）
b5  |  当前音节/字在韵律词中的位置（正序）
b6  |  当前音节/字在韵律词中的位置（倒序）
b7  |  当前音节/字在韵律短语中的位置（正序）
b8  |  当前音节/字在韵律短语中的位置（倒序）
---- | ----
c1  |  前一个词的词性
c2  |  当前词的词性
c3  |  后一个词的词性
c4  |  前一个词的音节数目
c5  |  当前词中的音节数目
c6  |  后一个词的音节数目
c7  |  当前词在韵律词中的位置（正序）
c8  |  当前词在韵律词中的位置（倒序）
---- | ----
d1  |  前一个韵律词的音节数目
d2  |  当前韵律词的音节数目
d3  |  后一个韵律词的音节数目
d4  |  前一个韵律词的词数目
d5  |  当前韵律词的词数目
d6  |  后一个韵律词的词数目
d7  |  当前韵律词在韵律短语的位置（正序）
d8  |  当前韵律词在韵律短语的位置（倒序）
---- | ----
e1  |  前一韵律短语的音节数目
e2  |  当前韵律短语的音节数目
e3  |  后一韵律短语的音节数目
e4  |  前一韵律短语的词数目
e5  |  当前韵律短语的词数目
e6  |  后一韵律短语的词数目
e7  |  前一韵律短语的韵律词个数
e8  |  当前韵律短语的韵律词个数
e9  |  后一韵律短语的韵律词个数
e10  |  前一韵律短语的语调类型
e11  |  当前韵律短语的语调类型
e12  |  后一韵律短语的语调类型
e13  |  当前韵律短语在语句中的位置（正序）
e14  |  当前韵律短语在语句中的位置（倒序）
e15  |  前一韵律短语重音的数量
e16  |  当前韵律短语重音的数量
e17  |  后一韵律短语重音的数量
---- | ----
g1  |  语句的语调类型
g2  |  语句的音节数目
g3  |  语句的词数目
g4  |  语句的韵律词数目
g5  |  语句的韵律短语数目

**可能的改进**

在声韵母层增加声韵母类型的标记，如

标号 | 含义
---- | ----
p6  |  前前基元的声韵母类型
p7  |  前一基元的声韵母类型
p8  |  当前基元的声韵母类型
p9  |  后一基元的声韵母类型
p10  |  后后基元的声韵母类型
