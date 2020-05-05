from bs4 import BeautifulSoup
import requests
import os
""" get the current file directory """
dir_path = os.path.dirname(os.path.realpath(__file__))


class Scarpy():
    @staticmethod
    def scrapy_function():
        with open(dir_path+'\simple.html') as file:
            soup = BeautifulSoup(file, 'html.parser')
        """ getting the title """
        print("***************getting the title******* \n")
        title = soup.title.text
        print("web title is {} \n".format(title))
        """ getting the first div """
        print("***************getting the first div******* \n")
        first_div = soup.div
        print("first div tag is {} \n".format(first_div))
        """ getting div with class= footer """
        print("***************getting div with class= footer******* \n")
        div_class = soup.find('div', class_="footer")
        print("div with class= footer \n {}".format(div_class))
        """ getting div with class article """
        print("***************getting div with class= article******* \n")
        div_article = soup.find('div', class_="article")
        print("div with class= article \n {}".format(div_article))
        """ getting text of link """
        print("**************getting text of <a> \n")
        print("text with within <a>  :{}".format(div_article.h2.a.text))
        print("text with within <p> :{}".format(div_article.p.text))
        print("\n\n using the find_all method ")
        for articls in soup.find_all('div', class_="article"):
            print("text with within <a>  :{}".format(articls.h2.a.text))
            print("text with within <p> :{}".format(articls.p.text))
