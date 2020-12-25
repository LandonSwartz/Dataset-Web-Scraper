#12.25.2020 Web Scrapper Script

#TODO add parallel processing for multiple search terms at once

import web_scrap
import argparse

def main():
    #path to driver
    DRIVER_PATH = r'C:\Users\Landon\Documents\Programming\Web_image_scrapper\chromedriver.exe'

    #arugment parser
    parser = argparse.ArgumentParser(description="Web scrapper for image collection")

    parser.add_argument("-q", "--query", help="Search query to be web scrapped for", required=True)
    parser.add_argument('-n', '--number', help='Number of links to fetch and images to save from search (optional). Default 5.',
                        default=5, type=int)
    parser.add_argument('-t', '--target', help='path to target folder (optional)', default='./images')

    args = parser.parse_args()

    #search and download
    web_scrap.search_and_download(search_term=args.query, driver_path=DRIVER_PATH, number_images=args.number, target_path=args.target)

if __name__ == "__main__":
    main()