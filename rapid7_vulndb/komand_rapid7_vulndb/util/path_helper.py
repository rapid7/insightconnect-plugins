def set_xpath( data_base) -> dict:
    """
    Sets the xpath based on which data base the user wants to search.
    :param data_base: The data base to search.
    :return: the xpath (search parameters in dict form) and db. (a magic string that tells the browser what database to search)
    """
    if data_base == "Vulnerability Database":
        db = 'v'
        xpath = {'name': "//div/section/article/h4[@class='clearfix']/a/text()[1]",
                 'link': "//div/section/article/h4[@class='clearfix']/a/@href[1]",
                 'severity': "//*[@id='torso']/div/section/article[@class='vbResultItem']/ul[1]/li[1]/text()",
                 'type': '//*[@id="torso"]/div/section/article/h4/span/text()',
                 'summary': '//*[@id="torso"]/div/section/article/p[1]/text()',
                 'published': "//*[@id='torso']/div/section/article/ul[1]/li[2]/text()[1]"}
    elif data_base == "Metasploit Modules":
        db = 'm'
        xpath = {'name': '//*[@id="torso"]/div/section/div/h4/a/text()[1]',
                 'link': '//*[@id="torso"]/div/section/div/h4/a/@href[1]',
                 'module': '//*[@id="torso"]/div/section/div/h4/a/@href[1]',
                 'type': '//*[@id="torso"]/div/section/div/h4/span/text()',
                 'summary': '//*[@id="torso"]/div/section/div/p[2]/text()',
                 'published': '//*[@id="torso"]/div/section/div/p[1]/text()'}
    else:
        db = 'a'
        xpath = {'name': '//h4[@class]/a/text()',
                 'severity': "//*[@id='torso']/div/section/article[@class='vbResultItem']/ul[1]/li[1]/text()",
                 'type': '//*[@id="torso"]/div/section/article/h4/span/text()',
                 'summary': '//*[@id="torso"]/div/section/article/p/text()',
                 'published': "//*[@id='torso']/div/section/article/ul/li[2]/text()"}
    return {'xpath': xpath, 'db': db}
