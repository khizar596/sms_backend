from fastapi import FastAPI , HTTPException
from fastapi.middleware.cors import CORSMiddleware

from routes import (   Examinationadmin_route,Accountant2_route,HR2_route,StudentAdmin_route,Staff2_route,Teacher_route,Userlogin_route,Admin_route,stdnoticeboard_route,student_route,Salary_route,Section_route,
                        StudentAttendence_route,Studentcomplain_route,Parent_route,
                        Assignment_route,EmpAttendence_route,EmpComplain_route,
                        Employee_route,Empnoticeboard_route,Exam_route,Chatbox_route,
                        Class_route,Classsubject_route,Course_route,Datesheet_route,
                        Fee_route,Marksheet_route,Question_route,Quizz_route,Timetable_route
                        )

# from models import ( Student, StudentAdmin, StudentAttendence, StudentComplain, 
#                     StudentNoticeboard,Parent,
#                     Teacher,Timetable, Courses,Accountant2,
#                     Admin2,Admin_route, Assignment, chatbox,
#                     Class,Class_subject,EmployeeNoticeboard2, employeeattendance2,
#                     Employee2,EmployeeComplain,Exam,ExaminationAdmin2,Fee,HR2,
#                     Marksheet,Questions,Quiz,Salary2,Section,Staff2)
#App Creations
app=FastAPI()
origins = [ 'https://localhost:8000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(Userlogin_route.router)

#ADMIN
app.include_router(Admin_route.router)
# #Employee
# app.include_router(Employee_route.router)
# app.include_router(Empnoticeboard_route.router)
# app.include_router(EmpComplain_route.router)
# app.include_router(EmpAttendence_route.router)
# app.include_router(Staff2_route.router)
# app.include_router(StudentAdmin_route.router)

# app.include_router(HR2_route.router)
# app.include_router(Accountant2_route.router)
# app.include_router(Examinationadmin_route.router)

# app.include_router(StudentAdmin_route.router)


# # #Student
# app.include_router(student_route.router)
# app.include_router(Studentcomplain_route.router)


# #PARENT
# app.include_router(Parent_route.router)
# app.include_router(Fee_route.router)
# app.include_router(Question_route.router)

# app.include_router(Teacher_route.router)

# #COMBINE ROUTES
# app.include_router(Marksheet_route.router)
# app.include_router(Datesheet_route.router)
# app.include_router(Timetable_route.router)
# app.include_router(stdnoticeboard_route.router)
# app.include_router(StudentAttendence_route.router)
# app.include_router(Quizz_route.router)
# app.include_router(Salary_route.router)
# app.include_router(Section_route.router)
# app.include_router(Class_route.router)
# app.include_router(Exam_route.router)
# app.include_router(Course_route.router)
app.include_router(Chatbox_route.router)
# app.include_router(Assignment_route.router)
# app.include_router(Classsubject_route.router)