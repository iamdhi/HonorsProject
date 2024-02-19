# -*- coding: utf-8 -*-

# Scrapy settings for jspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jspider'

SPIDER_MODULES = ['jspider.spiders']
NEWSPIDER_MODULE = 'jspider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jspider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {

':authority':'www.jobsite.co.uk',
':method':'GET',
':path':'/jobs/java?page=6',
':scheme':'https',
'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding':'gzip,deflate,br',
'accept-language':'zh-CN,zh;q=0.9',
'cache-control':'max-age=0',
'cookie':'AnonymousUser=MemberId=e913829c-fe09-4fed-ba1f-53d4edbfd0af&IsAnonymous=True; visitorid=88f8320a-0b3a-47f2-ada9-cf4693d31bda; s_fid=481A92559B820F8B-04D3D098E7E33A28; __gads=ID=03605a9032c6ce1d:T=1578608475:S=ALNI_MaV6u5kdDk5hAK9KZl_o7cLeNw4IA; euconsent=BOmQYSHOmQYSHDDABBENCj-AAAAqJ7v______9______9uz_Ov_v_f__33e8__9v_l_7_-___u_-3zd4u_1vf99yfm1-7etr3tp_87ues2_Xur__79__3z3_9phP78k89r7337Ew-v83og; CONSENTMGR=c1:1%7Cc2:1%7Cc3:1%7Cc4:1%7Cc5:1%7Cc6:1%7Cc7:1%7Cc8:1%7Cc9:1%7Cc10:1%7Cc11:1%7Cc12:1%7Cc13:1%7Cc14:1%7Cc15:1%7Cts:1578614134815%7Cconsent:true; LOCATIONJOBTYPEID=null; INEU=1; PJBJOBSEEKER=1; sc_vid=21d85d3f8da280ab2355832d65072f82; s_cc=true; SessionCookie=f8a397e6-3bcc-4cdb-9de6-7e9558ecbb73; SearchKeywords=Java; gpv_pn=%2FJobSearch%2FResults.aspx; FreshUserTemp=https://www.jobsite.co.uk/jobs/java?page=6; TJG-Engage=1; SearchResults=89394407,89393609,89393602,89393766,89393730,89391547,89390259,89390242,89391204,89390030,89389042,89389009,89387888,89387471,89410652,89409561,89409973,89410151,89408549,89386117; EntryUrl=/jobs/java?page=6; s_sq=%5B%5BB%5D%5D; utag_main=v_id:016f8c65b69d0014045be2cb039c03072001a06a00bd0$_sn:9$_ss:0$_st:1580608812575$dc_visit:8$learninghub-courseKeywordSearches:undefined$learninghub-jobKeywordSearches:undefined$learninghub-lastKeyword:Data%20Analysis$ses_id:1580606874853%3Bexp-session$_pn:3%3Bexp-session$PersistedClusterId:OTHER--9999%3Bexp-session$PersistedFreshUserValue:0.1%3Bexp-session$dc_event:3%3Bexp-session$dc_region:eu-central-1%3Bexp-session; s_ppvl=%2FJobSearch%2FResults.aspx%2C13%2C13%2C969%2C993%2C969%2C1920%2C1080%2C1%2CP; s_ppv=%2FJobSearch%2FResults.aspx%2C12%2C12%2C969%2C993%2C969%2C1920%2C1080%2C1%2CP',
'referer':'https://www.jobsite.co.uk/jobs/java?page=5',
'sec-fetch-mode':'navigate',
'sec-fetch-site':'same-origin',
'sec-fetch-user':'?1',
'upgrade-insecure-requests':'1',
'user-agent':'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/79.0.3945.130Safari/537.36',




}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jspider.middlewares.JspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'jspider.middlewares.JspiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'jspider.pipelines.JspiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
