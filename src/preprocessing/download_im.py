import ssl
import urllib.request
import numpy as np
import pandas as pd
import json
import os
import sys

sys.path.append(r'F:\\UNIVERSITY\\UNIVERSITY_DOCUMENTS\\CS231\\doan_v2')
os.chdir(r'F:\\UNIVERSITY\\UNIVERSITY_DOCUMENTS\\CS231\\doan_v2')
print(os.listdir())

from utils import *

# Set up SSL context to allow legacy TLS versions
ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
ctx.options |= 0x4  # OP_LEGACY_SERVER_CONNECT


if __name__=='__main__':
    data_path = 'data/save_all_final_clean.json'
    save_path = 'images/'

    # URLS list
    data = load_json(data_path)
    # urls = [val['img_url'] for val in ]
    
    for id_film, val in data.items():
        url = val['img_url']
        filename = os.path.join(save_path, f'{id_film}.png')

        # Use urllib to open the URL and read the content
        try:
            response = urllib.request.urlopen(url, context=ctx)
            image_content = response.read()

            ## Write the content to a file
            with open(filename, "wb") as file:
                file.write(image_content)
                print(f"Download successfully filename {filename}")
        except Exception as e:
            print(f"Download failed filename {filename}")
            print(e)


