# MTTS基于Merlin的中文语音合成Demo

**ON_DEVELOPMENT**

Mandarin/Chinese Text to Speech based on statistical parametric speech synthesis using merlin toolkit

此项目为我本科毕业设计中的一部分

欢迎做语音合成的伙伴加我微信`explorerrr`交流探讨

[中文语音合成手册（整理中）](http://mtts.readthedocs.io/zh_CN/latest/#)  
[中文语音合成相关思维导图（更新中）](http://naotu.baidu.com/file/efd4f580e80ed57c7bef115f2d7d5813?token=9b6dd5d2e4bc5b95)  

## 合成语音效果

目前500短句训练的效果见example_file下的音频文件

## 如何复现

首先你需要一个中文语料库...目前网络上没有开源的中文语音合成语料库。中文语料库中至少需要包含文本和音频。

得到文本和音频后，你需要做文本音频的对齐forced alignment(见下面的说明)，得到音素的发音时长标注，韵律标注是可选项。
根据本项目代码生成Label文件，在爱丁堡大学的语音合成开源项目[merlin](https://github.com/CSTR-Edinburgh/merlin)下进行训练，具体过程参见 [Mandarin_Voice](https://github.com/Jackiexiao/MTTS/tree/master/egs/mandarin_voice/s1)

## 目前进展

目前实现了简单的自动文本转label程序，设计了上下文相关标注格式和对应的问题集，具体见misc文件夹。目前仅能处理纯中文文本，不可包含阿拉伯数字，英文字母等非中文文本

## 上下文相关标注和问题集设计规则
[上下文相关标注](https://github.com/Jackiexiao/MTTS/blob/master/misc/mandarin_label.md)
[问题集](https://github.com/Jackiexiao/MTTS/blob/master/misc/questions-mandarin.hed)
[问题集设计规则](https://github.com/Jackiexiao/MTTS/blob/master/docs/mddocs/question.md)

### TODO List
- [x] Forced Alignment 根据音频文件和文本生成发音时长标注

## 使用指南
### 1.环境与依赖
兼容python2.7-3.6，需要安装`pip install jieba pypinyin`
### 2.txt2label

lab, sfs 样例文件参见example_file文件夹

```
from mandarin_frontend import txt2label

result = txt2label('香港和澳门')
for line in result:
    print(line)

# 带韵律标记的文本也被支持
# result = txt2label('香港#1和#1澳门')

# 可加入发音时长文件，则lab中会附加上发音时长
# result = txt2label('香港和澳门', sfsfile='example.sfs')
```

生成Label如下
```
0 0 xx^xx-sil+x=iang1@/A:xx-xx^xx@/B:xx+xx@xx^xx^xx+xx#xx-xx-/C:xx_xx^xx#xx+xx+xx&/D:xx=xx!xx@xx-xx&/E:xx|xx-xx@xx#xx&xx!xx-xx#/F:xx^xx=xx_xx-xx!
0 0 xx^sil-x+iang1=g@/A:xx-1^3@/B:0+4@1^2^1+5#1-5-/C:xx_n^c#xx+2+1&/D:xx=5!xx@1-1&/E:xx|5-xx@xx#1&xx!1-1#/F:xx^5=3_1-1!
0 0 sil^x-iang1+g=ang3@/A:xx-1^3@/B:0+4@1^2^1+5#1-5-/C:xx_n^c#xx+2+1&/D:xx=5!xx@1-1&/E:xx|5-xx@xx#1&xx!1-1#/F:xx^5=3_1-1!
0 0 x^iang1-g+ang3=h@/A:1-3^2@/B:1+3@2^1^2+4#2-4-/C:xx_n^c#xx+2+1&/D:xx=5!xx@1-1&/E:xx|5-xx@xx#1&xx!1-1#/F:xx^5=3_1-1!
0 0 iang1^g-ang3+h=e2@/A:1-3^2@/B:1+3@2^1^2+4#2-4-/C:xx_n^c#xx+2+1&/D:xx=5!xx@1-1&/E:xx|5-xx@xx#1&xx!1-1#/F:xx^5=3_1-1!
0 0 g^ang3-h+e2=ao4@/A:3-2^4@/B:2+2@1^1^3+3#3-3-/C:n_c^n#2+1+2&/D:xx=5!xx@1-1&/E:xx|5-xx@xx#1&xx!1-1#/F:xx^5=3_1-1!
0 0 ang3^h-e2+ao4=m@/A:3-2^4@/B:2+2@1^1^3+3#3-3-/C:n_c^n#2+1+2&/D:xx=5!xx@1-1&/E:xx|5-xx@xx#1&xx!1-1#/F:xx^5=3_1-1!
0 0 h^e2-ao4+m=en2@/A:2-4^2@/B:3+1@1^2^4+2#4-2-/C:c_n^xx#1+2+xx&/D:xx=5!xx@1-1&/E:xx|5-xx@xx#1&xx!1-1#/F:xx^5=3_1-1!
0 0 e2^ao4-m+en2=sil@/A:4-2^xx@/B:4+0@2^1^5+1#5-1-/C:c_n^xx#1+2+xx&/D:xx=5!xx@1-1&/E:xx|5-xx@xx#1&xx!1-1#/F:xx^5=3_1-1!
0 0 ao4^m-en2+sil=xx@/A:4-2^xx@/B:4+0@2^1^5+1#5-1-/C:c_n^xx#1+2+xx&/D:xx=5!xx@1-1&/E:xx|5-xx@xx#1&xx!1-1#/F:xx^5=3_1-1!
0 0 m^en2-sil+xx=xx@/A:xx-xx^xx@/B:xx+xx@xx^xx^xx+xx#xx-xx-/C:xx_xx^xx#xx+xx+xx&/D:xx=xx!xx@xx-xx&/E:xx|xx-xx@xx#xx&xx!xx-xx#/F:xx^xx=xx_xx-xx!
```

### 3.merlin脚本
将egs/mandarin_voice复制到merlin对应文件夹下，然后根据egs/mandarin_voice/s1/README.md进行配置即可

### 4.forced-alignment
可使用[Montreal-Forced-Aligner](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner)进行中文的音频文本对齐。
1. 如果你想使用mfa(montreal-forced-aligner)已经训练好的声学模型进行align，这里提供了所需要的 [中文字典文件](https://github.com/Jackiexiao/MTTS/blob/master/misc/mandarin-for-montreal-forced-aligner-pre-trained-model.lexicon)
2. 由于mfa自带的声学模型音素集和本项目使用的音素集不同，想要通过本项目
合成label需要使用本项目的音素集训练声学模型并进行align。
所需要的[字典文件](https://github.com/Jackiexiao/MTTS/blob/master/misc/mandarin_mtts.lexicon)
准备必要的数据文件后，在montreal-forced-aligner目录运行命令，详见mfa官方文档，dictionary_path改成本项目字典文件所在路径
`bin/mfa_train_and_align corpus_directory dictionary_path output_directory [-o train-model.zip]`
3. 通过forced align得到textgrid文件后，通过src/forced_align.py
   将textgrid转化为本项目使用的sfs文件，具体见代码


## 一些说明
### sfs文件
['239100 s',   
'313000 a',   
'400000 b'   
'480000 s'   
......]  
a stands for consonant  
b stands for vowel  
d stands for silence that is shorter than 100ms  
s stands for silence that is longer than 100ms and the start && end  
silence of each sentence  
 
### 韵律标注
代码中#0表示词语的边界，#1表示韵律词，#2表示重音，#3表示韵律短语，#4表示语调短语。本项目规定词语比韵律词小，代码里自动进行了调整。当不输入韵律时也能够生成可用的label，不过合成的语音韵律感不强

### Merlin已知bug
* 在merlin/src/frontend/label_normalisation.py中，在903行后添加（函数 def wildcards2regex 中） ` question = question.replace('\\?', '.')` 这样可以支持对HTS风格的问题集中?的转换(本项目问题集使用了?）
* 在src/frontend/label_normalisation.py文件中 `frame_number = int((end_time - start_time) / 50000)` 修改为`frame_number = int(end_time/50000) - int(start_time / 50000)` 因为我的数据不是以帧为单位的，数据的时间信息不是50000整
* 如果使用44100的采样频率，应该修改所有conf中的framelength 和fw_alpha 为 framelength = 2048 fw_alpha = 0.76 （参数是world提取44100采样频率音频所使用的参数

## 贡献者：
* Jackiexiao
* willian56

