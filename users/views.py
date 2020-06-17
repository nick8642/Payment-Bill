import datetime
from django.shortcuts import render

from users.models import Branch_Master
from users.models import Course_Master
from users.models import Account_Master
from users.models import Student_Master


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def login(request):
    if request.method == "POST":
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        request.method == "POST"
        lperson = request.POST["lperson"]
        if lperson == "Admin":
            if uname == "Admin" and pwd == "Admin123":
                request.session['admin'] = "Admin"
                return render(request, "admin_home.html")
            else:
                return render(request, "login.html", {"result": "Please enter valid login details"})
        else:
            if Account_Master.objects.filter(uname=uname, pwd=pwd).exists():
                acc = Account_Master.objects.get(uname=uname, pwd=pwd)
                request.session['aid'] = acc.id
                request.session['bid'] = acc.bid
                return render(request, "accountant_home.html")
            else:
                return render(request, "login.html", {"result": "Please enter valid password or login details"})
    else:
        return render(request, "login.html")


def add_branch(request):
    if request.session.has_key("admin"):
        if request.method == "POST":
            name = request.POST['name']
            city = request.POST['city']
            address = request.POST['address']
            phone = request.POST['phone']
            branch = Branch_Master(name=name, city=city, address=address, phone=phone)
            branch.save()
            bobj = Branch_Master.objects.all()
            return render(request, "viewallbranches.html", {"branches": bobj})
        else:
            return render(request, "addbranch.html")
    else:
        return render(request, "login.html")


def getBranch(request, id):
    if request.session.has_key("admin"):
        branch = Branch_Master.objects.get(id=id)
        return render(request, "update_branch.html", {"branch": branch})
    else:
        return render(request, "login.html")


def deleteBranch(request, id):
    if request.session.has_key("admin"):
        branch = Branch_Master.objects.get(id=id)
        branch.delete()
        bobj = Branch_Master.objects.all()
        return render(request, "viewallbranches.html", {"branches": bobj})
    else:
        return render(request, "login.html")


def allBranches(request):
    if request.session.has_key("admin"):
        bobj = Branch_Master.objects.all()
        return render(request, "viewallbranches.html", {"branches": bobj})
    else:
        return render(request, "login.html")


def updateBranch(request, id):
    if request.method == "POST":
        name = request.POST['name']
        city = request.POST['city']
        address = request.POST['address']
        phone = request.POST['phone']
        Branch_Master.objects.filter(id=id).update(name=name, address=address, city=city, phone=phone)
        bobj = Branch_Master.objects.all()
        return render(request, "viewallbranches.html", {"branches": bobj})
    else:
        bobj = Branch_Master.objects.all()
        return render(request, "viewallbranches.html", {"branches": bobj})


def addcourse(request):
    if request.session.has_key("admin"):
        if request.method == "POST":
            fees = float(request.POST['fees'])
            name = request.POST['name']
            seats = int(request.POST['seats'])
            bid = int(request.POST['bid'])
            course = Course_Master(name=name, fees=fees, seats=seats, bid=bid)
            course.save()
            course = Course_Master.objects.all()
            return render(request, "viewallcourses.html", {"courses": course})
        else:
            bobj = Branch_Master.objects.all()
            return render(request, "addCourse.html", {"branches": bobj})
    else:
        return render(request, "login.html")


def getCourse(request, id):
    if request.session.has_key("admin"):
        course = Course_Master.objects.get(id=id)
        bobj = Branch_Master.objects.all()
        return render(request, "updateCourse.html", {"course": course, "branches": bobj})
    else:
        return render(request, "login.html")


def deleteCourse(request, id):
    if request.session.has_key("admin"):
        course = Course_Master.objects.get(id=id)
        course.delete()
        course = Course_Master.objects.all()
        return render(request, "viewallcourses.html", {"courses": course})
    else:
        return render(request, "login.html")


def allcourses(request):
    if request.session.has_key("admin"):
        course = Course_Master.objects.all()
        return render(request, "viewallcourses.html", {"courses": course})
    else:
        return render(request, "login.html")


def admin_home(request):
    if request.session.has_key("admin"):
        return render(request, "admin_home.html")
    else:
        return render(request, "login.html")


