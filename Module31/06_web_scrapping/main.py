import requests
import re
from typing import List

if __name__ == '__main__':
    html_text = requests.get('http://www.columbia.edu/~fdc/sample.html').text
    pattern = r'<h3.*>(.+)</h3>'
    result: List[str] = re.findall(pattern, html_text)
    print(result)
