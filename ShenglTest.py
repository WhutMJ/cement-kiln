# -*- coding: utf-8 -*-

def doubtKH(kh):
    if kh < 0.667:
        return 'kh值过低'
    elif kh > 1:
        return 'kh值超标'
    else:
        return 'kh值正常'

def doubtSM(sm):
    if sm < 1.7:
        return 'sm值过低'
    elif sm > 2.7:
        return 'sm值超标'
    else:
        return 'sm值正常'

def doubtIM(im):
    if im < 0.9:
        return 'im值过低'
    elif im > 1.7:
        return 'im值超标'
    else:
        return 'im值正常'
