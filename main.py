from collect_faculty_urls import extract_faculty_urls as get_urls
from scrape_profile import scrape_and_search as check_url
import pandas as pd

url_list = get_urls('https://mcb-seattle.edu/directory/faculty/?_sft_aoi=computational-biology')

names = []
interests_1 = []
interests_2 = []
lab_url = []
for url in url_list:
    test = check_url(url)
    if test:
        names.append(test['header'])
        interests_1.append(test['paragraph_1'])
        interests_2.append(test['paragraph_2'])
        if 'link' in test:
            lab_url.append(test['link'])

all_interests = [interests_1[i] + ', ' + interests_2[i] for i in range(len(interests_1))]

data = {'Name': names, 'Interests': all_interests, 'URL': lab_url}
data = pd.DataFrame(data)

data.to_csv('Faculty_info.csv', index=False)


print(data)