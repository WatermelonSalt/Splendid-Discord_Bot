import json
import os

from discord.ext import commands

from dotenv import load_dotenv

import requests

# Loading the environment variables from ".env"
load_dotenv("../../")

# Retriving the required environment variables from ".env"
TOKEN = os.getenv('DISCORD_TOKEN')
NEWS_KEY = os.getenv('NEWSAPI_KEY')
NAME = os.getenv('BOT_NAME')


# Definition of a Cog class
class news(commands.Cog):
    def __init__(self, bot):

        self.bot = bot

    # Declaration of a command "top-headlines" and a function "askfortopheadlines" which uses NEWS API to fetch results based on the options passed to it and atleast one option must be passed
    @commands.command(
        name="top-headlines",
        help='Usage : $#top-headlines "q=<keywords/topic>" "sources=<sources>" "language=<language(2-digit code)>" "country=<country>"\n\n"sources" and "country" switches cannot be used simultaneously!\n\nThe option "q" filters the results based on the provided keyword/string\n\nThe option "sources" is provided to specify the web sources from which to index the results\n\nThe option "language" is used to specify the language of the news. The option must be a two letter language code\n\nThe option "country" specifies the location of the news, it is also a two letter code\n\nValid options for country : ae|ar|at|au|be|bg|br|ca|ch|cn|co|cu|cz|de|eg|fr|gb|gr|hk|hu|id|ie|il|in|it|jp|kr|lt|lv|ma|mx|my|ng|nl|no|nz|ph|pl|pt|ro|rs|ru|sa|se|sg|si|sk|th|tr|tw|ua|us|ve|za --- These are the 2-letter ISO 3166-1 code of the country you want to get headlines for\n\nIf an option contains whitespaces, enclose them within quotes. The "sources" option takes more than one source to index, separate each source by a comma.\n\nEg:  $#top-headlines "q=bitcoin" "sources=BBC News,N-tv.de" "language=en"',
        pass_context=True)
    async def askfortopheadlines(self, ctx, *args):
        print(f'Arguments passed : {args}')

        url = self.typesettopheadlinesurl(args)
        topheadlines = requests.get(url)
        status, numberofresults, sourceid, sourcename, author, title, description, url, urltoimage, publishedat, content = self.decodejsonfromresult(
            topheadlines)
        print(f"`Status : {status}`")
        await ctx.author.send(f"`Status : {status}`")
        print(f"`Number of Results : {numberofresults}`")
        await ctx.author.send(f"`Number of Results : {numberofresults}`")
        print("`Only the first 20 results will be printed!`")
        await ctx.author.send("`Only the first 20 results will be printed!`")
        numberofitems = len(sourceid)
        for counter in range(0, numberofitems):
            print(
                f"{url[counter]}\n{urltoimage[counter]}\n```\nSource Id : {sourceid[counter]}\nSource Name : {sourcename[counter]}\n\nAuthor : {author[counter]}\n\nTitle : {title[counter]}\n\nDescription : {description[counter]}\n\nPublished At : {publishedat[counter]}\n\nContent : {content[counter]}\n```"
            )
            await ctx.author.send(f"{url[counter]}")
            await ctx.author.send(
                f"\n\n```\nSource Id : {sourceid[counter]}\nSource Name : {sourcename[counter]}\n\nAuthor : {author[counter]}\n\nTitle : {title[counter]}\n\nDescription : {description[counter]}\n\nPublished At : {publishedat[counter]}\n\nContent : {content[counter]}\n```\n\n\n\nDone!"
            )

    # Declaration of a command "everything" and a function "askforeverything" which uses NEWS API to fetch results based on the options passed to it and atleast one option must be passed
    @commands.command(
        name="everything",
        help='Usage : $#everything "q=<keywords/topic>" "domains=<domains>" "excludeDomains=<domains to exclude>" "from=<a date>" "to=<a date>" "sortBy=<relevancy/popularity/publishedAt>" "language=<language(2-digit code)>"\n\n"domains" and "excludeDomains" switches should not be used simultaneously!\n\nThe option "q" filters the results based on the provided keyword/string\n\nThe option "domains" is provided to specify the web domains from which to index the results\n\nThe option "language" is used to specify the language of the news. The option must be a two letter language code\n\nThe option "excludeDomains" specifies the domains from which the news should not be indexed\n\nIf an option contains whitespaces, enclose them within quotes. The "domains and excludeDomains" options take more than one domain to index, separate each source by a comma\n\nThe option "from" takes a date in "YYYY-MM-DD" format\n\nThe option "to" takes the date in "YYYY-MM-DD" format\n\nThe option "sortBy" option takes one of the followinf three options "relevancy/popularity/publishedAt"\n\nEg:  $#everything "q=bitcoin" "domains=techcrunch.com,thenextweb.com" "language=en" "from=2021-01-15" "to=2021-01-15" "sortBy=popularity"',
        pass_context=True)
    async def askforeverything(self, ctx, *args):
        print(f'Arguments passed : {args}')

        url = self.typeseteverythingurl(args)
        everything = requests.get(url)
        status, numberofresults, sourceid, sourcename, author, title, description, url, urltoimage, publishedat, content = self.decodejsonfromresult(
            everything)
        print(f"`Status : {status}`")
        await ctx.author.send(f"`Status : {status}`")
        print(f"`Number of Results : {numberofresults}`")
        await ctx.author.send(f"`Number of Results : {numberofresults}`")
        print("`Only the first 20 results will be printed!`")
        await ctx.author.send("`Only the first 20 results will be printed!`")
        numberofitems = len(sourceid)
        for counter in range(0, numberofitems):
            print(
                f"{url[counter]}\n{urltoimage[counter]}\n```\nSource Id : {sourceid[counter]}\nSource Name : {sourcename[counter]}\n\nAuthor : {author[counter]}\n\nTitle : {title[counter]}\n\nDescription : {description[counter]}\n\nPublished At : {publishedat[counter]}\n\nContent : {content[counter]}\n```"
            )
            await ctx.author.send(f"{url[counter]}")
            await ctx.author.send(
                f"\n\n```\nSource Id : {sourceid[counter]}\nSource Name : {sourcename[counter]}\n\nAuthor : {author[counter]}\n\nTitle : {title[counter]}\n\nDescription : {description[counter]}\n\nPublished At : {publishedat[counter]}\n\nContent : {content[counter]}\n```\n\n\n\nDone!"
            )

    # Definition of a function "decodejsonfromresult" which takes in the result from the "get" function and decodes the json
    def decodejsonfromresult(self, result):

        resolved = json.loads(result.content)
        sourceid = []
        sourcename = []
        author = []
        title = []
        description = []
        url = []
        urltoimage = []
        publishedat = []
        content = []

        try:
            status = resolved['status']
        except:
            status = ''
        try:
            numberofresults = resolved['totalResults']
        except:
            numberofresults = 0
        try:
            articles = resolved['articles']
        except:
            articles = []

        for article in articles:
            sourceid.append(article['source']['id'])
            sourcename.append(article['source']['name'])
            author.append(article['author'])
            title.append(article['title'])
            description.append(article['description'])
            url.append(article['url'])
            urltoimage.append(article['urlToImage'])
            publishedat.append(article['publishedAt'])
            content.append(article['content'])

        return status, numberofresults, sourceid, sourcename, author, title, description, url, urltoimage, publishedat, content

    # Definition of a function "typesettopheadlinesurl" which takes in the arguments from the command "top-headlines" and typesets the url which must be passed to the "get" function to fetch the results
    def typesettopheadlinesurl(self, listofargs):

        url = "http://newsapi.org/v2/top-headlines?"

        for argument in listofargs:
            url = url + f"{argument}&"

        url = url + f"apiKey={NEWS_KEY}"

        return url

    # Definition of a function "typeseteverythingurl" which takes in the arguments from the command "everything" and typesets the url which must be passed to the "get" function to fetch the results
    def typeseteverythingurl(self, listofargs):

        url = "http://newsapi.org/v2/everything?"

        for argument in listofargs:
            url = url + f"{argument}&"

        url = url + f"apiKey={NEWS_KEY}"

        return url


def setup(bot):

    bot.add_cog(news(bot))
