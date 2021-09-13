# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class RinaPipeline:
    def __init__(self):
        pass
    def process_item(self, item, spider):
        with open('/home/tf-dev-01/workspace_sol/wn/rina/rina/wine.json', 'a', encoding='utf8') as f:
            jsonData = json.dumps(item._values, ensure_ascii=False)
            f.write(jsonData)
        return item

class Rinacsv:
    def __init__(self):
        pass
    def process_item(self, item, spider)
        import csv
# csv파일 저장
        with open('./wine1.csv', 'w',newline="") as f:
             writer = csv.writer(f)
            for row in item:
                writer.writerow(row)
# class RinaPipeline_excel:
#     import xlsxwriter

#     def __init__(self):
#         self.work=xlsxwriter.Workbook("./result_excel.xlsx")
#         self.worksheet=self.work.add_worksheet()
#         self.rowcount=1
#     def process_item(self, item, spider):
#         with open('/home/tf-dev-01/workspace_sol/wn/rina/rina/wine.json', 'a', encoding='utf8') as f:
#             jsonData = json.dumps(item._values, ensure_ascii=False)
#             f.write(jsonData)
#         return item
