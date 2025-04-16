import os
import json
import requests
import concurrent.futures
import logging
from typing import Dict, List

SERPER_API_KEY = "API_KEY"


def search(query_list: List[str], n_max_doc: int = 20, search_engine: str = 'serper', freshness: str = '') -> List[Dict[str, str]]:
    doc_lists = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(
            search_single, query, search_engine, freshness) for query in query_list]
        for future in concurrent.futures.as_completed(futures):
            try:
                doc_lists.append(future.result())
            except:
                pass
    doc_list = _rearrange_and_dedup([d for d in doc_lists if d])
    return doc_list[:n_max_doc]


def search_single(query: str, search_engine: str, freshness: str = '') -> List[Dict[str, str]]:
    try:
        if search_engine == 'serper':
            search_results = serper_request(query, freshness=freshness)
            return serper_format_results(search_results)
        else:
            raise ValueError(f'Unsupported Search Engine: {search_engine}')
    except Exception as e:
        logging.error(f'Search failed: {str(e)}')
        raise ValueError(f'Search failed: {str(e)}')


def serper_request(query: str, count: int = 50, freshness: str = '') -> List[Dict[str, str]]:
    endpoint = "https://google.serper.dev/search"
    headers = {
        'X-API-KEY': SERPER_API_KEY,
        'Content-Type': 'application/json'
    }
    payload = {
        "q": query
    }
    try:
        response = requests.post(endpoint, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        organic_results = data.get('organic', [])
        return organic_results

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

    return []


def serper_format_results(search_results: List[Dict[str, str]]):
    formatted_results = [
        {
            'id': str(rank + 1),
            'title': str(res.get('title', '')),
            'snippet': str(res.get('snippet', '')),
            'url': str(res.get('link', '')),
            'timestamp': ''  # Serper API doesn't provide timestamp
        }
        for rank, res in enumerate(search_results)
    ]
    return formatted_results


def _rearrange_and_dedup(doc_lists: List[List[Dict[str, str]]]) -> List[Dict[str, str]]:
    doc_list = []
    snippet_set = set()
    for i in range(50):
        for ds in doc_lists:
            if i < len(ds):
                if 'snippet' in ds[i]:
                    signature = ds[i]['snippet'].replace(' ', '')[:200]
                else:
                    signature = ds[i]['content'].replace(' ', '')[:200]
                if signature not in snippet_set:
                    doc_list.append(ds[i])
                    snippet_set.add(signature)
    return doc_list


if __name__ == '__main__':
    queries = ["egypt crisis timeline"]
    from pprint import pprint
    pprint(search(queries, search_engine='serper', n_max_doc=30))
