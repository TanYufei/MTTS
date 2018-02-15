import textgrid as tg
import os 

consonant = ['b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k',
                  'h', 'j', 'q', 'x', 'zh', 'ch', 'sh', 'r', 'z',
                  'c', 's', 'y', 'w']


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



def force_align(txt, wavfile):
    '''Return forced alignment of wav.
    
    Return:
        A list of forced alignment information. For example:
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
    '''
    pass

def textgrid2csv(textgrid_file, output_file):
    tgrid = tg.read_textgrid(textgrid_file)
    tg.write_csv(tgrid, output_file, sep=' ', header=False, meta=False)

def csv2sfs(csv_file, output_file):
    total_list = []
    with open(csv_file) as fid:
        for line in fid.readlines():
            #start, end, name, label = line.strip().split(' ')
            csv_list = line.strip().split(' ')
            if csv_list[3] == 'phones':
                total_list.append(_standard_sfs(csv_list))
    with open(output_file, 'w') as fid:
        for item in total_list:
            fid.write(' '.join(item) + '\n')

if __name__ == '__main__':
    # use textgrid to generate csv and sfs file
    grid_path = '/home/jackie/proj/MTTS/data/jackie_voice/textgrid/'
    sfs_path = '/home/jackie/proj/MTTS/data/jackie_voice/sfs/'
    csv_path = '/home/jackie/proj/MTTS/data/jackie_voice/csv/'
    for i in range(503)[1:]:
        if os.path.exists(grid_path+str(i)+'.TextGrid'):
            textgrid2csv(grid_path+str(i)+'.TextGrid', csv_path+str(i)+'.csv')
            csv2sfs(csv_path+str(i)+'.csv', sfs_path+str(i)+'.sfs')
        else:
            print('miss: ' + str(i) + ' file')

