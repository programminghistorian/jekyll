import requests
import time
import pandas as pd
from random import randint
from retrying import retry

def retry_if_connection_error(exception):
    return isinstance(exception, JSONDecodeError)

# if exception retry with a 600-seconds plus wait  
@retry(retry_on_exception=retry_if_connection_error, wait_random_min=600000, wait_random_max=610000)
def safe_request(url):
    return requests.get(url)

if __name__ == '__main__':
    langs = ["Albanian",
    "Amharic",
    "Arabic",
    "Armenian",
    "Asue Awyu",
    "Austronesian (Other)",
    "Basque",
    "Belarussian",
    "Bengali",
    "Bosnian",
    "Bulgarian",
    "Burmese",
    "Cebuano",
    "Central Huasteca Nahuatl",
    "Chechen",
    "Cherokee",
    "Chinese",
    "Choctaw",
    "Cree",
    "Creek",
    "Creoles and Pidgins",
    "Creoles and Pidgins, French-based (Other)",
    "Croatian",
    "Croatian",
    "Czech",
    "Dakota",
    "Danish",
    "Dutch",
    "English",
    "Esperanto",
    "Estonian",
    "Finnish",
    "French",
    "German",
    "Germanic",
    "Greek",
    "Gujarati",
    "Hawaiian",
    "Hebrew",
    "Hindi",
    "Hmong",
    "Hungarian",
    "Icelandic",
    "Iloko",
    "Indonesian",
    "Inupiaq",
    "Iranian",
    "Irish",
    "Italian",
    "Japanese",
    "Khmer",
    "Korean",
    "Kurdish",
    "Ladino",
    "Latvian",
    "Lithuanian",
    "Macedonian",
    "Malayalam",
    "Marathi",
    "Mohawk",
    "Multiple",
    "Navajo",
    "Negidal",
    "No Linguistic Content",
    "Northwest Alaska Inupiatun",
    "Norwegian",
    "Norwegian",
    "Panjabi",
    "Persian",
    "Polish",
    "Portuguese",
    "Romanian",
    "Russian",
    "Samaritan Aramaic",
    "Samoan",
    "Serbian",
    "Serbian",
    "Slovak",
    "Slovenian",
    "Sorbian",
    "Spanish",
    "Swedish",
    "Syriac",
    "Tagalog",
    "Tajik",
    "Tamil",
    "Thai",
    "Turkish",
    "Ukrainian",
    "Urdu",
    "Uzbek",
    "Vietnamese",
    "Welsh",
    "Yiddish",
    "Yupik"]

    years = list(range(1690, 2023+1, 10))
    
    data_dict={}

    for y in years[years.index(1690):]:
        print(y, y+10)
        for lang in langs[langs.index("Albanian"):]:
            time.sleep(randint(10,15))
            url = r"https://chroniclingamerica.loc.gov/search/titles/results/?year1={0}&year2={1}&language={2}&format=json".format(y, y+10, lang)
            print(y, lang)
            rsp = safe_request(url)
            if rsp.status_code == 429:
                
                wait_time = int(rsp.headers["Retry-After"])
                time.sleep(wait_time)
                print("sleeping for:", wait_time)
                n_titles = safe_request(url).json()['totalItems']
                title_dict = {lang: n_titles}
                if y not in data_dict.keys():
                    data_dict.update({y: title_dict})
                else:
                    data_dict[y].update(title_dict) 
            else:
                n_titles = safe_request(url).json()['totalItems']
                title_dict = {lang: n_titles}

                if y not in data_dict.keys():
                    data_dict.update({y: title_dict})
                else:
                    data_dict[y].update(title_dict)

    lang_asrow = pd.DataFrame.from_dict(data_dict, orient='index').T
    lang_asrow.to_csv("data/data_lang_asrow_test.csv", encoding="utf-8")