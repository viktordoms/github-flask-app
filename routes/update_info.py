from app import app, db
from flask import request, redirect, render_template
from models.models import *


@app.route('/employees/<int:employee_id>/update', methods=['POST', 'GET'])
def update_employees(employee_id):
    employee = Employees.query.get(employee_id)
    if request.method == 'POST':
        employee.first_name = request.form['first_name'],
        employee.last_name = request.form['last_name'],
        employee.email = request.form['email'],
        employee.phone_number = request.form['phone_number'],
        employee.hire_date = request.form['hire_date'],
        employee.job_id = request.form['job_id'],
        employee.salary = request.form["salary"],
        employee.commission_pct = request.form['commission_pct'],
        employee.department_id = request.form['department_id'],
        employee.manager_id = request.form['manager_id']

        try:
            db.session.commit()
            return redirect('/ok_add')
        except:
            return redirect('/error_add')

    else:
        return render_template('update_employee.html', employee=employee)


@app.route('/departments/<int:department_id>/update', methods=['POST', 'GET'])
def update_department(department_id):
    department = Departments.query.get(department_id)
    if request.method == 'POST':
        department.department_id = request.form['department_id'],
        department.department_name = request.form['department_name'],
        department.manager_id = request.form['manager_id'],
        department.location_id = request.form['location_id']

        try:
            db.session.commit()
            return redirect('/ok_add')
        except:
            return redirect('/error_add')

    else:
        return render_template('update_department.html', department=department)


@app.route('/jobs/<int:job_id>/update', methods=['POST', 'GET'])
def update_job(job_id):
    job = Jobs.query.get(job_id)
    if request.method == 'POST':
        job.job_id = request.form['job_id'],
        job.job_title = request.form['job_title'],
        job.min_salary = request.form['min_salary'],
        job.max_salary = request.form['max_salary']

        try:
            db.session.commit()
            return redirect('/ok_add')
        except:
            return redirect('/error_add')

    else:
        return render_template('update_job.html', job=job)


@app.route('/job-history/<int:id>/update', methods=['POST', 'GET'])
def update_job_history(id):
    job_history = JobHistory.query.get(id)
    if request.method == 'POST':
        job_history.employee_id = request.form['employee_id'],
        job_history.start_date = request.form['start_date'],
        job_history.end_date = request.form['end_date'],
        job_history.job_id = request.form['job_id'],
        job_history. department_id = request.form['department_id']

        try:
            db.session.commit()
            return redirect('/ok_add')
        except:
            return redirect('/error_add')

    else:
        return render_template('update_job_history.html', job_history=job_history)


@app.route('/locations/<int:location_id>/update', methods=['POST', 'GET'])
def update_locations(location_id):
    location = Locations.query.get(location_id)
    if request.method == 'POST':
        location.location_id = request.form['location_id'],
        location.street_address = request.form['street_address'],
        location.postal_code = request.form['postal_code'],
        location.city = request.form['city'],
        location.state_province = request.form['state_province'],
        location.country_id = request.form['country_id']

        try:
            db.session.commit()
            return redirect('/ok_add')
        except:
            return redirect('/error_add')

    else:
        return render_template('update_locations.html', location=location)
