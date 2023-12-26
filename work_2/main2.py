import urllib3


r = urllib3.request('POST', 'https://pub.fsa.gov.ru/api/v1/rds/common/declarations/get').json()
print(r)