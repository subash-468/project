import requests
result=requests.get('https://334de7e5-ad66-42ad-af50-748483750c28.mock.pstmn.io//mock_data')
if(result.status_code==200):
    result=result.json()
    '''result=dict((result[i]["name"],result[i]["password"]) for i in range(0,len(result)))
    print("logesh" in result.keys())'''
    data=result
    print(data)