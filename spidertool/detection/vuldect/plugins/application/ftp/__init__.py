KEYWORDS = ['ftp', ]
def rules(head='',context='',ip='',port='',productname={},keywords='',hackresults=''):
    if port=='21':
        return True
    return False