def addAccount_master(request):
    if request.session.has_key("admin"):
        if request.method == "POST":
            name = request.POST['name']
            uname = request.POST['uname']
            pwd = request.POST['pwd']
            mno = request.POST['mno']
            address = request.POST['address']
            bid = int(request.POST['bid'])
            branch = Branch_Master.objects.get(id=bid)
            doj = datetime.datetime.now().strftime('%d/%m/%Y')
            salary = float(request.POST['salary'])
            email = request.POST['email']
            account_master = Account_Master(branch=branch.name, name=name, uname=uname, pwd=pwd, mno=mno,
                                            address=address,
                                            bid=bid, doj=doj,
                                            salary=salary, email=email)
            account_master.save()
            account = Account_Master.objects.all()
            return render(request, "viewallaccount.html", {"account_master": account})
        else:
            bobj = Branch_Master.objects.all()
            return render(request, "addAccount_master.html", {"branches": bobj})
    else:
        return render(request, "login.html")


def deleteaccount_master(request, id):
    account = Account_Master.objects.get(id=id)
    account.delete()
    account = Account_Master.objects.all()
    return render(request, "viewallaccount.html.", {"account_master": account})


def getaccount(request, id):
    account = Account_Master.objects.get(id=id)
    bobj = Branch_Master.objects.all()
    return render(request, "updateaccount.html", {"account": account, "branches": bobj})


def viewallaccount(request):
    accounts = Account_Master.objects.all()
    return render(request, "viewallaccount.html", {"account_master": accounts})


def updateaccount(request, id):
    if request.method == "POST":
        name = request.POST['name']
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        mno = request.POST['mno']
        address = request.POST['address']
        bid = int(request.POST['bid'])
        doj = request.POST['doj']
        salary = float(request.POST['salary'])
        email = request.POST['email']
        Account_Master.objects.filter(id=id).update(name=name, uname=uname, pwd=pwd, mno=mno, address=address, bid=bid,
                                                    doj=doj, salary=salary, email=email)
        account = Account_Master.objects.all()
        return render(request, "viewallaccount.html", {"account_master": account})

    else:
        account = Account_Master.objects.all()
        return render(request, "viewallaccount.html", {"account_master": account})


def accountant_home(request):
    if request.session.has_key("aid"):
        return render(request, "accountant_home.html")
    else:
        return render(request, "login.html")


def addstudent(request):
    if request.session.has_key("aid"):
        bid = request.session['bid']
        if request.method == "POST":
            paid = float(request.POST['fees'])
            name = request.POST['name']
            email = request.POST['email']
            mno = request.POST['mno']
            cid = request.POST['cid']
            address = request.POST['address']
            course = Course_Master.objects.get(id=cid)
            balance = course.fees - paid
            doj = datetime.datetime.now().strftime('%d/%m/%Y')
            student = Student_Master(course=course.name, bid=bid, name=name, doj=doj, balance=balance, paid=paid,
                                     email=email, mno=mno,
                                     address=address, cid=cid)
            student.save()
            students = Student_Master.objects.all().filter(bid=bid)
            return render(request, "viewallstudent.html", {"students": students})
        else:
            courses = Course_Master.objects.all().filter(bid=bid)
            return render(request, "studentadd.html", {"courses": courses})
    else:
        return render(request, "login.html")


def viewallstudent(request):
    if request.session.has_key("aid"):
        bid = request.session['bid']
        students = Student_Master.objects.all().filter(bid=bid)
        return render(request, "viewallstudent.html", {"students": students})
    else:
        return render(request, "login.html")


def pay_fees12(request, id):
    if request.session.has_key("aid"):
        return render(request, "pay_fees.html", {"sid": id})
    else:
        return render(request, "login.html")


def payed_fees(request, id):
    if request.session.has_key("aid"):
        bid = request.session['bid']
        if request.method == "POST":
            student = Student_Master.objects.get(id=id)
            fees = float(request.POST['fees'])
            paid = fees + student.paid
            balance = student.balance - fees
            Student_Master.objects.filter(id=id).update(balance=balance, paid=paid)
            students = Student_Master.objects.all().filter(bid=bid)
            return render(request, "viewallstudent.html", {"students": students})
        else:
            courses = Course_Master.objects.all().filter(bid=bid)
            return render(request, "studentadd.html", {"courses": courses})
    else:
        return render(request, "login.html")


def student_by_admin(request):
    branches = Branch_Master.objects.all()
    students = Student_Master.objects.all()
    return render(request, "students_by_admin.html", {"students": students, "branches": branches})


def student_by_branch(request, id):
    branches = Branch_Master.objects.all()
    students = Student_Master.objects.all().filter(bid=id)
    return render(request, "students_by_admin.html", {"students": students, "branches": branches})


def user_logout(request):
    del request.session['aid']
    return render(request, "index.html")


def admin_logout(request):
    del request.session['admin']
    return render(request, "index.html")
