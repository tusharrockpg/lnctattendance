import requests
from urllib.parse import quote
from bs4 import BeautifulSoup
import re
from firebase import Firebase
import os
config = {
    'apiKey': str(os.getenv('apiKey3')),
    'authDomain': "testing-f442d.firebaseapp.com",
    'databaseURL': "https://testing-f442d.firebaseio.com",
    'projectId': "testing-f442d",
    'storageBucket': "testing-f442d.appspot.com",
}
database = Firebase(config).database()
def main(username,password,lnctu=False):
    s = requests.Session()
    url = "http://portal.lnct.ac.in/Accsoft2/StudentLogin.aspx?ctl00%24ScriptManager1=ctl00%24cph1%24UpdatePanel5%7Cctl00%24cph1%24btnStuLogin&__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUJLTk3NzUxOTMxD2QWAmYPZBYCAgMPZBYEAgcPZBYGAgcPZBYCZg9kFgICAQ8QZGQWAWZkAgkPZBYCZg9kFgICAQ8WAh4HVmlzaWJsZWcWAgIED2QWAmYPZBYCAgEPZBYCZg9kFgICAQ9kFgRmD2QWAmYPZBYCAgEPZBYCZg9kFgICAQ8QZGQWAGQCAQ9kFgJmD2QWAgIDDxYCHgVWYWx1ZQUCNTFkAgsPZBYCZg9kFgICAQ8WAh8AaBYCAgQPZBYCZg9kFgICAQ9kFgJmD2QWAgIBD2QWBGYPZBYCZg9kFgICAQ9kFgJmD2QWAgIBDxAPFgYeDURhdGFUZXh0RmllbGQFB0ZpblllYXIeDkRhdGFWYWx1ZUZpZWxkBQlGaW5ZZWFySUQeC18hRGF0YUJvdW5kZ2QQFQ8KLS1TZWxlY3QtLQoyMDE5LTIwMjAgCjIwMTgtMjAxOSAKMjAxNy0yMDE4IAoyMDE2LTIwMTcgCjIwMTUtMjAxNiAKMjAxNC0yMDE1IAoyMDEzLTIwMTQgCjIwMTItMjAxMyAKMjAxMS0yMDEyIAoyMDEwLTIwMTEgCjIwMDktMjAxMCAKMjAwOC0yMDA5IAoyMDA3LTIwMDggCjIwMDYtMjAwNyAVDwEwAjE0AjEzAjEyAjExAjEwATkBOAE3ATYBNQE0ATMBMgExFCsDD2dnZ2dnZ2dnZ2dnZ2dnZxYBAgFkAgEPZBYCZg9kFgICAQ9kFgJmD2QWAgIBDxBkZBYAZAIJDw8WAh4EVGV4dAULMjMtSmFuLTIwMjBkZGQjNMuk5EJq5qSPZq4EJBD6tB0pUuNkWeHCb1PHtBhULw%3D%3D&__EVENTVALIDATION=%2FwEdAAbizBDBTGYL1tI3qzYeuPAJseDjO4OjzzusyZ26WwJoA%2BzQjwyf5g%2B4ezBNg2ywlcRWRY5uqcphA2smPJPFzLHn%2Bmo9SV2v%2FSHtiocBMWq7cO7ou5vayuKtr5%2FnHS8pGkVcIkhB%2BazkX5InlwRHe1E7CMFQAS9GRJ3Y3jJTO15Clg%3D%3D&ctl00%24cph1%24rdbtnlType=2&ctl00%24cph1%24txtStuUser="+str(username) + "&ctl00%24cph1%24txtStuPsw=" + quote(str(password)) + "&__ASYNCPOST=true&ctl00%24cph1%24btnStuLogin=Login%20%3E%3E"
    if(lnctu == True):
        url = "http://accsoft.lnctu.ac.in/Accsoft2/Login.aspx?ctl00%24ScriptManager1=ctl00%24cph1%24UpdatePanel5%7Cctl00%24cph1%24btnStuLogin&ctl00%24cph1%24rdb=rdp&ctl00%24cph1%24txtStuUser=" +str(username) +"&ctl00%24cph1%24txtStuPsw=" + quote(password) + "&__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwULLTEwNDk1ODMyMTYPZBYCZg9kFgICAw9kFgQCBw9kFgYCBw9kFgJmD2QWBAIBDxAPFgIeB0NoZWNrZWRoZGRkZAIDDxAPFgIfAGdkZGRkAgkPZBYCZg9kFgICAQ8WAh4HVmlzaWJsZWdkAgsPZBYCZg9kFgICAQ8WAh8BaBYGAgEPZBYCZg9kFgQCAQ8WAh4FVmFsdWUF6QF7CiAgImlwIjogIjI3LjYyLjE1MC4xNzQiLAogICJjaXR5IjogIlJhaXB1ciIsCiAgInJlZ2lvbiI6ICJDaGhhdHRpc2dhcmgiLAogICJjb3VudHJ5IjogIklOIiwKICAibG9jIjogIjIxLjIzMzMsODEuNjMzMyIsCiAgIm9yZyI6ICJBUzQ1NjA5IEJoYXJ0aSBBaXJ0ZWwgTHRkLiBBUyBmb3IgR1BSUyBTZXJ2aWNlIiwKICAicG9zdGFsIjogIjQ5MjAxMyIsCiAgInRpbWV6b25lIjogIkFzaWEvS29sa2F0YSIKfWQCAw8WAh8CBQ43MTEzZTU5OGZmNmU1OWQCAw9kFgJmD2QWAgIDDw8WAh8BaGRkAgQPZBYCZg9kFgICAQ9kFgJmD2QWAgIBD2QWBGYPZBYCZg9kFgICAQ9kFgJmD2QWAgIBDxAPFgYeDURhdGFUZXh0RmllbGQFB0ZpblllYXIeDkRhdGFWYWx1ZUZpZWxkBQlGaW5ZZWFySUQeC18hRGF0YUJvdW5kZ2QQFQwKLS1TZWxlY3QtLQoyMDE5LTIwMjAgCjIwMTgtMjAxOSAKMjAxNy0yMDE4IAoyMDE2LTIwMTcgCjIwMTUtMjAxNiAKMjAxNC0yMDE1IAoyMDEzLTIwMTQgCjIwMTItMjAxMyAKMjAxMS0yMDEyIAoyMDEwLTIwMTEgCjIwMDktMjAxMCAVDAEwAjExAjEwATkBOAE3ATYBNQE0ATMBMgExFCsDDGdnZ2dnZ2dnZ2dnZxYBAgFkAgEPZBYCZg9kFgICAQ9kFgJmD2QWAgIBDxBkZBYAZAIJDw8WAh4EVGV4dAULMDEtTWFyLTIwMjBkZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAwUOY3RsMDAkY3BoMSRyZGYFDmN0bDAwJGNwaDEkcmRmBQ5jdGwwMCRjcGgxJHJkcBWJcaamtDeCXfaIrWtUKXuRZHXCCO1zJCcfy3F%2FmXNE&__EVENTVALIDATION=%2FwEWBgLby5ChAgKo4vbNDAL66OaeDALF29%2B1DQLwxNyhCALInIuCCA0XJI9riPA6nYs7KduveWs%2Fluwarj3KoEtaglr%2ByyII&__ASYNCPOST=true&ctl00%24cph1%24btnStuLogin=Login%20%3E%3E"
    mhtml = s.get(url).text
    soupm = BeautifulSoup(mhtml, 'html.parser')
    login = False
    try:
        title = str(soupm.title.text)
        title = title.split()
        title.reverse()
        if (len(title) > 0):
            if (title[0] == "DashBoard"):
                login = True
        else:
            login = True
    except:
        print('error')
    # if login==True and lnctu==False:
    #     totalRequests=database.child("stats/totalRequests").get().val()
    #     print(totalRequests)
    #     database.child("stats").set({
    #         "totalRequests":int(totalRequests)+1
    #     })
    #     name = soupm.findAll("td", {'class': "TopMenuTD_2"})[2].text.strip()
    #     college = soupm.findAll("td", {'class': "LoginInfo"})[0].text.strip()
    #     rawData  = soupm.find_all("td",{'class':"TopMenuTD_2"})[6].text.strip()
    #     branch = re.sub('[^A-Za-z0 ]+', '', rawData).strip("BTech  Sem")
    #     Semester = re.sub('[^1-9]+', '', rawData)
    #     attendenceurl = "http://portal.lnct.ac.in/Accsoft2/Parents/StuAttendanceStatus.aspx"
    #     ahtml = s.get(attendenceurl).text
    #     soupa = BeautifulSoup(ahtml, 'html.parser')
    #     total = soupa.find(id="ctl00_ContentPlaceHolder1_lbltotperiod").text
    #     attendence = soupa.find(id="ctl00_ContentPlaceHolder1_lbltotalp").text
    #     attendence = int(re.findall(r'\d+', attendence)[0])
    #     total = int(re.findall(r'\d+', total)[0])
    #     lecturesNeeded =0
    #     daysNeeded = 0
    #     if(total==0):
    #         percentage  = 100
    #     else:
    #         percentage = round(attendence/total*100,2)
    #     if(percentage<75):
    #         lecturesNeeded = ((0.75*total)-attendence)/(0.25)
    #         daysNeeded = round(lecturesNeeded/7)
    #     return [name, total, attendence,percentage,branch,college,Semester,lecturesNeeded,daysNeeded]
	#
    if login==True:
        college = "LNCT"
        if lnctu==True:
            college = "LNCTU"
        attendenceurl = "http://accsoft.lnctu.ac.in/AccSoft2/Parents/StuAttendanceStatus.aspx"
        if lnctu==False:
            attendenceurl = "http://portal.lnct.ac.in/AccSoft2/Parents/StuAttendanceStatus.aspx"
        ahtml = s.get(attendenceurl).text
        soupa = BeautifulSoup(ahtml, 'html.parser')
        total = soupa.find(id="ctl00_ContentPlaceHolder1_lbltotperiod").text
        attendence = soupa.find(id="ctl00_ContentPlaceHolder1_lbltotalp").text
        leaves = soupa.find(id="ctl00_ContentPlaceHolder1_lbltotall").text
        leaves = int(re.findall(r'\d+', leaves)[0])
        print('leaves',leaves)
        attendence = int(re.findall(r'\d+', attendence)[0])
        attendence += leaves
        total = int(re.findall(r'\d+', total)[0])
        lecturesNeeded = 0
        daysNeeded = 0
        if (total == 0):
            percentage = 100
        else:
            percentage = round(attendence / total * 100, 2)
        if (percentage < 75):
            lecturesNeeded = ((0.75 * total) - attendence) / (0.25)
            daysNeeded = round(lecturesNeeded / 7)
        try:
            database.child('college').child(college).child(username).update({
                'username':username
            })
        except:
            print('error in updating students college data')

        # database.child('attendance').child(username).set({
        #     'attendance': percentage
        # })
        return ['', total, attendence, percentage, '', '', '', lecturesNeeded, daysNeeded]
    else:
        return "error"
