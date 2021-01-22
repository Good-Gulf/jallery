import jallery

if __name__ == '__main__':
    # print()
    jallery.what_is_what(jallery.pat)
    picpath = jallery.give_me_a_pic_path()
    print(picpath.__next__())
    print(picpath.__next__())
    print(picpath.__next__())
    # print(jallery.pict_list)
    # for _ in jallery.give_me_a_pic_path():
    #     print(_)
    # print(jallery.new_user('Ninde'))

