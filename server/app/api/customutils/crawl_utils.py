def parse_content_type1(soup, urlInfo):
    posts = []
    for post in soup.select('#jwxe_main_content > div > div.list_wrap > table > tbody > tr'):
        try:
            title = post.find('td', class_='title_comm').a.text.strip()
            link = urlInfo['link'] + \
                post.find('td', class_='title_comm').a['href']
            posts.append({
                'unit': urlInfo['name'],
                'code': urlInfo['code'],
                'boardName': urlInfo['boardName'],
                'title': title,
                'link': link
            })
        except:
            pass
    return posts


def parse_content_type2(soup, urlInfo):
    posts = []
    for post in soup.select('#contentsArea > table > tbody > tr'):
        try:
            title = post.find('td', class_='aleft').a.text.strip()
            link = '/'.join(urlInfo['link'].split('/')[:-1]) + \
                '/' + post.find('td', class_='aleft').a['href']
            posts.append({
                'unit': urlInfo['name'],
                'code': urlInfo['code'],
                'boardName': urlInfo['boardName'],
                'title': title,
                'link': link
            })
        except:
            pass
    return posts


def parse_content_type3(soup, urlInfo):
    posts = []
    lists = soup.select('tr[height]:not([bgcolor])')
    for post in lists:
        try:
            print(post)
            title = post.find('td', attrs={"align": "left"}).a.text.strip()
            link = 'http://software.ajou.ac.kr' + \
                post.find('td', attrs={"align": "left"}).a['href']
            posts.append({
                'unit': urlInfo['name'],
                'code': urlInfo['code'],
                'boardName': urlInfo['boardName'],
                'title': title,
                'link': link
            })
        except:
            pass
    return posts
