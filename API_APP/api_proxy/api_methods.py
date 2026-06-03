import requests

BASE_URL = "http://newsapi.org/v2"

def _make_request(endpoint: str, api_key: str, params: dict[str, str]) -> dict[str, str]:
    url = f"{BASE_URL}/{endpoint}"
    default_params = {'apiKey': api_key}


    if params:
        default_params.update(params)
    try:
        response = requests.get(url, params=default_params, timeout=10)
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f'Ошибка в запросе к NewsAPI({endpoint}):{e}')

    except ValueError as e:
        raise Exception(f'Ошибка типа JSON:{e}')

def get_top_headlines(api_key: str, q: str,country: str = None,
                      category: str = None, sources: str = None, page_size: int = None) -> dict:

    allowed_params = {'q':q, 'country':country,
                      'category':category, 'sources':sources, 'pageSize':page_size}
    params= {key:value for key, value in allowed_params.items() if value is not None}

    return _make_request('top-headlines', api_key, params)



def get_everything(api_key: str, q: str, searchln: str = None,
                   sources: str = None, domains: str = None, excludedomains: str = None, froom: str=None,
                   to: str=None, language:str=None, sortby: str=None,pagesize:int=None,
                   page: int=None) -> dict:

    allowed_params = {'q':q, 'searchln':searchln, 'sources':sources, 'domains':domains, 'excludedomains':excludedomains,
                    'froom': froom, 'to': to, 'language':language, 'sortby':sortby, 'pagesize':pagesize, 'page':page}

    params= {key: value for key, value in allowed_params.items() if value is not None}
    return _make_request('everything', api_key, params)


def get_sources(api_key: str, category: str=None, language: str=None, country: str=None) -> dict:

    allowed_params = {'category':category, 'language':language, 'country':country}

    params= {key:value for key, value in allowed_params.items() if value is not None}

    return _make_request('sources', api_key, params)