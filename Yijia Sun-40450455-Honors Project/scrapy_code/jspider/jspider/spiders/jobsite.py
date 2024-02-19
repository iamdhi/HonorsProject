# -*- coding: utf-8 -*-
import scrapy
import re
class JobsiteSpider(scrapy.Spider):
    name = 'jobsite'
    #allowed_domains = ['totaljobs.com']
    start_urls = ['https://www.jobsite.co.uk/jobs/php-developer/in-east-midlands']
    #start_urls = ['file:///C:/Users/HP/Desktop/zzz/nb1.html']
    #main_url=['https://www.totaljobs.com/job/']



    def parse(self, response):
        num=int(response.url[-6:-5])+1
        print(num)
        new_url='file:///C:/Users/HP/Desktop/zzz/nb{}.html'.format(num)
        print(new_url)
        selectors = response.xpath('//div[@class="job-title"]')
        for selector in selectors:
            #url=selector.xpath('./a/@href').get()
            next_href1 = selector.xpath('./a/@href').get()[54:]
            next_href = next_href1.replace('%2F', '/')
            next_url = 'https://www.totaljobs.com/job/' + next_href
            if next_url:
                yield scrapy.Request(next_url,callback=self.parseDetail)
        yield scrapy.Request(new_url,callback=self.parse)

#'''
    def parseDetail(self, response):
        html_url = response.url
        jobname=response.xpath('//h1[@class="brand-font"]/text()').get(default='').replace('\r\n','').replace('\t','').replace(' ','',8)
        jobissue=response.xpath('//li[contains(@class,"date")]/div/span/text()').get(default='')
        joblocation1 = response.xpath('//li[contains(@class,"location")]/div').get(default='')
        dr = re.compile(r'<[^>]+>', re.S)
        joblocation = dr.sub('', joblocation1)
        salary=response.xpath('//li[contains(@class,"salary")]/div/text()').get(default='')
        company_name=response.xpath('//li[contains(@class,"company")]/div/a/text()').get(default='')
        company_locations = response.xpath('//div[contains(@class,"col-xs-12 col-sm-7")]/ul').get(default='')
        company_location = dr.sub('', company_locations)
        job_contents = response.xpath('//div[@class="job-description"]/ul[1]').get(default='')
        job_content = dr.sub('', job_contents)
        job_descriptions = response.xpath('//div[@class="job-description"]/ul[2]').get(default='')
        job_description = dr.sub('', job_descriptions)
        job_style=response.xpath('//li[contains(@class,"job-type")]/div/text()').get(default='')
        #job_contents=response.xpath('//div[@class="content content-word"]/text()').extract()
        #job_content=''
        #for job in job_contents:
         #   job_content += job.replace('\r\n', '')
          #  #job_content=normalize-space()


        items={
            'jobname' : jobname,
            'html_url':html_url,
            'jobissue':jobissue,
            'joblocation':joblocation,
            #'education':education,
            #'experience':experience,

            'salary':salary,
            'company_name':company_name,
            #'company_industry':company_industry,
            #'company_scale':company_scale,
            'company_location':company_location,
            'job_content':job_content,
            'job_description':job_description,
            'job_style': job_style




        }
#'''
        yield items

