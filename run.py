import time
from threading import Thread

from webcrawler.crawler import Crawler

if __name__ == "__main__":
    crawler = Crawler()

    # Add seed URLs
    crawler.queue_raw_url("http://reddit.com")
    #crawler.queue_raw_url('http://tv2.dk')

    # Start logger thread
    def logger():
        while True:
            print(f'{len(crawler.seen_urls)} seen URLs, {len(crawler.back_heap.get_hosts())} hosts, {len(crawler.back_queues)} back queues')

            time.sleep(5)

    thread = Thread(target=logger)
    thread.start()

    # Start crawler threads
    crawler.run_crawlers()
