# -*- coding: utf-8 -*-
import scrapy
import re

class ZpwSpider(scrapy.Spider):
    name = 'zpw'
    start_urls=['https://search.51job.com/list/170200%252C050000%252C120300%252C120200%252C01,000000,0000,00,9,99,Python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=']
    def parse(self, response):
        s1 = response.url[:106]
        s2 = response.url[-230:]
        s3 = response.url.replace(s1, '')
        s4 = s3.replace(s2, '')
        num = int(s4) + 1
        print(num)
        new_url = s1+'{}'.format(num)+s2
        selectors = response.xpath('//div[@class="el"]')
        for selector in selectors:
            next_url=selector.xpath('./p/span/a/@href').get()
            if next_url:
                yield scrapy.Request(next_url, callback=self.parseDetail)
        if num<2:
            yield scrapy.Request(new_url, callback=self.parse)

    #'''
    def parseDetail(self, response):
        dr = re.compile(r'<[^>]+>', re.S)
        html_url = response.url
        jobname=response.xpath('//div[@class="cn"]/h1/text()').get(default='')
        company_name=response.xpath('//p[@class="cname"]/a[1]/text()').get(default='')
        salary=response.xpath('//div[@class="cn"]/strong/text()').get(default='')
        joblocation=response.xpath('//div[@class="cn"]/p[2]/text()[1]').get(default='').replace('\xa0','')
        experience=response.xpath('//div[@class="cn"]/p[2]/text()[2]').get(default='').replace(' ','').replace('\xa0','')
        education=response.xpath('//div[@class="cn"]/p[2]/text()[3]').get(default='').replace('\xa0','')
        job_issue=response.xpath('//div[@class="cn"]/p[2]/text()[5]').get(default='').replace('\xa0','')[:-2]
        company_style=response.xpath('//div[@class="com_tag"]/p[1]/text()').get(default='')
        company_scale=response.xpath('//div[@class="com_tag"]/p[2]/text()').get(default='')
        job_industry=response.xpath('//div[@class="com_tag"]/p[3]/@title').get(default='')
        job_classification=response.xpath('//div[@class="mt10"]/p').get(default='').replace('职能类别：','')
        job_classification = dr.sub('', job_classification)
        job_content = response.xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div').extract()
        job_content = "".join(job_content).replace('\xa0','').replace('\r','').replace('\n','').replace('微信分享','')#
        job_content=job_content.replace(job_content[job_content.rfind('职能类别：'):],'')
        job_content = dr.sub('', job_content)
        job_content=job_content.replace(' ','')
        a = re.split(r'(工作要求：|任职要求：|任职资格：|岗位要求：|岗位职责：|工作职责：|岗位职能：|我们期望：|工作内容：'
                     r'|职位描述：|职位要求：|岗位职责:|招聘要求：|任职资格:|职责要求：|主要职责1)', job_content, 3)
        job_demand=''
        job_responsibility=''
        if len(a) == 5:
            if a[1] in ("岗位职责：", "工作职责：", "岗位职能：", '工作内容：', '关于职位：','任职资格：',
                        '职位描述：','职位要求','岗位职责:','招聘要求：','任职资格:','职责要求：','主要职责1'):
                job_responsibility = a[2]
                job_content = ""
            elif a[1] == 0:
                job_demand =  a[2]
                job_content = ""
                #print(job_demand)
            if a[3] in ("岗位职责：", "工作职责：", "岗位职能：", '工作内容：', '关于职位：','任职资格：'
                        ,'职位描述：','职位要求：','岗位职责:','招聘要求：','任职资格:','职责要求：','主要职责1'):              # 带上括号控制优先级
                job_responsibility =  a[4]
                job_content = ""
            else:
                job_demand =   a[4]
        else:
            pass
        if (salary):
            sal = salary.split('-')
            # print(len(sal))
            if len(sal) == 1:
                salary = salary
                salary_min = sal[0]
                salary_max = float(sal[0].split('/')[0][:-1])
                salary_method = sal[0].split('/')[0][-1:]
                salary_style = salary[-1:]
            else:
                salary = salary
                salary_min = float(sal[0])
                salary_max = float(sal[1].split('/')[0][:-1])
                salary_method = sal[1].split('/')[0][-1:]
                salary_style = salary[-1:]
        else:
            salary = None
            salary_min = None
            salary_max = None
            salary_method=None
            salary_style = None




        #print(job_content)

        items={
            'html_url':html_url,
            'jobname':jobname,
            'company_name':company_name,
            'salary':salary,
            'salary_min':salary_min,
            'salary_max':salary_max,
            'salary_method':salary_method,
            'salary_style':salary_style,
            'joblocation':joblocation,
            'experience':experience,
            'education':education,
            'job_issue':job_issue,
            'company_style':company_style,
            'company_scale':company_scale,
            'job_industry':job_industry,
            'job_classification':job_classification,
            'job_content':job_content,
            'job_responsibility':job_responsibility,
            'job_demand':job_demand
        }
        yield items
