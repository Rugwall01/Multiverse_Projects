import schedule
import time
import subprocess
import logging
import os


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_scrapy_spider():
    try:
        logger.info("Starting Scrapy spider...")
        subprocess.run(['scrapy', 'crawl', 'financial_spider'], check=True, cwd=os.path.join(os.path.dirname(__file__), '../scrapy_spider'))
        logger.info("Scrapy spider finished successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Scrapy spider failed: {e}")

schedule.every(15).minutes.do(run_scrapy_spider)

if __name__ == '__main__':
    logger.info("Scheduler started. Running Scrapy spider every 15 minutes.")
    run_scrapy_spider()  
    while True:
        schedule.run_pending()
        time.sleep(1)


