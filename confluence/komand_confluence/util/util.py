def normalize_page(p):
    p['created'] = p['created'].value + 'Z'
    p['modified'] = p['modified'].value + 'Z'
    if p['homePage'] == 'false':
        p['homePage'] = False
    else:
        p['homePage'] = True 

    if p['current'] == 'false':
        p['current'] = False
    else:
        p['current'] = True 

    return p 
