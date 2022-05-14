import requests
import json
from typing import Dict, List

if __name__ == '__main__':
    deaths_request = requests.get('https://www.breakingbadapi.com/api/deaths')
    data = json.loads(deaths_request.text)
    with open('breaking_bad_file.json', 'w') as file:
        json.dump(data, file, indent=4)

    with open('breaking_bad_file.json', 'r') as file:
        data_file_episod = json.load(file)
        episode: Dict[str, int] = max(data_file_episod, key=lambda x: x.get('number_of_deaths'))

    episode_request = requests.get('https://www.breakingbadapi.com/api/episodes')
    id_episod_finding = json.loads(episode_request.text)

    with open('episodes_file.json', 'w') as file:
        json.dump(id_episod_finding, file, indent=4)

    with open('episodes_file.json', 'r') as file:
        data_file_id_episode = json.load(file)
        id_of_episode: List[dict] = list(filter(
            lambda x: int(x.get('episode')) == episode.get('episode') and int(x.get('season')) == episode.get('season'),
            data_file_id_episode))
        id_of_episode[0].update(episode)
        result = {}

        for item in id_of_episode:
            result['episode_id'] = item.get('episode_id')
            result['season'] = item.get('season')
            result['episode'] = item.get('episode')
            result['number_of_deaths'] = item.get('number_of_deaths')
            result['death'] = item.get('death')

    with open('result_file.json', 'w') as file:
        json.dump(result, file, indent=4)

    with open('result_file.json', 'r') as file:
        data = json.load(file)
        print(data)
