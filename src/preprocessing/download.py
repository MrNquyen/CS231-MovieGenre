import gdown

def download_folder(url):
    gdown.download_folder(
        url=url,
        output='data',
    )


if __name__=='__main__':
    url = 'https://drive.google.com/drive/folders/1HyOP_dTqX3fsQJ0exXxrZqa1Cxn4qCZb?usp=sharing'
    download_folder(url)


