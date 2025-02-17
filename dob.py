# DoberMan - Advanced Website Spider/Crawler/Scraper
# Created by: DamnBoy402
# Version: 1.1
# Color(Rich) variable & texting is from Meta AI no cap
# Credits:
# - Meta AI
# - Translate
"""
 (                              *                   
 )\ )           )             (  `                  
(()/(        ( /(    (   (    )\))(      )          
 /(_))   (   )\())  ))\  )(  ((_)()\  ( /(   (      
(_))_    )\ ((_)\  /((_)(()\ (_()((_) )(_))  )\ )   
 |   \  ((_)| |(_)(_))   ((_)|  \/  |((_)_  _(_/(   
 | |) |/ _ \| '_ \/ -_) | '_|| |\/| |/ _` || ' \))  
 |___/ \___/|_.__/\___| |_|  |_|  |_|\__,_||_||_|   
DoberMan Web Crawler - Extract all links from a website
By DamnBoy402
"""

import argparse
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import json
import os
import platform
import sys
from concurrent.futures import ThreadPoolExecutor

class dobconf:
    def __init__(self):
        self.dikunjung = set()
        self.internal = set()
        self.external = set()
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'DoberMan/1.0 (+https://example.com/doberman)'
        }

    def klin(self):
         if platform.system() == "Windows":
             os.system('cls')
         else:
             os.system('clear')

    def validator(self, url):
        parsed = urlparse(url)
        return parsed.scheme in ('http', 'https')
        
    def get(self, soup):
        title = soup.find('title')
        return title.text.strip() if title else 'No Title'

    def ekstrakurl(self, url, link2):
        try:
            response = self.session.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            links = set()
            
            for link in soup.find_all('a', href=True):
                link = urljoin(link2, link['href'])
                if self.validator(link):
                    links.add(link)
            
            return links, self.get(soup)
        
        except Exception as e:
            print(f"Error crawling {url}: {str(e)}")
            return set(), ''

    def crawl(self, url, max_depth=3, current_depth=1):
        if url in self.dikunjung or current_depth > max_depth:
            return
            
        print(f"Crawling: {url} (Depth: {current_depth})")
        self.dikunjung.add(url)
        
        try:
            links, title = self.ekstrakurl(url, url)
            
            parsed_base = urlparse(url)
            base_domain2 = parsed_base.netloc
            
            for link in links:
                parsed_link = urlparse(link)
                if parsed_link.netloc == base_domain2:
                    if link not in self.internal:
                        self.internal.add(link)
                        self.crawl(link, max_depth, current_depth + 1)
                else:
                    self.external.add(link)
        
        except KeyboardInterrupt:
            print("\nCrawling interrupted by user!")
            self.save()
            sys.exit(0)
        except Exception as e:
            print(f"Error processing {url}: {str(e)}")

    def save(self, format='txt'):
        results = {
            'internal_links': list(self.internal),
            'external_links': list(self.external),
            'visited_urls': list(self.dikunjung)
        }
        
        if format == 'json':
            with open('results.json', 'w') as f:
                json.dump(results, f, indent=2)
            print("Results saved to results.json")
        else:
            with open('results.txt', 'w') as f:
                f.write("=== Internal Links ===\n")
                f.write('\n'.join(results['internal_links']))
                f.write("\n\n=== External Links ===\n")
                f.write('\n'.join(results['external_links']))
                f.write("\n\n=== Visited URLs ===\n")
                f.write('\n'.join(results['visited_urls']))
            print("Results saved to results.txt")

def main():
    print(__doc__)
    print("="*60)
    print("DOBERMAN WEB CRAWLER | FAST AND AGGRESSIVE LINK EXTRACTOR")
    print("="*60)
    print("Credits:")
    print("- Developed by DamnBoyz")
    print("- Powered by Python Requests & BeautifulSoup")
    print("- Supported by Leviathan404CT\n")

def main2():
    parser = argparse.ArgumentParser(description='DoberMan Web Crawler')
    parser.add_argument('url', help='URL to crawl')
    parser.add_argument('-d', '--depth', type=int, default=3,
                        help='Maximum crawl depth (default: 3)')
    parser.add_argument('-f', '--format', choices=['txt', 'json'],
                        default='txt', help='Output format (default: txt)')
    parser.add_argument('-t', '--threads', type=int, default=5,
                        help='Number of threads (default: 5)')
    
    args = parser.parse_args()
    
    if not args.url.startswith(('http://', 'https://')):
        print("Error: Please include http:// or https:// in the URL")
        return
      
    crawler = dobconf()
    crawler.klin()
    
    main()
    
    try:
        with ThreadPoolExecutor(max_workers=args.threads) as executor:
            executor.submit(crawler.crawl, args.url, args.depth)
        
        crawler.save(args.format)
        
        print("\nCrawling Summary:")
        print(f"Total Internal Links Found: {len(crawler.internal)}")
        print(f"Total External Links Found: {len(crawler.external)}")
        print(f"Total Pages Crawled: {len(crawler.dikunjung)}")
    
    except Exception as e:
        print(f"Fatal error occurred: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main2()
    
# ★ Special Thanks To: ★
# - Noxs404
# - ChiroXploit404
# - FkzSec
# - Darkness
# - Leviathan404CyberTeam
# - Always Mikaelz
# - Fem|301
# - YhujinOS
# - Laten Cyber
# - Zull
# - HyperXclic!
# - NoTolerance - Ilham
# - C10F - Darkness
# And all contributors
# You are free to recode this tool, but don't forget to include the original developer!
# Copyright©2025 DoberMan Web Crawling
