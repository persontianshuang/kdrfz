import re

from datetime import datetime


def get_mark(any_mark):
    # print(clip_any)
    mes = [x for x in any_mark.split('\n') if x != '']
    # print(mes)
    name = re.sub('\ufeff','',mes[0])

    findPage = re.compile(r'(\d+[-]\d+)').findall(mes[1])[0]
    content = re.sub('\u200a','',mes[2])

    readDate = re.compile(r'(\d{4}年\d{1,2}月\d{1,2})').findall(mes[1])[0]
    read_date_list = [int(x) for x in re.split(r'[年月]',readDate)]
    read_datetime = datetime(read_date_list[0],read_date_list[1],read_date_list[2])

    data = {
        'book_raw_name': name,
        'book_simple_name': re.split(r'[（(]',name)[0],
        'read_time': read_datetime,
        'find_page': findPage,
        'content': content,
    }
    return data


def clip_to_data(clip_path):
    file = open(clip_path,'rt',encoding='utf8')
    clip = file.read()
    clip_list = clip.split('==========')
    all = []

    for index,clip_any in enumerate(clip_list):
        data = {}
        try:
            data = get_mark(clip_any)

        except:
            mes = [x for x in clip_any.split('\n') if x != '']
            if len(mes)==3:
                if '笔记' in mes[1]:
                    data = get_mark(clip_list[index+1])
                    note = re.sub('\u200a','',mes[2])
                    data['note'] = note
                    # print(data)
        if data != {}:
            all.append(data)
    for i,x in enumerate(all):
        if 'note' in x:
            all.pop(i+1)
    return all


if __name__ == '__main__':
    cc = clip_to_data('/Users/user/pynew/project/kinde_drf/first/My Clippings.txt')
    print(len(cc))
