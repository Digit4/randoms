from bs4 import BeautifulSoup as soup
import requests, os

site = "https://srgrafo.com"
delimiter = ";"
comic = "/comic/"
folder_name = "Rimworld_Tales"
path_to_folder = "/home/dhavalp/Comics"#os.path.abspath('.')
comic_save_directory = os.path.join(path_to_folder, folder_name)



def download_previous():
    if not os.path.exists(comic_save_directory):
        os.makedirs(comic_save_directory)


    # save all the downloaded files in a database
    db_name = "rimworldtales.csv"
    db_loc = os.path.join(comic_save_directory, db_name)
    database = open(db_loc,'w')
    db_header =  "Sr. No.;Title;URL;Suggested_Music"


    for site_no in range(1,87):
        site_data = requests.get(site+comic+str(site_no), {'user-agent':'bot'+str(site_no)})
        site_soup = soup(site_data.text, 'html.parser')

        #Base panel stored in comic_panel
        comic_panel = site_soup.find('div', {'class':'panel'})
        comic_title = comic_panel.find('div',{'class':'panel-heading'}).h3.string
        comic_title = str(site_no) + '. ' + comic_title
        comic_url = site+'/'+str(site_no)
        # If any suggested music is present in website link the youtube in csv
        suggested_music = ""
        try:
            suggested_music = comic_panel.find('p',{'id':'comic-body'}).a['href']
        except:
            suggested_music = "N/A"

        # Extracting image tag from webpage and then using the source of the image to download the image
        comic_img_tag = comic_panel.find('img',{'class':'img-responsive'})
        comic_img_src = comic_img_tag['src']
        
        # the comic is saved by default at the current location of the .py file in a folder named 'Rimworld Tales'
        comic_save_name = os.path.join(comic_save_directory, comic_title)
        image_binary_data = requests.get(site+comic_img_src, {'user-agent':'downloader_bot'+str(site_no)}).content
        # image title format will be like: "1. Ruins of rimworld #1"
        with open(comic_save_name,'wb+') as image_file:
            image_file.write(image_binary_data)
            # write data format (1;title of image, url, suggested music{if any})
            write_data = str(site_no) + delimiter + comic_title + delimiter + comic_url + delimiter + suggested_music + "\n"
            database.write(write_data)
            print(write_data.rstrip('\n') + " :: data stored in rimworldtales.csv")
        
    database.close()

download_previous()