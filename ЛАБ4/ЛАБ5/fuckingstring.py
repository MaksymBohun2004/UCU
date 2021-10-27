songtitles = []
song_titles = ['Янанебібув', 'Той день', 'Мало мені', 'Сосни', 'Кавачай', 'Відпусти', 'Африка', 'Поясни', 'Фіалки', 'Коли тебе нема', 'Етюд']
songtitles = []
length_songs = ['3.19', '3.58', '5.06', '4.31', '4.39', '3.52', '4.24','3.39', '3.43', '3.17', '2.21']
for i in song_titles:
    if i.count(" ") == 0:
        songtitles.append(i[0].lower())
    else:
        i = str(i)
        i = i.split()
        i = i[-1]
        i = " ".join(i)
        songtitles.append(i[0].lower())
zpl = list(zip(songtitles, length_songs))
zpl.sort(key = lambda numb: numb[0])
print(zpl)