import json

data = {
    "competence":{
        "worktime": 11,
        "salary": 11,
        "com_charac":5,
        "education": 4,
        "city": 3,
        "school": 9,
        "age": 42
    },
    "stability":{
        "worktime": 11,
        "salary": 11,
        "insurance_edu_time":1,
        "time_num": 25,
        "marry": True,
        "position": 210000,
        "exp_tendency":True,
        "age": 42
    },
    "honesty":{
        "business_black":"",
        "bank_black":"",
        "police_black": "",
        "court_black": "",
        "insurance_exp_time": 1,
        "eduBg": True,
        "posBg": True
    },
    "enterprise":{
        "enterpriseScore": 5,
        "proSki": 5,
        "worAtt": 5,
        "proQua": 5,
        "leaAbi": 5,
        "comAbi": 5,
        "appreciation": True
    },
    "buyPower":{
        "travellerScore": 2

    },
    "user":{
        "user_id": 115584867522,
        "social_security_time": 8
    }
}

data2 = {
    "competence":{
        "worktime": "",
        "salary": "",
        'com_charac':"",
        "education": "",
        "city": "",
        "school": "",
        "age": ""
    },
    "stability":{
        "worktime": "",
        "salary": "",
        "insurance_edu_time":"",
        "time_num": "",
        "marry": "",
        "position": "",
        "exp_tendency":"",
        "age": ""
    },
    "honesty":{
        "business_black": "",
        "bank_black": "",
        "police_black": "",
        "court_black": "",
        "insurance_exp_time": 1,
        "eduBg": True,
        "posBg": True
    },
    "enterprise":{
        "enterpriseScore": "",
        "proSki": "",
        "worAtt": "",
        "proQua": "",
        "leaAbi": "",
        "comAbi": "",
        "appreciation": ""
    },
    "buyPower":{
        "travellerScore": ""

    },
    "user":{
        "user_id": 115584867522,
        "social_security_time": ""
    }
}
data3= {
    "competence":  {
        "worktime":  1.9444000190259,
        "salary":  0,
        "com_charac":  0,
        "education":  1,
        "city":  0,
        "school":  1,
        "age":  21
    },
    "stability":  {
        "worktime":  1.9444000190259,
        "salary":  0,
        "insurance_edu_time":  0.85716244104012,
        "time_num":  4.6665600456621,
        "marry":  False,
        "position":  200000,
        "exp_tendency":"",
        "age":  21
    },
    "honesty":  {
        "business_black":  "",
        "bank_black":  "",
        "police_black":  "",
        "court_black":  "",
        "insurance_exp_time":  0,
        "eduBg":  True,
        "posBg":  False
    },
    "enterprise":  {
        "proSki":  0,
        "worAtt":  0,
        "proQua":  0,
        "leaAbi":  0,
        "comAbi":  0,
        "appreciation":  False
    },
    "buyPower":  {
        "travellerScore":  0
    },
    "user":  {
        "user_id":  90,
        "social_security_time":  1.6666666666667
    }
}


if __name__ == '__main__':
    d = json.dumps(data2)  # 转化json
    # print(d)
    from score_model.working_score.score_4 import WorkspaceCreditScore

    wc = WorkspaceCreditScore()
    wc.load_data(d)
    print('用户',wc.user_id)
    print('工作能力得分', wc.competence)
    print('稳定性得分',wc.stability[0])
    print('稳定性：',wc.stability[1])
    print('个人诚信得分', wc.honesty)
    print('社会关系得分', wc.enterprise)
    print('经济能力得分',wc.buyPower)
    s = wc.buyPower + wc.competence + wc.enterprise +wc.honesty+wc.stability[0]
    print('总得分', s)
    print('诚信系数',wc.coe)

# 基本分
# 经济能力得分 48
# 企业对个人评价得分 85
# 工作能力得分 90.99216
# 个人诚信得分 180
# 稳定性得分 80.10009000000001
# 总得分 484.09225000000004
# 诚信系数 0.6885
# 最高分
# 工作能力得分 239.61
# 个人诚信得分 229.4
# 稳定性得分 165.18
# 总得分 859.19
# 诚信系数 1
# 最低分
# 经济能力得分 48
# 社会关系得分 85
# 工作能力得分 38.932040454749995
# 个人诚信得分 139
# 稳定性得分 29.05822959525
# 总得分 339.99027005
# 诚信系数 0.2536950375

# 稳定性 165，120，78 ，29  （0，50），（50，80），（80，120），（120，200）