from app import app, db
from flask import render_template, redirect, request
from models.models import *
from sqlalchemy import and_, or_


@app.route('/employees')
def info_employee():
    employee = Employees.query.all()
    return render_template('info_employee.html', employee=employee)


@app.route('/employees/<int:employee_id>')
def info_employee_detail(employee_id):
    employee = Employees.query.get(employee_id)
    return render_template('info_employee_detail.html', employee=employee)


@app.route('/employees/<int:employee_id>/delete')
def info_employee_delete(employee_id):
    employee = Employees.query.get_or_404(employee_id)

    try:
        db.session.delete(employee)
        db.session.commit()
        return redirect('/ok_add')
    except:
        return redirect('/error_add')


@app.route('/departments')
def info_department():
    department = Departments.query.all()
    return render_template('info_department.html', department=department)


@app.route('/departments/<int:department_id>/delete')
def info_department_delete(department_id):
    department = Departments.query.get_or_404(department_id)

    try:
        db.session.delete(department)
        db.session.commit()
        return redirect('/ok_add')
    except:
        return redirect('/error_add')


@app.route('/jobs')
def info_jobs():
    job = Jobs.query.all()
    return render_template('info_jobs.html', job=job)


@app.route('/jobs/<int:job_id>/delete')
def info_job_delete(job_id):
    job = Jobs.query.get_or_404(job_id)

    try:
        db.session.delete(job)
        db.session.commit()
        return redirect('/ok_add')
    except:
        return redirect('/error_add')


@app.route('/job-history')
def info_job_history():
    job_history = JobHistory.query.all()
    return render_template('info_job_history.html', job_history=job_history)


@app.route('/job-history/<int:id>/delete')
def info_job_history_delete(id):
    job_history = JobHistory.query.get_or_404(id)

    try:
        db.session.delete(job_history)
        db.session.commit()
        return redirect('/ok_add')
    except:
        return redirect('/error_add')


@app.route('/regions')
def info_regions():
    regions = Regions.query.all()
    return render_template('info_regions.html', regions=regions)


@app.route('/regions/<int:region_id>/delete')
def info_regions_delete(region_id):
    region = Regions.query.get_or_404(region_id)

    try:
        db.session.delete(region)
        db.session.commit()
        return redirect('/ok_add')
    except:
        return redirect('/error_add')


@app.route('/countries')
def info_countries():
    countries = Countries.query.all()
    return render_template('info_countries.html', countries=countries)


@app.route('/countries/<int:country_id>/delete')
def info_countries_delete(country_id):
    country = Countries.query.get_or_404(country_id)

    try:
        db.session.delete(country)
        db.session.commit()
        return redirect('/ok_add')
    except:
        return redirect('/error_add')


@app.route('/locations')
def info_locations():
    locations = Locations.query.all()
    return render_template('info_locations.html', locations=locations)


@app.route('/locations/<int:location_id>/delete')
def info_locations_delete(location_id):
    location = Locations.query.get_or_404(location_id)

    try:
        db.session.delete(location)
        db.session.commit()
        return redirect('/ok_add')

    except:
        return redirect('/error_add')


@app.route('/locations/<int:location_id>')
def info_location_detail(location_id):
    location = Locations.query.get(location_id)
    return render_template('info_location_detail.html', location=location)


@app.route('/search/result', methods=["GET"])
def search():
    conditions = []
    if request.args.get('first_name'):
        conditions.append(Employees.first_name.like(request.args['first_name']))
    if request.args.get('last_name'):
        conditions.append(Employees.last_name.like(request.args['last_name']))
    if request.args.get('email'):
        conditions.append(Employees.email.like(request.args['email']))
    if request.args.get('phone_number'):
        conditions.append(Employees.phone_number.like(request.args['phone_number']))
    if request.args.get('hire_date'):
        conditions.append(Employees.hire_date.like(request.args['hire_date']))
    if request.args.get('salary'):
        conditions.append(Employees.salary.like(request.args['salary']))
    if request.args.get('commission_pct'):
        conditions.append(Employees.commission_pct.like(request.args['commission_pct']))
    if request.args.get('job_id'):
        conditions.append(Employees.job_id.like(request.args['job_id']))
    if request.args.get('department_id'):
        conditions.append(Employees.department_id.like(request.args['department_id']))
    if request.args.get('manager_id'):
        conditions.append(Employees.manager_id.like(request.args['manager_id']))

    if_search = Employees.query.filter(and_(*conditions))
    result = if_search.all()
    return render_template('result-search.html', search_dict=result)


@app.route('/search')
def result_search():
    return render_template('search.html')


# @app.route('/print')
# def print():
#     return render_template('print')




