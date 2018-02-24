import argparse
import os
import re
from pypinyin import pinyin, Style
import textgrid as tg
from mandarin_frontend import txt2label

consonant = ['b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k',
                  'h', 'j', 'q', 'x', 'zh', 'ch', 'sh', 'r', 'z',
                  'c', 's', 'y', 'w']


def _add_lab(txtlines, wav_dir_path):
    for line in txtlines:
        numstr, txt = line.split(' ')
        txt = re.sub('#\d', '', txt)
        pinyin_list = pinyin(txt, style = Style.TONE3)
        new_pinyin_list = []
        for item in pinyin_list:
            if not item[0][-1].isdigit():
                phone = item[0]+'5'
            else:
                phone = item[0]
            new_pinyin_list.append(phone)
            if phone == '5':
                print('error')
        lab_file = os.path.join(wav_dir_path, numstr + '.lab')
        with open(lab_file, 'w') as oid:
            oid.write(' '.join(new_pinyin_list))

def _txt_preprocess(txtfile):
    # 去除所有标点符号，报错，如果txt中含有数字和字母(报错并跳过）
    # todo 暂时不能处理包含韵律标注的文本
    with open(txtfile) as fid:
        txtlines = [x.strip() for x in fid.readlines()]
    valid_txtlines = []
    error_list = [] # line which contain number or alphabet
    for line in txtlines:
        num, txt = line.split(' ', 1)
        txt = re.sub('\W', '', txt)
        if bool(re.search('[A-Za-z0-9]', txt)):
            error_list.append(num)
        else:
            valid_txtlines.append(num + ' ' + txt)
    if error_list:
        for item in error_list:
            print('line %s contain number and alphabet!!' % item)
    return valid_txtlines

    # 去除所有标点符号，除了韵律标注#[0-9]+格式
    #    txtlines = [re.sub('(?!#[0-9]+)[\W]', '', x) for x in txtlines]

def _standard_sfs(csv_list):
    '''Change csv_list like "0 0.21 sil phones" to standard format like "2100000 s" '''
    def change2absd(phone, csv_list):
        if phone in consonant:
            return 'a'
        elif phone == 'sil' or phone == 'sp':
            if float(csv_list[1]) - float(csv_list[0]) > 0.1:
                return 's'
            else:
                #return 'd'
                return 's'
        else: #phone is vowel
            return 'b'
    standard_sfs_list = list((str(int(float(csv_list[1])*10e6)), 
                   change2absd(csv_list[2], csv_list)))
    return standard_sfs_list


def _mfa_align(txtlines, wav_dir_path, output_path):
    os.system('mkdir -p %s/wav' % output_path)
    os.system('ln -s %s %s/wav/mandarin_voice' % (wav_dir_path, output_path))
    os.system('../tools/montreal-forced-aligner/bin/mfa_align %s/wav ../misc/mandarin_mtts.lexicon ../misc/thchs30.zip %s/textgrid' %
            (output_path,output_path))

def _textgrid2sfs(txtlines, wav_dir_path, output_path):
    textgrid_path = os.path.join(output_path, 'textgrid/mandarin_voice')
    sfs_path = os.path.join(output_path , 'sfs')
    csv_path = os.path.join(output_path , 'csv')
    os.system('mkdir -p %s' % sfs_path)
    os.system('mkdir -p %s' % csv_path)

    for line in txtlines:
        numstr, txt = line.split()
        textgrid_file = os.path.join(textgrid_path , numstr + '.TextGrid')
        csv_file = os.path.join(csv_path , numstr + '.csv')
        sfs_file = os.path.join(sfs_path , numstr + '.sfs')

        if os.path.exists(textgrid_file):
            # textgrid to csv
            tgrid = tg.read_textgrid(textgrid_file)
            tg.write_csv(tgrid, csv_file, sep=' ', header=False, meta=False)

            # csv to sfs
            total_list = []
            with open(csv_file) as fid:
                for line in fid.readlines():
                    #start, end, name, label = line.strip().split(' ')
                    csv_list = line.strip().split(' ')
                    if csv_list[3] == 'phones':
                        total_list.append(_standard_sfs(csv_list))
            with open(sfs_file, 'w') as fid:
                for item in total_list:
                    fid.write(' '.join(item) + '\n')
        else:
            print('miss: ' + numstr + ' textgrid file')


def _sfs2label(txtlines, wav_dir_path, output_path):
    sfs_path = os.path.join(output_path ,'sfs')
    label_path = os.path.join(output_path, 'labels')
    os.system('mkdir -p %s/labels' % output_path)

    sfs_list = [x.replace('.sfs', '') for x in os.listdir(sfs_path)]

    for line in txtlines:
        numstr, txt = line.split()
        if numstr in sfs_list:
            sfs_file = os.path.join(sfs_path, numstr + '.sfs')
            label_file = os.path.join(label_path, numstr + '.lab')

            label_line = txt2label(txt, sfsfile=sfs_file)
            with open (label_file, 'w') as oid:
                for item in label_line:
                    oid.write(item + '\n')


def _delete_tmp_file(output_path):
    '''Delete tmp file like csv sfs'''
    pass

def generate_label(txtlines, wav_dir_path, output_path):
    _add_lab(txtlines, wav_dir_path)
    _mfa_align(txtlines, wav_dir_path, output_path)
    _textgrid2sfs(txtlines, wav_dir_path, output_path)
    _sfs2label(txtlines, wav_dir_path, output_path)
    _delete_tmp_file(output_path)
    print('Successful! The label files are in %s/labels' % output_path)


def main():
    parser = argparse.ArgumentParser(description="convert mandarin_txt and wav to label for merlin.")
    parser.add_argument("txtfile",
                        help="Full path to txtfile which each line contain num and txt (seperated by a white space) ")
    parser.add_argument("wav_dir_path",
                        help="Full path to a wav directory contain wav (sampling frequency should larger than 16khz)")
    parser.add_argument("output_path",
                        help="Full path to output directory, will be created if it doesn't exist")
    args = parser.parse_args()
    txtlines = _txt_preprocess(args.txtfile)

    output_path = os.path.abspath(args.output_path)
    wav_dir_path = os.path.abspath(args.wav_dir_path)

    os.system('mkdir -p %s' % args.output_path)
    generate_label(txtlines, wav_dir_path, output_path)
    # todo 把相对路径转换成绝对路径..

if __name__ == '__main__':
    main()

