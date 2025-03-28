import requests, yaml, sys, time
from pathlib import Path

# grab your absolute path of file without hardcoding it in script
script_location = Path(__file__).absolute().parent

yaml_path = f'{script_location}/context.yaml'

def load_payload_from_yaml(file_path):
    try:
        with open(file_path, 'r') as file:
            # grab contents of yaml file
            data = yaml.safe_load(file)
            return data
    except Exception as e:
        print(f"Error loading YAML file: {e}")
        return []

def get_urls(payload):
    url_lst = []
    try:
    #    convert the payload to a list of url's to use
       url_lst = [d['url'] for d in payload]
       return url_lst
    except Exception as e:
        print(f"Error loading URLs: {e}")
        return []  

def testing_response(data):
    response_hash = {}
    results = {}
    
    while True: 
        for url in data:
            try:
                response = requests.get(url, timeout=5)
                results[url] = {
                    'status_code': response.status_code,
                    'response_time': response.elapsed.total_seconds()
                }
            except requests.exceptions.RequestException as e:
                results[url] = {'error': str(e)}
        
        for url, result in results.items():
            try: 
                if url not in response_hash:
                    response_hash[url] = [{'num_of_success_req': 0, 'num_of_http_req':0 }]
                
                response_hash[url][0]['num_of_http_req'] += 1

                # if the status code within 2xx and response time is less than .5 the site is up 
                if 200 <= result['status_code'] <= 299 and result['response_time'] < .5:
                    
                    response_hash[url][0]['num_of_success_req'] += 1

                percent = 100 * (response_hash[url][0]['num_of_success_req'] / response_hash[url][0]['num_of_http_req'])    
                
                print(f"The res time is: {result['response_time']}")
                
                print(f"{url} has {percent}% availability percentage")
                print("-" * 50)
            except Exception as e:
                print(f"Error grabbing health points: {e}")
                return [] 
        # program sleeps for 15 seconds before starting again  
        time.sleep(15)

if __name__ == "__main__":
    
    payload = load_payload_from_yaml(yaml_path)
    
    if not payload:
        print("No valid URLs found in the YAML file.")
        sys.exit(1)

    urls = get_urls(payload)
    
    return_res = testing_response(urls)