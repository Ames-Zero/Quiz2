from django.db import models

DEF_MAX_LEN = 100

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=DEF_MAX_LEN)
    hire_date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='employees')
    job_title = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    status = models.CharField(max_length=DEF_MAX_LEN, choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Remote', 'Remote')])
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.employee} - {self.date}"

class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='performances')
    review_date = models.DateField()
    score = models.IntegerField()
    reviewer = models.CharField(max_length=100)
    comments = models.TextField(blank=True)
    goal_achieved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee} - {self.review_date}"

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    employees = models.ManyToManyField(Employee, related_name='projects')

    def __str__(self):
        return self.name
