import disney
#import netflix
import pymongo
import json

if __name__ == '__main__':
    Disney = disney.Disney()
    json_ = Disney.scraping()
    json_ = json.loads(json_)
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["HackatonBB-5"]
    mycol = mydb["top_10"]
    query = mycol.insert_many(json_)

    #print list of the _id values of the inserted documents:
    print(query.inserted_ids)
    #Netflix = netflix.Netflix()
    #Netflix.main()