# Mandarin Voice

(1) Create the following dir and copy your file to dir (suppose current dir is merlin/egs/mandarin_voice/s1/)

* database/wav 
* database/labels/label_phone_align 
* database/prompt-lab 

* cp your own question file (like questions-mandarin.hed) to ~/merlin/misc/questions/


(2) modify params as per your own data in 01_setup.sh file, especially

* Voice Name
* QuestionFile
* Labels
* SamplingFreq
* Train
* Valid
* Test

default setting is 

* QuestionFile=questions-mandarin.hed
* Labels=phone_align
* SamplingFreq=44100
* Train=40
* Valid=5
* Test=5



(3) then run

```
./run_mandarin_voice.sh
```
