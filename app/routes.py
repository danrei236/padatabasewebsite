import pandas as pd
from flask import Blueprint, render_template, redirect, url_for, flash, request, Response
from app import db
from app.models import Member
from app.forms import MemberForm, SearchForm

# Define Blueprints
main_routes = Blueprint('main', __name__)
member_routes = Blueprint('member', __name__)

# Default Admin Password
ADMIN_PASSWORD = "AdminPA#2025"

# Main Routes
@main_routes.route('/')
def home():
    return render_template('home.html')

# Member Routes
@member_routes.route('/members')
def members():
    sort_by = request.args.get('sort_by', 'first_names')  # Default sorting column
    order = request.args.get('order', 'asc')  # Default sorting order

    # Filtering logic based on query parameters
    filters = []
    if request.args.get('street_address'):
        filters.append(Member.street_address.like(f"%{request.args.get('street_address')}%"))
    if request.args.get('ward'):
        filters.append(Member.ward.like(f"%{request.args.get('ward')}%"))
    if request.args.get('region'):
        filters.append(Member.region.like(f"%{request.args.get('region')}%"))
    if request.args.get('municipality'):
        filters.append(Member.municipality.like(f"%{request.args.get('municipality')}%"))
    if request.args.get('city'):
        filters.append(Member.city.like(f"%{request.args.get('city')}%"))
    if request.args.get('province'):
        filters.append(Member.province.like(f"%{request.args.get('province')}%"))
    if request.args.get('iec_registered'):
        filters.append(Member.iec_registered == request.args.get('iec_registered'))
    if request.args.get('voting_district'):
        filters.append(Member.voting_district.like(f"%{request.args.get('voting_district')}%"))

    # Dynamically determine the column to sort by
    if hasattr(Member, sort_by):
        column = getattr(Member, sort_by)
        if order == 'desc':
            column = column.desc()
        members = Member.query.filter(*filters).order_by(column).all()
    else:
        members = Member.query.filter(*filters).all()  # Fallback if invalid column

    return render_template('members.html', members=members, sort_by=sort_by, order=order)

@member_routes.route('/add_member', methods=['GET', 'POST'])
def add_member():
    form = MemberForm()
    if form.validate_on_submit():
        # Check if member already exists by ID Number
        existing_member = Member.query.filter_by(id_number=form.id_number.data).first()
        if existing_member:
            flash('Member with this ID Number already exists!', 'danger')
            return redirect(url_for('member.add_member'))

        # Create and add member to the database
        member = Member(
            first_names=form.first_names.data,
            surname=form.surname.data,
            id_number=form.id_number.data,
            gender=form.gender.data,
            language=form.language.data,
            mobile_number=form.mobile_number.data,
            alternative_number=form.alternative_number.data,
            ward=form.ward.data,
            region=form.region.data,
            municipality=form.municipality.data,
            house_number=form.house_number.data,
            street_address=form.street_address.data,
            suburb=form.suburb.data,
            city=form.city.data,
            province=form.province.data,
            postal_code=form.postal_code.data,
            iec_registered=form.iec_registered.data,
            pat_no=form.pat_no.data,
            voting_district=form.voting_district.data
        )
        db.session.add(member)
        db.session.commit()

        flash('Member added successfully!', 'success')
        return redirect(url_for('member.members'))

    return render_template('add_member.html', form=form)

@member_routes.route('/edit_member/<int:member_id>', methods=['GET', 'POST'])
def edit_member(member_id):
    member = Member.query.get_or_404(member_id)
    form = MemberForm(obj=member)

    if form.validate_on_submit():
        password = request.form.get("admin_password")
        if password != ADMIN_PASSWORD:
            flash("Incorrect password! Member details not updated.", "danger")
            return redirect(url_for('member.view_member', member_id=member.id))

        # Update member details
        member.first_names = form.first_names.data
        member.surname = form.surname.data
        member.id_number = form.id_number.data
        member.gender = form.gender.data
        member.language = form.language.data
        member.mobile_number = form.mobile_number.data
        member.alternative_number = form.alternative_number.data
        member.ward = form.ward.data
        member.region = form.region.data
        member.municipality = form.municipality.data
        member.house_number = form.house_number.data
        member.street_address = form.street_address.data
        member.suburb = form.suburb.data
        member.city = form.city.data
        member.province = form.province.data
        member.postal_code = form.postal_code.data
        member.iec_registered = form.iec_registered.data
        member.pat_no = form.pat_no.data
        member.voting_district = form.voting_district.data

        db.session.commit()

        flash('Member updated successfully!', 'success')
        return redirect(url_for('member.members'))

    return render_template('edit_member.html', form=form, member=member)

