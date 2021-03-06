### 本项目自行设计的上下文标注

此上下文设计时尽可能考虑了可扩展性，如果需要在某一层级添加新的属性，在该层级后面添加新的未使用的匹配组合符即可。例如声韵母层添加p6属性，原标注格式改写为...=p5#p6_即可，问题集中其他问题的答案不受影响，只需添加新的问题即可。

设置此中文上下文标注和对应问题集时参考了 `HTS label <http://www.cs.columbia.edu/~ecooper/tts/lab_format.pdf>`_ 以及 `Merlin Questions <https://github.com/CSTR-Edinburgh/merlin/tree/master/misc/questions>`_ 

备注：
* 没有设计语调短语层和段落层
* 也没有设置重音标注
* @&#$!^-+=以及/A:/B:...的使用主要是为了正则表达式匹配方便，10个符号(@&#$!^-+=)共有100个匹配组合，即可以匹配100个属性
* 如果前后位置的基元不存在的话，用xx代替，例如 xx^sil-w+o=sh 

层级      |   标注格式
--------- | --------------
声韵母层  |  p1^p2-p3+p4=p5@
声调层    |  /A:a1-a2^a3@
字/音节层 |  /B:b1+b2@b3^b4^b5+b6#b7-b8-
词层      |  /C:c1_c2^c3#c4+c5+c6&
韵律词层  |  /D:d1=d2!d3@d4-d5&
韵律短语层 |  /E:e1| e2-e3@e4#e5&e6!e7-e8#
语句层     |  /F:f1^f2=f3_f4-f5!


还没有使用的匹配组合符号如下

, , , , , ^!, ^_, ^&, , ^|,  
, , , , , , , , -_, -|,  
, , , +|, +^, +_, , , +!, ,  
=^, =-, =+, ==, =|, =&, =#, , , ,  
@&, @+, @_, @=, @@, , , , @!, @|,  
, _+, _#, _=, _@, __, , _&, _!, _|,  
#^, ,#! , #=, #@, #_, , , ##, #|,  
, &=, &+, , &@, &_, &#, &&, &^, &|,  
!^, , !+, !=, , !_, !#, !&, !!, !|,  
|^, |_, |+, |=, |@, |#, , |&, |!, ||,  
  
  
原匹配组合符号 

^^, ^-, ^+, ^=, ^@, ^_, ^#, ^&, ^!, ^|,  
-^, --, -+, -=, -@, -_, -#, -&, -!, -|,  
+^, +-, ++, +=, +@, +_, +#, +&, +!, +|,  
=^, =-, =+, ==, =@, =_, =#, =&, =!, =|,  
@^, @-, @+, @=, @@, @_, @#, @&, @!, @|,  
_^, _-, _+, _=, _@, __, _#, _&, _!, _|,  
#^, #-, #+, #=, #@, #_, ##, #&, #!, #|,  
&^, &-, &+, &=, &@, &_, &#, &&, &!, &|,  
!^, !-, !+, !=, !@, !_, !#, !&, !!, !|,  
|^, |-, |+, |=, |@, |_, |#, |&, |!, ||,  
  
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
---- | ----
d1  |  前一个韵律词的音节数目
d2  |  当前韵律词的音节数目
d3  |  后一个韵律词的音节数目
d4  |  当前韵律词在韵律短语的位置（正序）
d5  |  当前韵律词在韵律短语的位置（倒序）
---- | ----
e1  |  前一韵律短语的音节数目
e2  |  当前韵律短语的音节数目
e3  |  后一韵律短语的音节数目
e4  |  前一韵律短语的韵律词个数
e5  |  当前韵律短语的韵律词个数
e6  |  后一韵律短语的韵律词个数
e7  |  当前韵律短语在语句中的位置（正序）
e8  |  当前韵律短语在语句中的位置（倒序）
---- | ----
f1  |  语句的语调类型
f2  |  语句的音节数目
f3  |  语句的词数目
f4  |  语句的韵律词数目
f5  |  语句的韵律短语数目
