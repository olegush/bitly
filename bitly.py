from dotenv import load_dotenv
import argparse
import requests
import os


def get_args_parser():
    parser = argparse.ArgumentParser(
        description='Utility for short urls to bitlinks and get click stats'
    )
    parser.add_argument(
        'url',
        help='Your link for shortening or bitlink for getting stats'
    )
    return parser.parse_args()


def get_bitlink_info(token, bitlink):
    bitly_url = 'https://api-ssl.bitly.com/v4/bitlinks/' + bitlink
    headers = {'Authorization': 'Bearer ' + token}
    request = requests.get(bitly_url, headers=headers)
    return request.ok


def get_bitlink(token, url):
    bitly_url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {'Authorization': 'Bearer ' + token}
    json = {'long_url': url}
    request = requests.post(bitly_url, headers=headers, json=json)
    if not request.ok:
        return 
    return request.json()['id']
        
    
def get_bitlink_stats(token, bitlink):
    bitly_url = 'https://api-ssl.bitly.com/v4/bitlinks/' + bitlink + '/clicks/summary'
    headers = {'Authorization': 'Bearer ' + token}
    params = {'unit': 'day', 'units': -1}
    request = requests.get(bitly_url, headers=headers, params=params)
    if not request.ok:
        return 
    return request.json()['total_clicks']


if __name__ == '__main__':
    load_dotenv()
    user_args = get_args_parser()
    user_link = user_args.url
    token = os.getenv('TOKEN')
    if get_bitlink_info(token, user_link):
        bitlink_stats = get_bitlink_stats(token, user_link)
        if bitlink_stats:
            print('Total bitlink clicks: {}'.format(bitlink_stats))
        else:
            print('Error stats count for the bitlink')
    else:
        bitlink = get_bitlink(token, user_link)
        if bitlink:
            print('Your bitlink: {}'.format(bitlink))
        else:
            print('Incorrect url or access denied for the bitlink')
