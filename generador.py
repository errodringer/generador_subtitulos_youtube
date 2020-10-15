from googletrans import Translator

sub_file = 'subtitulos.txt'

file = open(sub_file, 'r', encoding='utf8')
full_file = file.read()
full_file = full_file.split('\n')

num_lines = len(full_file)

file_es = open('subtitulos_ES.srt', 'w', encoding='utf8')
file_en = open('subtitulos_EN.srt', 'w', encoding='utf8')

traductor = Translator()

counter = 1

for i in range(0, 10, 2):
    try:
        file_es.write(str(counter)+'\n')
        file_en.write(str(counter) + '\n')

        tiempos = '00:'+full_file[i]+',000'\
        +' --> ' + '00:'+full_file[i+2]+',000'
        file_es.write(tiempos + '\n')
        file_en.write(tiempos + '\n')

        text_es = full_file[i+1]
        file_es.write(text_es + '\n')
        text_en = traductor.translate(text_es, scr='es', dest='en').text
        file_en.write(text_en + '\n')

        file_es.write('\n')
        file_en.write('\n')

        counter+=1

    except:
        pass


file_es.close()
file_en.close()