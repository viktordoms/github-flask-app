from flask import request, redirect, render_template
from app import app, db
from models.models import *


@app.route('/employees/new', methods=['POST', 'GET'])
def add_employees():
    if request.method == 'POST':
        employee_id = request.form['employee_id'],
        first_name = request.form['first_name'],
        last_name = request.form['last_name'],
        email = request.form['email'],
        phone_number = request.form['phone_number'],
        hire_date = request.form['hire_date'],
        job_id = request.form['job_id'],
        salary = request.form["salary"],
        commission_pct = request.form['commission_pct'],
        department_id = request.form['department_id'],
        manager_id = request.form['manager_id']

        employee = Employees(
            employee_id=employee_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            hire_date=hire_date,
            job_id=job_id,
            salary=salary,
            commission_pct=commission_pct,
            department_id=department_id,
            manager_id=manager_id
        )

        try:
            db.session.add(employee)
            db.session.commit()
            return redirect('/ok_add')
        except:
            return redirect('/error_add')

    else:
        return render_template('create-employees.html')


@app.route('/departments/new', methods=['POST', 'GET'])
def add_department():
    if request.method == 'POST':
        department_id = request.form['department_id'],
        department_name = request.form['department_name'],
        manager_id = request.form['manager_id'],
        location_id = request.form['location_id']

        department = Departments(
            department_id=department_id,
            department_name=department_name,
            manager_id=manager_id,
            location_id=location_id)

        try:
            db.session.add(department)
            db.session.commit()
            return redirect('/ok_add')
        except:
            return redirect('/error_add')

    else:
        return render_template('create_department.html')


@app.route('/jobs/new', methods=['POST', 'GET'])
def add_jobs():
    if request.method == 'POST':
        job_id = request.form['job_id'],
        job_title = request.form['job_title'],
        min_salary = request.form['min_salary'],
        max_salary = request.form['max_salary'],

        job = Jobs(
            job_id=job_id,
            job_title=job_title,
            min_salary=min_salary,
            max_salary=max_salary)

        try:
            db.session.add(job)
            db.session.commit()
            return redirect('/ok_add')
        except:
            return redirect('/error_add')

    else:
        return render_template('create_jobs.html')


@app.route('/job-history/new', methods=['POST', 'GET'])
def add_job_history():
    if request.method == 'POST':
        employee_id = request.form['employee_id'],
        start_date = request.form['start_date'],
        end_date = request.form['end_date'],
        job_id = request.form['job_id'],
        department_id = request.form['department_id']

        job_history = JobHistory(
            job_id=job_id,
            employee_id=employee_id,
            start_date=start_date,
            end_date=end_date,
            department_id=department_id)

        try:
            db.session.add(job_history)
            db.session.commit()
            return redirect('/ok_add')
        except:
            return redirect('/error_add')

    else:
        return render_template('create_job_history.html')


@app.route('/regions/new', methods=['POST', 'GET'])
def add_regions():
    if request.method == 'POST':
        region_id = request.form['region_id'],
        region_name = request.form['region_name'],

        region = Regions(
            region_id=region_id,
            region_name=region_name)

        try:
            db.session.add(region)
            db.session.commit()
            return redirect('/ok_add')
        except:
            return redirect('/error_add')

    else:
        return render_template('create_regions.html')


@app.route('/countries/new', methods=['POST', 'GET'])
def add_countries():
    if request.method == 'POST':
        country_id = request.form['country_id'],
        country_name = request.form['country_name'],
        region_id = request.form['region_id']

        country = Countries(
            country_id=country_id,
            country_name=country_name,
            region_id=region_id)

        try:
            db.session.add(country)
            db.session.commit()
            return redirect('/ok_add')
        except:
            return redirect('/error_add')

    else:
        return render_template('create_countries.html')


@app.route('/locations/new', methods=['POST', 'GET'])
def add_locations():
    if request.method == 'POST':
        location_id = request.form['location_id'],
        street_address = request.form['street_address'],
        postal_code = request.form['postal_code'],
        city = request.form['city'],
        state_province = request.form['state_province'],
        country_id = request.form['country_id']

        location = Locations(
            country_id=country_id,
            location_id=location_id,
            street_address=street_address,
            postal_code=postal_code,
            city=city,
            state_province=state_province)

        try:
            db.session.add(location)
            db.session.commit()
            return redirect('/ok_add')
        except:
            return redirect('/error_add')

    else:
        return render_template('create_locations.html')


@app.route('/ok_add')
def ok_add():
    return render_template('ok_add.html')


@app.route('/error_add')
def error_add():
    return render_template('error_add.html')
