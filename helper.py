import requests
from const import NEWS_URL
from keys import API_KEY

def get_top_news(country='gb', category='sports'): 
    """Get the TOP News"""
    
    response = requests.get(NEWS_URL.format(country,category, API_KEY))
    
    if response:
        data = response.json()
    else:

        data = None
    return data

 
def format_data(data):
    article_list = []

    for article in data['articles']:
        title = article['title']
        content = article['content']
        url = article['url']
        source_name = article['source']['name']

        insert_article = {
           'title':title,
           'content':content,
           'source_name':source_name,
           'url':url
       }
        article_list.append(insert_article)

    return article_list


def write_to_file(formatted_data=[],N=5):
    if N > len(formatted_data):
        raise ValueError('Please enter a smaller number')

    with open('articles.txt','w') as file:
        for article_number, article in enumerate(formatted_data):
            article_number=article_number+1
            if article_number > N:
                break
            title = str(article['title'])
            content=str(article['content'])
            source_name=str(article['source_name'])
            url=str(article['url'])

            file.write('-'*20 + '\n')   
            file.write('Article No.{article_num}:{title}\n'.format(article_num= article_number, title=title))
            file.write(content+'\n')
            file.write('Source:{src}\n'.format(src=source_name))
            file.write('URL:{url}\n'.format(url=url))
