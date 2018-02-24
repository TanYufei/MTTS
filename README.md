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

首先你需要一个中文语料库...目前网络上没有开源的中文语音合成语料库。中文语料库中至少需要包含文本和音频，当然你也可以使用thchs30中的数据，但是单个人的数据量太少，不足以合成优质的语音。

得到文本和音频(韵律标注是可选项)后， 根据本项目代码生成Label文件，在爱丁堡大学的语音合成开源项目[merlin](https://github.com/CSTR-Edinburgh/merlin)下进行训练，具体过程参见 [Mandarin_Voice](https://github.com/Jackiexiao/MTTS/tree/master/egs/mandarin_voice/s1)

## 上下文相关标注和问题集设计规则
* [上下文相关标注](https://github.com/Jackiexiao/MTTS/blob/master/misc/mandarin_label.md)
* [问题集](https://github.com/Jackiexiao/MTTS/blob/master/misc/questions-mandarin.hed)
* [问题集设计规则](https://github.com/Jackiexiao/MTTS/blob/master/docs/mddocs/question.md)

## 使用指南
### 1.环境与依赖
* 环境:python3.6
* 安装: `sudo ./tools/install_mtts.sh`
* 使用方法: `python src/mtts.py txtfile wav_directory_path output_directory_path`
* 结果: 生成label和forced align的textgrid文件在output_directory_path中，然后使用merlin即可合成语音，具体过程参见 [Mandarin_Voice](https://github.com/Jackiexiao/MTTS/tree/master/egs/mandarin_voice/s1)
* 注意:目前仅能处理纯中文文本，不可包含阿拉伯数字，英文字母等非中文文本

**txtfile文件内容**（左边编号，右边纯中文文本，中间以空格隔开）
```
A_01 这是一段文本
A_02 这是第二段文本
```
**wav_directory内容**（包含wav文件，文件命名需对应文本编号，采样率大于等于16khz）  
--A_01.wav  
--A_02.wav  

### 2.txt2label.py的说明

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
本项目使用[Montreal-Forced-Aligner](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner)进行中文的音频文本对齐。
1. 本项目Forced Align声学模型的训练使用了thchs30数据库，见misc/thchs30.zip，以及[字典文件](https://github.com/Jackiexiao/MTTS/blob/master/misc/mandarin_mtts.lexicon)
2. 如果你想使用mfa(montreal-forced-aligner)已经训练好的声学模型进行align，这里提供了所需要的 [中文字典文件](https://github.com/Jackiexiao/MTTS/blob/master/misc/mandarin-for-montreal-forced-aligner-pre-trained-model.lexicon)

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
s stands for silence that is longer than 100ms and the start && end silence of each sentence  
 
### 韵律标注
代码中#0表示词语的边界，#1表示韵律词，#2表示重音，#3表示韵律短语，#4表示语调短语。本项目规定词语比韵律词小，代码里自动进行了调整。当不输入韵律时也能够生成可用的label，不过合成的语音韵律感不强

### Merlin已知bug
* 在merlin/src/frontend/label_normalisation.py中，在903行后添加（函数 def wildcards2regex 中） ` question = question.replace('\\?', '.')` 这样可以支持对HTS风格的问题集中?的转换(本项目问题集使用了?）
* 在src/frontend/label_normalisation.py文件中 `frame_number = int((end_time - start_time) / 50000)` 修改为`frame_number = int(end_time/50000) - int(start_time / 50000)` 因为我的数据不是以帧为单位的，数据的时间信息不是50000整
* 如果使用44100的采样频率，应该修改所有conf中的framelength 和fw_alpha 为 framelength = 2048 fw_alpha = 0.76 （参数是world提取44100采样频率音频所使用的参数

## 贡献者：
* Jackiexiao
* willian56

