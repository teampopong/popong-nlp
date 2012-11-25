#! /usr/bin/python3
# -*- coding: utf=8 -*-

def apply_rules(fieldname, fieldlist):
    if fieldname == 'education':
        fieldlist = education_rules(fieldlist)
    return fieldlist

def education_rules(fieldlist):
    abbrevs = {
        '대졸':'대학 졸업',
        '중졸':'중학교 졸업',
        '소졸':'소학교 졸업',
        '전졸':'전문대학 졸업',
        '고졸':'고등학교 졸업',
        '국졸':'국민학교 졸업',
        '보졸':'보통학교 졸업',
        '초졸':'초등학교 졸업',
        '고보졸':'고등보통학교 졸업',
        '대퇴':'대학 중퇴',
        }
 
    delwords = ['한문수학','한수','한문']

    # nullify
    def _nullify(item):
        if item in delwords:
            item = ''
        return item
    
    def nullify(fieldlist):
        return (_nullify(item) for item in fieldlist)

    # 약어 대체
    def _replace_abbrevs(item):
        return abbrevs.get(item, item)
 
    def replace_abbrevs(fieldlist):
        newlist = []
        for item in fieldlist:
            idx = item.find('(')
            if idx > 0:
                tmp = _replace_abbrevs(item[:idx])
                newlist.append(tmp + item[idx:])
            else:
                newlist.append(_replace_abbrevs(item))
        return newlist 
    
    # 졸업 여부 체크
    def _check_grad(item):
        if item.endswith('졸'):
            '''
            if len(item) == 2:
                item = item.replace(item[:-1], abbrevs.get(item[:-1],''))
                #item = '*' + item
            '''
            item = item.replace(item[-1], ' 졸업')

        elif item.endswith(('졸업','수료','중퇴','제적')):
            item = item[:-2] + ' ' + item[-2:]

        return item

    def check_grad(fieldlist):
        return (_check_grad(item) for item in fieldlist)

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

    fieldlist = nullify(fieldlist)
    fieldlist = replace_abbrevs(fieldlist)
    fieldlist = check_grad(fieldlist)
    fieldlist = check_countries(fieldlist)

    return fieldlist
