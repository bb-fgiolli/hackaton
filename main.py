import disney
#import netflix
import starplus
import pymongo
import json

def scrap_and_insert():
    json_ = Disney.scraping()
    json_ = json.loads(json_)
    mycol.insert_many(json_)
    json_ = StarPlus.scraping()
    json_ = json.loads(json_)
    mycol.insert_many(json_)
    
if __name__ == '__main__':
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["HackatonBB-5"]
    mycol = mydb["top_10"]
    Disney = disney.Disney()
    StarPlus = starplus.StarPlus()
    scrap_and_insert()