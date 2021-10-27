from typing import ItemsView


def sort_songs(song_titles, length_songs, key):
    if isinstance(song_titles, list) == False or \
        isinstance(length_songs, list) == False or\
            isinstance(key,callable) == False:
            return None
    if len(song_titles) != len(length_songs):
        return None
    else:
        zplist = list(zip(song_titles,length_songs))
        if key == "song_length":
            sl_zplist = return_sl(zplist)
            return sl_zplist
        elif key == "title_length":
            tl_zplist = return_tl(zplist)
            return tl_zplist
        elif key == "last_word":
            songtitles = []
            for i in song_titles:
                if i.count(" ") == 0:
                    songtitles.append(i[0])
                else:
                    i = str(i)
                    i = i.split()
                    i = i[-1]
                    i = " ".join(i)
                    songtitles.append(i[0])
            zpl = list(zip(songtitles, length_songs))
            zpl.sort(key = lambda numb: numb[0])
def return_sl(zplist):
    zplist.sort(key=lambda length: float(length[1]))
    return zplist
def return_tl(zplist):
    zplist.sort(key = lambda length: len(length[0]))
    return zplist

print(sort_songs(['Янанебібув', 'Той день', 'Мало мені', 'Сосни', 'Кавачай', 'Відпусти', 'Африка', 'Поясни', 'Фіалки', 'Коли тебе нема', 'Етюд'],['3.19', '3.58', '5.06', '4.31', '4.39', '3.52', '4.24','3.39', '3.43', '3.17', '2.21'],"last_word"))