

import requests

cookies = {
    '_ga_SWJQXHKNTW': 'GS2.1.s1750882423$o1$g0$t1750882423$j60$l0$h0',
    '_ga': 'GA1.2.1661914141.1750882424',
    '_gid': 'GA1.2.1243320903.1750882424',
    '_ym_uid': '1750882425468778643',
    '_ym_d': '1750882425',
    '__gads': 'ID=d4eaf1f8199c62a1:T=1750882424:RT=1750882424:S=ALNI_MYnkPDSanCzIAZNh5QQvZvKaczm-Q',
    '__gpi': 'UID=00001139adb51592:T=1750882424:RT=1750882424:S=ALNI_MYWGdqvbmI0O602cG4ESx-AM0ci5w',
    '__eoi': 'ID=80ad4114cab930ec:T=1750882424:RT=1750882424:S=AA-AfjZ3uE1Wr4rzpTcrH5e7_UOD',
    '_ym_isad': '2',
    'FCNEC': '%5B%5B%22AKsRol_yuHy4GtUiJ-F8ZcLp9ryplaiYfKx-fi1iJ5C6vIO_10BpE5dZYJ2DQx0xnfzBGSaQFLUerJJeqSDNcckbGw_-VdoE4uEb96QzeQbnRDVjLTh9ZPqjfBsnhWsb9sq8C9epXFVE7lNHsBA1lw7oR3fZaPZL9A%3D%3D%22%5D%5D',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:140.0) Gecko/20100101 Firefox/140.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Alt-Used': 'this-person-does-not-exist.com',
    'Connection': 'keep-alive',
    'Referer': 'https://this-person-does-not-exist.com/en',
    # 'Cookie': '_ga_SWJQXHKNTW=GS2.1.s1750882423$o1$g0$t1750882423$j60$l0$h0; _ga=GA1.2.1661914141.1750882424; _gid=GA1.2.1243320903.1750882424; _ym_uid=1750882425468778643; _ym_d=1750882425; __gads=ID=d4eaf1f8199c62a1:T=1750882424:RT=1750882424:S=ALNI_MYnkPDSanCzIAZNh5QQvZvKaczm-Q; __gpi=UID=00001139adb51592:T=1750882424:RT=1750882424:S=ALNI_MYWGdqvbmI0O602cG4ESx-AM0ci5w; __eoi=ID=80ad4114cab930ec:T=1750882424:RT=1750882424:S=AA-AfjZ3uE1Wr4rzpTcrH5e7_UOD; _ym_isad=2; FCNEC=%5B%5B%22AKsRol_yuHy4GtUiJ-F8ZcLp9ryplaiYfKx-fi1iJ5C6vIO_10BpE5dZYJ2DQx0xnfzBGSaQFLUerJJeqSDNcckbGw_-VdoE4uEb96QzeQbnRDVjLTh9ZPqjfBsnhWsb9sq8C9epXFVE7lNHsBA1lw7oR3fZaPZL9A%3D%3D%22%5D%5D',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Priority': 'u=0',
}


base_url="https://this-person-does-not-exist.com"

import os 
folder_path = 'images'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)


def download_image(image_url, filename):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(os.path.join(folder_path, filename), 'wb') as file:
            file.write(response.content)
        print(f"Image saved as {filename}")
    else:
        raise Exception(f"Error downloading image: {response.status_code} - {response.text}")

def get_random_images(gender='all', age='all', etnic='all'):
    response = requests.get(
        f'{base_url}/new?time=1750883285644^&gender={gender}^&age={age}^&etnic={etnic}',
        cookies=cookies,
        headers=headers,
    )
    data = response.json()
    if response.status_code == 200:
        img_url= base_url+data['src']
        return img_url
    else:
        raise Exception(f"Error fetching data: {response.status_code} - {response.text}")
    


def main(number_of_images=5):
    for i in range(number_of_images):
        try:
            img_url = get_random_images()
            filename = f'random_person_{i+1}.jpg'
            download_image(img_url, filename)
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    num= 5
    main(number_of_images=num)

# created model 