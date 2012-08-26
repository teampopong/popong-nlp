#! /usr/bin/python3
# -*- coding: utf=8 -*-

def apply_rules(fieldname, fieldlist):
    if fieldname == 'education':
        fieldlist = education_rules(fieldlist)
    return fieldlist

def education_rules(fieldlist):
    abbrevs = {'대':'대학',
        '중':'중학교',
        '소':'소학교',
        '전':'전문대학',
        '고':'고등학교',
        '국':'국민학교',
        '보':'보통학교',
        '초':'초등학교',
        }

    # item이 '졸'로 끝나는 경우 ' 졸업'으로 대체
    def _check_grad(item, abbrevs):
        def cng_grad(tmp):
            if tmp.endswith(('졸업','수료','중퇴')):
                tmp = tmp[:-2] + ' ' + tmp[-2:]
            if tmp.endswith('졸'):
                if len(tmp) == 2:
                    tmp = tmp.replace(tmp[0], abbrevs.get(tmp[0],''))
                    #tmp = '*' + tmp
                tmp = tmp.replace(tmp[-1], ' 졸업')
            return tmp       
        
        idx = item.find('(')
        if idx > 0:
            tmp = cng_grad(item[:idx])
            item = tmp + item[idx:]
        else:
            item = cng_grad(item)

        return item


    def check_grad(fieldlist, abbrevs):
        return (_check_grad(item, abbrevs) for item in fieldlist)

    # item이 '미국'으로 시작하는 경우 '미국 '으로 대체
    def _check_US(item):
        if item.startswith(('미국', '미 ')):
            item = item.replace(item[0:2], '미국 ')
        return item

    def _check_JP(item):
        if item.startswith('일본'):
            item = item.replace(item[0:2], '일본 ')
        return item

    def check_countries(fieldlist):
        fieldlist = (_check_US(item) for item in fieldlist)
        fieldlist = (_check_JP(item) for item in fieldlist)
        return fieldlist

    fieldlist = check_grad(fieldlist, abbrevs)
    fieldlist = check_countries(fieldlist)

    return fieldlist