@member_routes.route('/delete_member/<int:member_id>', methods=['POST'])
def delete_member(member_id):
    member = Member.query.get_or_404(member_id)

    password = request.form.get("admin_password")
    if password != ADMIN_PASSWORD:
        flash("Incorrect password! Member not deleted.", "danger")
        return redirect(url_for('member.view_member', member_id=member.id))

    db.session.delete(member)
    db.session.commit()
    flash('Member deleted successfully!', 'success')
    return redirect(url_for('member.members'))

@member_routes.route('/search_members', methods=['GET', 'POST'])
def search_members():
    form = SearchForm()
    if form.validate_on_submit():
        filters = []
        if form.id_number.data:
            filters.append(Member.id_number == form.id_number.data)
        if form.pat_no.data:
            filters.append(Member.pat_no == form.pat_no.data)

        if filters:
            members = Member.query.filter(*filters).all()
        else:
            members = []

        return render_template('search_members.html', members=members, form=form)

    return render_template('search_members.html', form=form)

@member_routes.route('/member/<int:member_id>', methods=['GET', 'POST'])
def view_member(member_id):
    member = Member.query.get_or_404(member_id)
    form = MemberForm(obj=member)

    if form.validate_on_submit():
        password = request.form.get("admin_password")
        if password != ADMIN_PASSWORD:
            flash("Incorrect password! Member details not updated.", "danger")
            return redirect(url_for('member.view_member', member_id=member.id))

        member.first_names = form.first_names.data
        member.surname = form.surname.data
        member.id_number = form.id_number.data
        member.gender = form.gender.data
        member.language = form.language.data
        member.mobile_number = form.mobile_number.data
        member.alternative_number = form.alternative_number.data
        member.ward = form.ward.data
        member.region = form.region.data
        member.municipality = form.municipality.data
        member.house_number = form.house_number.data
        member.street_address = form.street_address.data
        member.suburb = form.suburb.data
        member.city = form.city.data
        member.province = form.province.data
        member.postal_code = form.postal_code.data
        member.iec_registered = form.iec_registered.data
        member.pat_no = form.pat_no.data
        member.voting_district = form.voting_district.data

        db.session.commit()

        flash('Member updated successfully!', 'success')
        return redirect(url_for('member.members'))

    if request.method == 'POST' and 'delete' in request.form:
        password = request.form.get("admin_password")
        if password != ADMIN_PASSWORD:
            flash("Incorrect password! Member not deleted.", "danger")
            return redirect(url_for('member.view_member', member_id=member.id))

        db.session.delete(member)
        db.session.commit()
        flash('Member deleted successfully!', 'success')
        return redirect(url_for('member.members'))

    return render_template('view_member.html', member=member, form=form)

# Export Members to Excel
@member_routes.route('/export_members')
def export_members():
    # Query all members from the database
    members = Member.query.all()

    # Prepare data to export
    data = []
    for member in members:
        data.append({
            'First Name': member.first_names,
            'Surname': member.surname,
            'ID Number': member.id_number,
            'PAT No': member.pat_no,
            'House Number': member.house_number,
            'Street Address': member.street_address,
            'Ward': member.ward,
            'Region': member.region,
            'Municipality': member.municipality,
            'City': member.city,
            'Province': member.province,
            'IEC Registered': member.iec_registered,
            'Voting District': member.voting_district
        })

    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(data)

    # Create a response object to return the Excel file
    output = Response(
        df.to_excel(index=False, engine='openpyxl'),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    output.headers['Content-Disposition'] = 'attachment; filename=members.xlsx'
    return output
