import json


class WorkspaceCreditScore():
    def __init__(self):
        self.__competence = {
            'worktime': {(0, 1): [1.5,3,1.2], (1, 2): [6, 7.5,3],(2, 3): [10.5,13.5,4.5], (3, 4): [13.5,21,7.5], (4, 6): [19.5,22.5,12], (6, 8): [22.5,24,19.5], (8, 10): [24,21,22.5], (10, 100): [25.5,12,27]},
            'salary': {0: [1.5,1.5,1.5], 1: [3,3.3,3.6], 2: [4.5,5.4,5.7], 3: [6,7.8,8.4], 4: [7.5,11.1,12], 5: [10.5,15.6,16.8], 6: [12,18,19.2], 7: [13.5,20.1,21.6], 8: [15,19.5,24], 9: [16.5,21.3,23.1], 10: [18,23.4,25.2], 11: [21,27.3,29.4]},
            'com_charac':{0:[2.1,2.1],1:[6.3,4.2],2:[9.45,5.25],3:[14.7,6.3],4:[17.85,7.35],5:[19.95,8.4]},
            'education': {0: [1.82,1.3], 1: [3.9,4.42], 2: [9.1,22.1], 3: [6.5,16.9], 4: [4.68,10.4]},
            'city':  {0: 1, 1: 3, 2: 7, 3: 9},
            'school': {0: 0.24, 1: 0.6, 2: 0.84, 3: 0.96, 4: 1.08, 5: 1.32, 6: 1.44, 7: 1.56, 8: 1.8, 9: 2.16},
            'age': {(0, 22): [0.3,0.3,0.3], (22, 26):[0.9,1.5,0.9] , (26, 28): [1.8,3,1.8], (28, 30): [2.7,5.1,2.7], (30, 35): [3.6,2.7,3.9], (35, 40): [4.5,1.2,4.5], (40, 100): [1.5,0.6,5.1]},
        }
        self.__stability = {
            'worktime': {(0, 1): [0.9,1.8,0.72], (1, 2): [3.6, 4.5,1.8],(2, 3): [6.3,8.1,2.7], (3, 4): [8.1,12.6,4.5], (4, 6): [11.7,13.5,7.2], (6, 8): [13.5,14.4,11.7], (8, 10): [14.4,12.6,13.5], (10, 100): [15.3,7.2,16.2]},
            'salary': {0: [0.9,0.9,0.9], 1: [1.8,1.98,2.16], 2: [2.7,3.24,3.42], 3: [3.6,4.68,5.04], 4: [4.5,6.66,7.2], 5: [6.3,9.36,10.08], 6: [7.2,10.8,11.52], 7: [8.1,12.06,12.96], 8: [9,11.7,14.4], 9: [9.9,12.78,13.86],10: [10.8,14.04,15.12], 11: [12.6,16.38,17.64]},
            "insurance_edu_time": {(0, 0.4): 4, (0.4, 0.8): 4.8, (0.8, 1): 7.2},
            "time_num": {(0, 6): [1.96, 1.12], (6, 12): [2.52, 1.4], (12, 18): [2.8, 1.96] , (18, 24): [3.22, 4.2] , (24, 2000): [3.5, 5.32]},
            "marry": {True: 6.5, False: 3.5},
            "position": {
                100000: 7,      #技术
                110000: 6.5,    #产品
                120000: 7.1,    #设计
                130000: 6,      #运营
                140000: 5,      #市场
                160000: 3,      #销售
                150000: 7.2,    #人事 / 财务 / 行政
                310000: 6.5,    #高级管理
                170000: 4.5,    #传媒
                180000: 3.6,    #金融
                230000: 3.8,    #汽车
                190000: 7.5,    #教育培训
                210000: 7.7,    #医疗健康
                250000: 6.2,    #采购 / 贸易
                240000: 6.3,    #供应链 / 物流
                220000: 7.3,    #房地产 / 建筑
                260000: 6.4,    #咨询 / 翻译 / 法律
                270000: 3.9,    #实习生 / 管培生
                280000: 3.2,    #旅游
                290000: 3.3,    #酒店 / 餐饮 / 零售
                300000: 4.1,    #生产制造
                200000: 2       #其他
            },
            'age': {(0, 22): 0.3, (22, 26): 0.9, (26, 28): 1.5, (28, 30): 2.4, (30, 35): 3.6, (35, 40): 4.5, (40, 100): 4.8},
            'exp_tendency':{True:8,False:0}
        }
        self.__honesty = {
            "business_black": {0:0,1:8,2:14,3:20},
            "bank_black": {True: 0, False: 14},
            "police_black": {0:0,1:4.4,2:7.7,3:11},
            "court_black": {0:0,1:2,2:3.5,3:5},
            "insurance_exp_time": {(0, 0): 0, (0, 0.2): 3.6, (0.2, 0.4): 6.75, (0.4, 0.6): 9, (0.6, 0.8): 11.25, (0.8, 1): 14.4},
            "eduBg": {True: 20, False: 0},
            "posBg": {True: 15, False: 0},

        }
        self.__enterprise ={

            "proSki": {0: 0, 1: [1.5,3], 2: [4.5,6], 3:[6,7.5], 4: [9,10.5], 5: [12,15]},
            "worAtt": {0: 0, 1: 3, 2: 6, 3: 9, 4: 12, 5: 15},
            "proQua": {0: 0, 1: 3, 2: 6, 3: 9, 4: 12, 5: 15},
            "leaAbi": {0: 0, 1: 3, 2: 6, 3: 9, 4: 12, 5: 15},
            "comAbi": {0: 0, 1: [1.5,3], 2: [4.5,6], 3:[6,7.5], 4: [9,10.5], 5: [12,15]},
            "appreciation": {True: 10, False: 0}
        }
        self.__buyPower = {
            "travellerScore": {0: 8, 1: 14, 2: 18},
        }
        # 工作能力
        self.worktime = None
        self.salary = None
        self.com_charac = None
        self.education = None
        self.city = None
        self.school = None
        self.age = None
        # 稳定性
        self.insurance_edu_time = None
        self.time_num = None
        self.marry = None
        self.position = None
        self.exp_tendency = None
        # 个人诚信
        self.business_black = None
        self.bank_black = None
        self.police_black = None
        self.court_black = None
        self.insurance_exp_time = None
        self.eduBg = None
        self.posBg = None
        # 企业对个人评分
        self.proSki = None
        self.worAtt = None
        self.proQua = None
        self.leaAbi = None
        self.comAbi = None
        self.appreciation = None
        #经济能力
        self.travellerScore = None
        #其他信息
        self.user_id = None
        self.social_security_time = None
        #诚信系数
        self.coe = 1
        # 得分情况
        self.honesty = 0
        self.competence = 0
        self.stability = 0
        self.enterprise = 0
        self.buyPower = 0

    def load_data(self, data):
        """

        :param data: json字符串
        :return:
        """
        data = json.loads(data,encoding='utf-8')  # 将json转化为字典
        # 工作能力
        self.worktime = data['competence']["worktime"]
        self.salary = data['competence']["salary"]
        self.com_charac = data['competence']['com_charac']
        self.education = data['competence']["education"]
        self.city = data['competence']["city"]
        self.school = data['competence']["school"]
        self.age = data['competence']["age"]
        # 稳定性
        self.insurance_edu_time = data['stability']['insurance_edu_time']
        self.time_num = data['stability']['time_num']
        self.marry = data['stability']['marry']
        self.position = data['stability']['position']
        self.exp_tendency = data['stability']['exp_tendency']
        # 个人诚信
        self.business_black = data['honesty']['business_black']
        self.bank_black = data['honesty']['bank_black']
        self.police_black = data['honesty']['police_black']
        self.court_black = data['honesty']['court_black']
        self.insurance_exp_time = data['honesty']['insurance_exp_time']
        self.eduBg = data['honesty']['eduBg']
        self.posBg = data['honesty']['posBg']
        # 企业对个人评分
        self.proSki = data['enterprise']['proSki']
        self.worAtt = data['enterprise']['worAtt']
        self.proQua = data['enterprise']['proQua']
        self.leaAbi = data['enterprise']['leaAbi']
        self.comAbi = data['enterprise']['comAbi']
        self.appreciation = data['enterprise']['appreciation']
        # 经济能力
        self.travellerScore = data['buyPower']['travellerScore']
        # 其他信息
        self.user_id = data['user']['user_id']
        self.social_security_time = data['user']['social_security_time']
        # self.honesty()
        #得分情况
        self.honesty = self.__honesty_score()
        self.competence = self.__competence_score()
        self.stability = self.__stability_score()
        self.enterprise = self.__enterprise_score()
        self.buyPower = self.__buyPower_score()


    def __competence_score(self):  # 个人能力
        """

        :return: 个人能力得分
        """
        score_worktime = 30
        score_salary = 30
        score_com_charac = 21
        score_education = 26
        score_city = 20
        score_school = 12
        score_age = 6
        # 判断工龄
        for i in self.__competence['worktime']:
            Youth_list = [100000 ,120000,140000 ,160000,170000,280000]
            Old_list = [190000,210000,220000,150000,260000]
            if self.position in Youth_list:
                if i[0] <=self.worktime <= i[1] :
                    score_worktime += self.__competence['worktime'][i][1]
                    break

                elif not self.worktime:
                    score_worktime += self.__competence['worktime'][i][1]
                    break
            elif self.position in Old_list :
                if i[0]<= self.worktime <=i[1]:
                    score_worktime += self.__competence['worktime'][i][2]
                    break
                elif not self.worktime :
                    score_worktime += self.__competence['worktime'][i][2]
                    break
            else:
                if not self.worktime:
                    score_worktime += self.__competence['worktime'][i][0]
                    break
                else:
                    if i[0]<= self.worktime <=i[1]:
                        score_worktime += self.__competence['worktime'][i][0]
                        break
        # print('工龄测试：',score_worktime)


        # 判断薪资收入
        for i in self.__competence['salary']:
            if self.city == 2 :
                if not self.salary:
                    score_salary += self.__competence['salary'][0][1]
                    break
                elif self.salary == i:
                    score_salary += self.__competence['salary'][i][1]
                    break
            elif self.city == 1 or self.city == 0:
                if not self.salary:
                    score_salary += self.__competence['salary'][0][2]
                    break
                elif self.salary == i:
                    score_salary += self.__competence['salary'][i][2]
                    break
            else:
                if not self.salary:
                    score_salary += self.__competence['salary'][0][0]
                    break
                elif self.salary == i:
                    score_salary += self.__competence['salary'][i][0]
                    break
        # print('薪资测试：',score_salary)

        #判断公司性质
        for i in self.__competence['com_charac']:
            high_charac_list = [100000,110000,120000,130000,310000,170000,180000,190000,210000,260000]
            if self.position in high_charac_list:
                if not self.com_charac:
                    score_com_charac += self.__competence['com_charac'][0][0]
                    # print('hello')
                    break
                elif self.com_charac == i:
                    score_com_charac += self.__competence['com_charac'][i][0]
                    # print('hello')
                    break
            else:
                if not self.com_charac:
                    score_com_charac += self.__competence['com_charac'][0][1]
                    break
                elif self.com_charac == i:
                    score_com_charac += self.__competence['com_charac'][i][1]
                    break

                    # 判断学历
        for i in self.__competence['education']:
            ask_edu_list = [100000 ,120000,310000,180000,190000 ,210000 ,260000 ]
            if self.position in ask_edu_list:
                if not self.education:
                    score_education += self.__competence['education'][0][1]
                    break
                elif self.education == i:
                    score_education += self.__competence['education'][i][1]
                    break
            else:
                if not self.education:
                    score_education += self.__competence['education'][0][0]
                    break
                elif self.education == i:
                    score_education += self.__competence['education'][i][0]
                    break
        # 判断工作城市
        for i in self.__competence['city']:
            if not self.city:
                score_city += self.__competence['city'][0]
                break
            elif self.city == i:
                score_city += self.__competence['city'][i]
                break
        # 判断最高学历毕业学校
        for i in self.__competence['school']:
            if not self.school:
                score_school += self.__competence['school'][i]
                break
            elif self.school == i:
                score_school += self.__competence['school'][i]
                break
        # 判断年龄

        for i in self.__competence['age']:
            Youth_list = [100000 ,120000,140000 ,160000,170000,280000]
            Old_list = [190000,210000,220000,150000,260000]
            if self.position in Youth_list:
                if self.age == "":
                    score_age += self.__competence['age'][(0,22)][1]
                    break
                elif self.age > i[0] and self.age <= i[1]:
                    score_age += self.__competence['age'][i][1]
                    break
            elif self.position in Old_list:
                if self.age == "":
                    score_age += self.__competence['age'][(0,22)][2]
                    # print('hello')
                    break
                elif self.age > i[0] and self.age <= i[1]:
                    score_age += self.__competence['age'][i][2]
                    # print('hello')
                    break
            else:
                if self.age == "":
                    score_age += self.__competence['age'][(0,22)][0]
                    break
                elif self.age > i[0] and self.age <= i[1]:
                    score_age += self.__competence['age'][i][0]
                    break
        # print(score_age)
        competence_score = score_worktime + score_salary + score_education + score_city + score_school + score_age + score_com_charac

        # print("个人能力：",score_worktime, score_salary, score_education, score_city, score_school, score_age)
        return competence_score * self.coe

    def __stability_score(self):
        """
        :return: 稳定性得分,非常稳定，基本稳定、暂时稳定和不稳定
        """
        worktime_score = 18
        salary_score = 18
        insurance_edu_time_score = 16
        time_num_score = 14
        marry_score = 10
        position_score = 10
        age_score = 6
        exp_tendency_score = 8
        #工作时长
        for i in self.__stability['worktime']:
            Youth_list = [100000 ,120000,140000 ,160000,170000,280000]
            Old_list = [190000,210000,220000,150000,260000]
            if self.position in Youth_list:
                if i[0] <= self.worktime <=i[1]:
                    worktime_score += self.__stability['worktime'][i][1]
                    break

                elif not self.worktime:
                    worktime_score += self.__stability['worktime'][i][1]
                    break
            elif self.position in Old_list :
                if i[0] <= self.worktime <=i[1]:
                    worktime_score += self.__stability['worktime'][i][2]
                    break
                elif not self.worktime :
                    worktime_score += self.__stability['worktime'][0][2]
                    break
            else:
                if not self.worktime:
                    worktime_score += self.__stability['worktime'][i][0]
                    break
                else:
                    if i[0] <= self.worktime <=i[1]:
                        worktime_score += self.__stability['worktime'][i][0]
                        break

        #薪资收入
        for i in self.__stability['salary']:
            if self.city == 2 :
                if not self.salary:
                    salary_score += self.__stability['salary'][0][1]
                    break
                elif self.salary == i:
                    salary_score += self.__stability['salary'][i][1]
                    break
            elif self.city == 1 or self.city == 0:
                if not self.salary:
                    salary_score += self.__stability['salary'][0][2]
                    break
                elif self.salary == i:
                    salary_score += self.__stability['salary'][i][2]
                    break
            else:
                if not self.salary:
                    salary_score += self.__stability['salary'][0][0]
                    break
                elif self.salary == i:
                    salary_score += self.__stability['salary'][i][0]
                    break
        #总缴纳社保的时长/学历工作时长
        for i in self.__stability['insurance_edu_time']:
            if not self.insurance_edu_time:
                insurance_edu_time_score += self.__stability['insurance_edu_time'][(0,0.4)]
                # print('hello1')
                break
            elif self.insurance_edu_time >i[0] and self.insurance_edu_time <= i[1] :
                insurance_edu_time_score += self.__stability['insurance_edu_time'][i]
                # print('hello2')
                break
        # print("比例分：",insurance_edu_time_score)
        #学历的工作时长/缴纳社保的公司数量
        if not self.social_security_time or self.social_security_time < 5:
            for i in self.__stability['time_num']:
                if not self.time_num:
                    time_num_score += self.__stability['time_num'][i][0]
                    break
                elif self.time_num > i[0] and self.time_num <= i[1]:
                    time_num_score += self.__stability['time_num'][i][0]
                    break
        elif self.social_security_time >= 5 :
            for i in self.__stability['time_num']:
                if not self.time_num:
                    time_num_score += self.__stability['time_num'][i][1]
                    break
                elif self.time_num > i[0] and self.time_num <= i[1]:
                    time_num_score += self.__stability['time_num'][i][1]
                    break
        #婚姻
        if not self.marry:
            marry_score += self.__stability['marry'][False]
        else:
            marry_score += self.__stability['marry'][self.marry]
        #职位
        if not self.position:
            position_score += self.__stability['position'][200000]
        else:
            position_score += self.__stability['position'][self.position]
        # 最近3家公司工作时长是否递增
        if not self.exp_tendency:
            exp_tendency_score += self.__stability['exp_tendency'][False]
        else:
            exp_tendency_score += self.__stability['exp_tendency'][self.exp_tendency]
        # print('趋势:',exp_tendency_score)


        #年龄
        for i in self.__stability['age']:
            if not self.age:
                age_score += self.__stability['age'][(0,22)]
                break
            elif self.age > i[0] and self.age <= i[1]:
                age_score += self.__stability['age'][i]
                break
        stability_score = (worktime_score + salary_score + insurance_edu_time_score + time_num_score + marry_score + position_score + age_score + exp_tendency_score) * self.coe
        if 0 < stability_score <= 50:
            stability_label = "不稳定"
        elif 50 < stability_score <= 80:
            stability_label = "暂时稳定"
        elif 80 < stability_score <= 120 :
            stability_label = "基本稳定"
        else:
            stability_label = "非常稳定"
        # print("稳定性：",stability_label)

        # print("个人稳定性：",worktime_score , salary_score ,insurance_edu_time_score ,time_num_score , marry_score , position_score ,age_score)
        return stability_score,stability_label

    def __honesty_score(self):#
        """
        :return: 个人诚信得分
        """
        business_black_score = 20
        bank_black_score = 14
        police_black_score = 11
        court_black_score = 5
        insurance_exp_time_score = 45
        eduBg_score = 15
        posBg_score = 20
        appreciation_score = 10
        # 企业黑名单
        for i in self.__honesty['business_black']:
            if self.business_black == "" :
                business_black_score += self.__honesty['business_black'][3]
                # print('企业:',business_black_score)
                break
            elif not self.business_black:
                self.coe *= 0.6
                business_black_score += self.__honesty['business_black'][0]
                break
        if self.business_black:

            if self.business_black == 1:
                self.coe *= 0.85
                business_black_score += self.__honesty['business_black'][1]

            elif self.business_black == 2:
                self.coe *= 0.95
                business_black_score += self.__honesty['business_black'][2]

            elif self.business_black == 3:
                business_black_score += self.__honesty['business_black'][3]
            else:
                print('企业黑名单数字传输错误，请重新输入')
                business_black_score += self.__honesty['business_black'][4]

        # 金融黑名单
        if self.bank_black == True:
            bank_black_score += self.__honesty['bank_black'][True]
            self.coe *= 0.85
        elif self.bank_black == False:
            bank_black_score += self.__honesty['bank_black'][False]
        elif not self.bank_black:
            bank_black_score += self.__honesty['bank_black'][False]

            # print('jinrong',bank_black_score)

        # 公安黑名单
        for i in self.__honesty['police_black']:
            if self.police_black == "" :
                police_black_score += self.__honesty['police_black'][3]
                # print('公安：',police_black_score)
                break
            elif not self.police_black:
                self.coe *= 0.85
                police_black_score += self.__honesty['police_black'][0]
                # print('hello')
                break
        if self.police_black:

            if self.police_black == 1:
                self.coe *= 0.92
                police_black_score += self.__honesty['police_black'][1]

            elif self.police_black == 2:
                self.coe *= 0.97
                police_black_score += self.__honesty['police_black'][2]

            elif self.police_black == 3:
                police_black_score += self.__honesty['police_black'][3]
            else:
                print('公安黑名单数字传输错误，请重新输入')
                police_black_score += self.__honesty['police_black'][4]
        # 法院黑名单
        for i in self.__honesty['court_black']:
            if self.court_black == "" :
                court_black_score += self.__honesty['court_black'][3]
                # print('法院：',court_black_score)
                break
            elif not self.court_black:
                self.coe *= 0.85
            court_black_score += self.__honesty['court_black'][0]
            # print('hello')
            break
        if self.court_black:

            if self.court_black == 1:
                self.coe *= 0.9
                court_black_score += self.__honesty['court_black'][1]

            elif self.court_black == 2:
                self.coe *= 0.95
                court_black_score += self.__honesty['court_black'][2]

            elif self.court_black == 3:
                court_black_score += self.__honesty['court_black'][3]
            else:
                print('法院黑名单数字传输错误，请重新输入')
                court_black_score += self.__honesty['court_black'][4]

        # 缴纳社保比例情况
        for i in self.__honesty['insurance_exp_time']:
            if not self.insurance_exp_time:
                insurance_exp_time_score += self.__honesty['insurance_exp_time'][(0,0)]
                # print('缴纳：',insurance_exp_time_score)
                break
            elif self.insurance_exp_time > i[0] and self.insurance_exp_time <= i[1]:
                insurance_exp_time_score += self.__honesty['insurance_exp_time'][i]
                break
        if self.insurance_exp_time :
            if self.insurance_exp_time < 0.8:
                self.coe *= 0.85
        elif not self.insurance_exp_time:
            self.coe *= 0.85
        #职位是否匹配
        if self.posBg == True:
            posBg_score += self.__honesty['posBg'][self.posBg]
        elif self.posBg == False:
            posBg_score += self.__honesty['posBg'][self.posBg]
            self.coe *= 0.9
        elif not self.posBg:
            posBg_score += self.__honesty['posBg'][False]
            self.coe *= 0.9
        # 学历是否真假
        if self.eduBg == True:
            eduBg_score += self.__honesty['eduBg'][self.eduBg]
        elif self.eduBg == False:
            eduBg_score += self.__honesty['eduBg'][self.eduBg]
            self.coe *= 0.9
        elif not self.eduBg:
            eduBg_score += self.__honesty['eduBg'][False]
            self.coe *= 0.9
        honesty_score = business_black_score + bank_black_score + police_black_score + court_black_score + insurance_exp_time_score + eduBg_score + posBg_score
        return honesty_score



    def __enterprise_score(self):
        """

        :return: 企业对个人评价得分
        """
        # 各项初始化分数
        proSki_score = 15
        worAtt_score = 15
        proQua_score = 15
        leaAbi_score = 15
        comAbi_score = 15
        appreciation_score = 10
        # 专业技能
        if not self.proSki:
            proSki_score += self.__enterprise['proSki'][0]
        else:
            list = [100000,120000,130000,310000,170000,180000,230000,190000,210000,260000]
            if self.position in list :
                proSki_score += self.__enterprise['proSki'][self.proSki][1]
            else:
                proSki_score += self.__enterprise['proSki'][self.proSki][0]

        # 工作态度
        if not self.worAtt:
            worAtt_score += self.__enterprise['worAtt'][0]
        else:
            worAtt_score += self.__enterprise['worAtt'][self.worAtt]
        # 职业素养
        if not self.proQua:
            proQua_score += self.__enterprise['proQua'][0]
        else:
            proQua_score += self.__enterprise['proQua'][self.proQua]
        # 学习能力
        if not self.leaAbi:
            leaAbi_score += self.__enterprise['leaAbi'][0]
        else:
            leaAbi_score += self.__enterprise['leaAbi'][self.leaAbi]
        # 沟通能力
        if not self.comAbi:
            proSki_score += self.__enterprise['comAbi'][0]
        else:
            list = [140000,160000,310000,310000,190000,250000,280000,290000]
            if self.position in list :
                comAbi_score += self.__enterprise['comAbi'][self.comAbi][1]
            else:
                comAbi_score += self.__enterprise['comAbi'][self.comAbi][0]
        # 列入计勋行赏
        if not self.appreciation:
            appreciation_score += self.__enterprise['appreciation'][False]
        else:
            appreciation_score += self.__enterprise['appreciation'][self.appreciation]
        enterprise_score = proSki_score + worAtt_score + proQua_score + leaAbi_score + comAbi_score + appreciation_score
        # print("个人评价：",proSki_score ,worAtt_score ,proQua_score ,leaAbi_score , comAbi_score ,appreciation_score)
        return enterprise_score

    def __buyPower_score(self): # 经济能力得分
        # 分数初始化
        score_travellerScore = 40
        # 判断航旅旅客身份评估
        if not self.travellerScore:
            score_travellerScore += self.__buyPower['travellerScore'][0]
        else:
            score_travellerScore += self.__buyPower['travellerScore'][self.travellerScore]
        return score_travellerScore


