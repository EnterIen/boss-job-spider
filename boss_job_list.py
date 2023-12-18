import requests

url = 'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=&city=101010100&experience=106&payType=&partTime=&degree=&industry=&scale=302&stage=&position=100103&jobType=1901&salary=406&multiBusinessDistrict=&multiSubway=&page=1&pageSize=30'

cookie_string = 'lastCity=101010100; __zp_seo_uuid__=b132c142-bae4-473f-bf5e-c341fedbc373; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1702651381; wd_guid=bc00bf9c-1d5c-4810-b387-8fd52b91d5bf; historyState=state; _bl_uid=Inl33q986O8q3Rob2bkUtLqabpgO; wbg=0; gdxidpyhxdE=jnoT%2B3asb6OxKZSDYSWWJecI8pbkmpbsYCLmBPD0ggadOHqBkp%5CclSU3ofu%2BHNwcAAupqiSfEevSE5%2FqO9%2Bc2fAaMrqlWv9zj9m34ueo%2FLdMXfsAqbz4U7qe07X8HUxHAM8%5CP8OjWHN%5CYUolbS2XhOdhSrjmBRdaTkbyZ1E0kWXPCPdj%3A1702653154882; collection_pop_window=1; __l=r=https%3A%2F%2Fwww.google.com%2F&l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3DAirbnb%26city%3D101010100&s=3&g=&friend_source=0&s=3&friend_source=0; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1702876752; __zp_stoken__=35c0fPzjDmMK6XcK8RSsSDAwXCkEoODgsC0A%2FLEQ9RD84Oj9GPzhCHTgvwpLCum3DssK5ZMONDT8qODpCPz9GOj1CGjhGwrs%2FPjLCisK9b8Oywr5mw4oMwovCv1jCnsK4DFcJFsK%2FDMKfwr0oLcO9wrk9OkA4w7XCuMOiw4PCksK6w6XDgcKPwr3Dp8OGOjg4JDc%2BX1wXZz44S05YCEpnT2JiVgpWVFMqOEQ7PcKIw6HDvzE%2FFRUSEBcRERYUExERFg0KFBQTERYODgkLDDc%2FwqXCvcKlw4LFuMKKxIDEnMKZWMKPVsO9wqPDg03CucK5wqxSw4NxwpVTwqhqwptwwolmwqPCgsK5X8KzdsK0Wnd1wrdbw4V5wrtVwr%2FCuE1LSVEQDGcWFj4QwqPCg8OI; boss_login_mode=app; wt2=DxYP15ANs4ubiI2IlEragxGTIZCcxbX8il3jckla8NZ5bWcD5uZ1M-r8ZvuWM4DcvDHdmo_0oRIxA59B5Fjk4FA~~; __c=1702651381; __a=59132821.1702651381..1702651381.62.1.62.62'
cookies = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookie_string.split('; ')}


response = requests.get(url, cookies=cookies)

print(response)
print(response.text)
print(response.json)
