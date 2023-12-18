data_container = {
    "code": 0,
    "zpData": {
        "number": 100,
        "jobList": [
            {
                "lastModifyTime": 1700566111000,
                "encryptBrandId": "ba442f6bc18ccacc1nV73dW8GVY~",
                "brandName": "某电子商务公司",
                "brandLogo": "https://img.bosszhipin.com/beijin/app/mobile/n-af8dd288f86448d9eaaf3a4b0fd60b27.png",
                "brandStageName": "",
                "brandIndustry": "电子商务",
                "brandScaleName": "20-99人",
            }
        ]
    }
}

zpData = data_container.get("zpData", {})
data = zpData.get("jobList", [])
print(data)
