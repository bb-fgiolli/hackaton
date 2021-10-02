import disney
import netflix

if __name__ == '__main__':
    Disney = disney.Disney()
    Disney.scraping()
    Netflix = netflix.Netflix()
    Netflix.main()