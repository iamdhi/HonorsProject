# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import re
from scrapy.exceptions import DropItem

class ZhipinPipeline(object):
    def process_item(self, item, spider):
        connect = pymysql.connect(
            host='localhost',
            user='root',
            passwd='123456',
            charset='utf8',
            db='liepin',
            use_unicode=False)

        cur = connect.cursor()
        cur.execute("use liepin")
        # table_name='liepinwang'
        # cur.execute('create table qcwy(_id int(5) NOT NULL AUTO_INCREMENT,html_url varchar(350), jobname varchar(100),company_name varchar(100),salary varchar(20),salary_min varchar(10),salary_max varchar(10),salary_method varchar(20),salary_style varchar(20),joblocation varchar(30),education varchar(20),experience varchar(20),job_issue varchar(20),company_style varchar(20),company_scale varchar(20),job_industry varchar(60),job_classification varchar(80),job_content varchar(2000),job_responsibility varchar(2000),job_demand varchar(2000),primary key (_id))AUTO_INCREMENT=1')
        data = {'html_url': item['html_url'], 'jobname': item['jobname'],'company_name':item['company_name'],
                'salary':item['salary'],'salary_min':item['salary_min'],'salary_max':item['salary_max'],
                'salary_method':item['salary_method'],'salary_style':item['salary_style'],'joblocation':item['joblocation'],
                'experience':item['experience'],'education':item['education'],'job_issue':item['job_issue'],
                'company_style':item['company_style'],'company_scale':item['company_scale'],'job_industry':item['job_industry'],
                'job_classification':item['job_classification'],'job_content':item['job_content'],'job_responsibility':item['job_responsibility'],'job_demand':item['job_demand']}
        # cur.execute('insert into liepinwang (jobname,jobissue,joblocation,education,experience,salary,company_name,company_industry,company_scale,companylocation,job_content) value("{jobname}","{jobissue}","{joblocation}","{education}","{experience}" ,"{salary}","{company_name}","{company_industry}","{company_scale}","{companylocation}","{job_content}");').format(item)

        html_url = data['html_url']
        jobname = data['jobname']
        company_name = data['company_name']
        salary = data['salary']
        salary_min = data['salary_min']
        salary_max = data['salary_max']
        salary_method = data['salary_method']
        salary_style = data['salary_style']
        joblocation = data['joblocation']
        education = data['education']
        experience = data['experience']
        job_issue = data['job_issue']
        company_style=data['company_style']
        company_scale = data['company_scale']
        #company_location = data['company_location']
        job_industry=data['job_industry']
        job_classification=data['job_classification']
        job_content = data['job_content']
        job_responsibility = data['job_responsibility']
        job_demand=data['job_demand']
        num = 0
        # cur.execute('insert into liepinwang(jobname,jobissue,joblocation,education,experience,salary,company_name,company_industry,company_scale,company_location,job_content)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
        # [jobname,jobissue,joblocation,education,experience,salary,company_name,company_industry,company_scale,company_location,job_content])
        try:
            numm = num + 1
            re = self.db_distinct(item['html_url'])
            if re:
                try:
                    cur.execute(
                        'insert into qcwy(html_url,jobname,company_name,salary,salary_min,salary_max,salary_method,salary_style,joblocation,education,experience,job_issue,company_style,company_scale,job_industry,job_classification,job_content,job_responsibility,job_demand)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                        [html_url, jobname, company_name,salary,salary_min,salary_max,salary_method,salary_style,joblocation,education,experience,job_issue,company_style,company_scale,job_industry,job_classification,job_content,job_responsibility,job_demand])
                    connect.commit()  # 每次上传后记得提交
                    print('success' + str(numm))
                except:
                    print('sql执行错误' + str(numm))
                    raise DropItem('sql执行错误')

            else:
                print('fail2' + str(numm))
                raise DropItem('数据已存在')
        except:

            connect.rollback()

            cur.close()
            connect.close()
        # sql=''
        # return item

    def db_distinct(self, html_url):
        connect = pymysql.connect(
            host='localhost',
            user='root',
            passwd='123456',
            charset='utf8',
            db='liepin',
            use_unicode=False)

        cur = connect.cursor()

        sql = 'select * from qcwy where html_url ="{}";'.format(html_url)

        cur.execute(sql)
        data = cur.fetchone()
        cur.close()
        if data == None:
            return True
        else:
            return False
