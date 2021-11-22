from sqlalchemy import ForeignKey

from app import db


class Employees(db.Model):
    __tablename__ = 'employees'
    employee_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50))
    phone_number = db.Column(db.Integer)
    hire_date = db.Column(db.String(40))
    salary = db.Column(db.Integer)
    commission_pct = db.Column(db.Integer)

    job_id = db.Column(db.Integer, ForeignKey("jobs.job_id"))
    department_id = db.Column(db.Integer, ForeignKey("departments.department_id"))
    manager_id = db.Column(db.Integer, ForeignKey("employees.employee_id"))

    department = db.relationship("Departments", foreign_keys=[department_id])
    manager = db.relationship("Employees", remote_side=[employee_id], backref="manager_employee")
    job = db.relationship("Jobs", foreign_keys=[job_id])

    def __repr__(self):
        return 'Employees %r>' % self.employee_id

    @property
    def serialize(self):
        return {
            "employee_id": self.employee_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            'salary': self.salary,
            "phone_number": self.phone_number,
            "commission_pct": self.commission_pct,
            "hire_date": self.hire_date,
            "department_id": self.department_id,
            "manager_id": self.manager_id,
            "job_id": self.job_id
        }


class Departments(db.Model):
    __tablename__ = 'departments'
    department_id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(45), nullable=False)
    manager_id = db.Column(db.Integer, ForeignKey("employees.employee_id"))
    location_id = db.Column(db.Integer, ForeignKey("locations.location_id"), nullable=False)

    manager = db.relationship("Employees", foreign_keys=[manager_id])
    location = db.relationship("Locations", foreign_keys=[location_id])

    def __repr__(self):
        return 'Departments %r>' % self.department_id

    @property
    def serialize(self):
        return {
            "department_id": self.department_id,
            "department_name": self.department_name,
            "manager_id": self.manager_id,
            "location_id": self.location_id,
        }


class Jobs(db.Model):
    __tablename__ = 'jobs'
    job_id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(45), nullable=False)
    min_salary = db.Column(db.Integer, nullable=False)
    max_salary = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return 'Jobs %r>' % self.job_id

    @property
    def serialize(self):
        return {
            "job_id": self.job_id,
            "job_title": self.job_title,
            "min_salary": self.min_salary,
            "max_salary": self.max_salary,
        }


class JobHistory(db.Model):
    __tablename__ = 'jobhistory'
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, ForeignKey("employees.employee_id"), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date,)
    job_id = db.Column(db.Integer, ForeignKey("jobs.job_id"), nullable=False)
    department_id = db.Column(db.Integer, ForeignKey("departments.department_id"), nullable=False)

    employee = db.relationship("Employees", foreign_keys=[employee_id])
    job = db.relationship("Jobs", foreign_keys=[job_id])
    department = db.relationship("Departments", foreign_keys=[department_id])

    def __repr__(self):
        return 'JobHistory %r>' % self.employee_id

    @property
    def serialize(self):
        return {
            "employee_id": self.employee_id,
            "start_date": self.start_date,
            "end_date": self.end_date
        }


class Regions(db.Model):
    __tablename__ = 'regions'
    region_id = db.Column(db.Integer, primary_key=True)
    region_name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return 'Regions %r>' % self.region_id

    @property
    def serialize(self):
        return {
            "region_id": self.region_id,
            "region_name": self.region_name
        }


class Countries(db.Model):
    __tablename__ = 'countries'
    country_id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(50), nullable=False)
    region_id = db.Column(db.Integer, ForeignKey("regions.region_id"), nullable=False)

    region = db.relationship("Regions", foreign_keys=[region_id])

    def __repr__(self):
        return 'Countries %r>' % self.country_id

    @property
    def serialize(self):
        return {
            "country_id": self.country_id,
            "country_name": self.country_name
        }


class Locations(db.Model):
    __tablename__ = 'locations'
    location_id = db.Column(db.Integer, primary_key=True)
    street_address = db.Column(db.String(100), nullable=False)
    postal_code = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(25), nullable=False)
    state_province = db.Column(db.String(40), nullable=False)
    country_id = db.Column(db.Integer, ForeignKey("countries.country_id"), nullable=False)

    country = db.relationship("Countries", foreign_keys=[country_id])

    def __repr__(self):
        return 'Locations %r>' % self.location_id

    @property
    def serialize(self):
        return {
            "location_id_id": self.location_id,
            "street_address": self.street_address,
            "postal_code": self.postal_code,
            "city": self.city,
            "state_province": self.state_province
        }
