# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import re
from scrapy.exceptions import DropItem

class JspiderPipeline(object):
    '''
    def table_exists(self, con, table_name):
        sql = "show tables;"
        con.execute(sql)
        tables = [con.fetchall()]
        table_list = re.findall('(\'.*?\')', str(tables))
        table_list = [re.sub("'", '', each) for each in table_list]
        if table_name in table_list:
            return 1
        else:
            return 0
'''

    def process_item(self, item, spider):
        connect = pymysql.connect(
            host='localhost',
            user='root',
            passwd='123456',
            charset='utf8',
            db='liepin',
            use_unicode=False)

        cur=connect.cursor()
        cur.execute("use liepin")
        #table_name='liepinwang'
        #cur.execute('create table jobsite(html_url varchar(350), jobname varchar(100),jobissue varchar(30),joblocation varchar(50),companylocation varchar(50),salary varchar(30),company_name varchar(50),job_content varchar(2000),job_description varchar(2000))')
        data = {'html_url':item['html_url'],
                'jobname': item['jobname'],
                'jobissue':item['jobissue'],
                'joblocation':item['joblocation'],
                'company_location':item['company_location'],
                'salary':item['salary'],
                'company_name':item['company_name'],
                'job_content':item['job_content'],
                'job_description':item['job_description'],
                'job_style':item['job_style']}
        #cur.execute('insert into liepinwang (jobname,jobissue,joblocation,education,experience,salary,company_name,company_industry,company_scale,companylocation,job_content) value("{jobname}","{jobissue}","{joblocation}","{education}","{experience}" ,"{salary}","{company_name}","{company_industry}","{company_scale}","{companylocation}","{job_content}");').format(item)
        html_url=data['html_url']
        jobname=data['jobname']
        jobissue=data['jobissue']
        joblocation=data['joblocation']
        company_location=data['company_location']
        #education=data['education']
        #experience=data['experience']
        salary=data['salary']
        company_name=data['company_name']
        #company_industry=data['company_industry']
        #company_scale=data['company_scale']
        #company_location=data['company_location']
        job_content=data['job_content']
        job_description=data['job_description']
        job_style=data['job_style']
        num=0
        #cur.execute('insert into liepinwang(jobname,jobissue,joblocation,education,experience,salary,company_name,company_industry,company_scale,company_location,job_content)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            #[jobname,jobissue,joblocation,education,experience,salary,company_name,company_industry,company_scale,company_location,job_content])
        try:
            re = self.db_distinct(item['html_url'])
            if re:
                try:
                    cur.execute('insert into jobsite(html_url,jobname,jobissue,joblocation,company_location,salary,company_name'
                                ',job_content,job_description,job_style)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                        [html_url,jobname,jobissue,joblocation,company_location,salary,company_name,job_content,job_description,job_style])
                    connect.commit()
                    print('sql insert success')
                except:
                    raise DropItem('sql run error')
            else:
                raise DropItem('data exists')
        except:
            connect.rollback()
            cur.close()
            connect.close()
        #sql=''
        #return item

    def db_distinct(self, html_url):
        connect = pymysql.connect(
        host='localhost',
        user='root',
        passwd='123456',
        charset='utf8',
        db='liepin',
        use_unicode=False)
        cur = connect.cursor()
        sql = 'select * from jobsite where html_url ="{}";'.format(html_url)
        cur.execute(sql)
        data = cur.fetchone()
        cur.close()
        if data == None:
            return True
        else:
            return False

