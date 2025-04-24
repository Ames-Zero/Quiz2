import os
import django
import random
import sys
# from datetime import timedelta
from datetime import datetime, timedelta
from faker import Faker

# Setup Django environment
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_project.settings')
django.setup()

from employee_app.models import Department, Employee, Attendance, Performance, Project

fake = Faker()

def create_departments(n=3):
    departments = []
    for _ in range(n):
        dept, _ = Department.objects.get_or_create(
            name=fake.unique.company(),
            location=fake.city(),
            description=fake.catch_phrase(),
        )
        departments.append(dept)
    return departments

def create_projects(n=2):
    projects = []
    for _ in range(n):
        proj, _ = Project.objects.get_or_create(
            name=fake.unique.bs().title(),
            description=fake.text(max_nb_chars=50),
            start_date=fake.date_between(start_date='-2y', end_date='today'),
            end_date=None if random.choice([True, False]) else fake.date_between(start_date='today', end_date='+1y'),
        )
        projects.append(proj)
    return projects

def create_employees(departments, projects, n=5):
    employees = []
    for _ in range(n):
        dept = random.choice(departments)
        emp = Employee.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.unique.email(),
            phone=fake.phone_number(),
            hire_date=fake.date_between(start_date='-5y', end_date='today'),
            department=dept,
            job_title=fake.job(),
            salary=round(random.uniform(40000, 120000), 2),
            is_active=random.choice([True, True, False]),
        )
        # Assign projects
        emp.projects.set(random.sample(projects, k=random.randint(1, len(projects))))
        employees.append(emp)
    return employees

def create_attendance(employees, days_per_employee=5):
    for emp in employees:
        for _ in range(days_per_employee):
            date = fake.date_between(start_date='-30d', end_date='today')
            check_in = fake.time_object()
            check_out = (datetime.combine(date, check_in) + timedelta(hours=8)).time()
            Attendance.objects.create(
                employee=emp,
                date=date,
                check_in=check_in,
                check_out=check_out,
                status=random.choice(['Present', 'Absent', 'Remote']),
                remarks=fake.sentence(nb_words=6),
            )

def create_performance(employees, reviews_per_employee=2):
    for emp in employees:
        for _ in range(reviews_per_employee):
            Performance.objects.create(
                employee=emp,
                review_date=fake.date_between(start_date=emp.hire_date, end_date='today'),
                score=random.randint(1, 10),
                reviewer=fake.name(),
                comments=fake.sentence(nb_words=10),
                goal_achieved=random.choice([True, False]),
            )

if __name__ == '__main__':
    print("Generating departments...")
    departments = create_departments()
    print("Generating projects...")
    projects = create_projects()
    print("Generating employees...")
    employees = create_employees(departments, projects)
    print("Generating attendance records...")
    create_attendance(employees)
    print("Generating performance records...")
    create_performance(employees)
    print("Data generation complete.")
