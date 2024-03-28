import requests
def check(s):
    name = s
    print("entered in check")
    print(s)
    print("helelleoeo")
    api_url = 'https://api.api-ninjas.com/v1/logo?ticker={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': 'RC8YRY7+NipYXfOhlsAAWQ==SwsGkmDsCIdRcg97'})
    if response.status_code == requests.codes.ok:
        print(response.text)
        print("code is okaay")
        result=response.text
    else:
        print("Error:", response.status_code, response.text)
        result="wrong input"
    return result
