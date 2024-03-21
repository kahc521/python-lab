import requests

def urlCheck(url):
    isUp=True
    try:
        resp = requests.get(url)
    except:
        print("please double check your url")
    else:
        status = resp.status_code
        if status == 200:
            isUp=True
        else:
            isUp=False
    return isUp

a=urlCheck('http://google.com')
print(a)
