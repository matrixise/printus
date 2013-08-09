from flask import Blueprint
from flask import current_app
from flask import request
from flask import jsonify
from flask import abort
from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash
from werkzeug.exceptions import NotFound

from printus.web.models import Report
from printus.web.models import User
from printus.web.forms import UserForm
from printus.web.forms import ReportForm
from printus.web.forms import LoginForm
from printus.web.forms import SignupForm
from printus.web.forms import ContactForm

from printus.web.extensions import login_manager

from flask.ext.login import login_required, current_user, login_user, logout_user

bp = Blueprint('general', __name__, template_folder='templates')

@bp.route('/')
@login_required
def index():
	try:
		page = long(request.args.get('page', 1))
	except Exception:
		page = 1

	try:
		pagination = current_user.reports.order_by('created_at desc').paginate(page, 10)
	except NotFound:
		page = 1
		pagination = current_user.reports.order_by('created_at desc').paginate(page, 10)

	return render_template('reports.index.html', pagination=pagination)

@bp.route('/reports/new', methods=['GET', 'POST'])
@login_required
def reports_new():
	form = ReportForm()
	if form.validate_on_submit():
		flash('Report created')
		return redirect(url_for('general.index'))
	return render_template('reports.new.html', form=form)

@bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
	form = UserForm(obj=current_user)

	if form.validate_on_submit():
		form.populate_obj(current_user)
		db.session.add(current_user)
		db.session.commit()

	return render_template('profile.html', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	signupForm = SignupForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
		if not user:
			return render_template("login.html", form=form, signupForm=signupForm)
		else:
			login_user(user)
			return redirect(request.args.get("next") or url_for("general.index"))
	return render_template("login.html", form=form, signupForm=signupForm)

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignupForm()
	if form.validate_on_submit():
		return redirect(request.args.get('next') or url_for('general.index'))
	return render_template("signup.html", form=form)

@bp.route('/logout')
@login_required
def logout():
	logout_user()
	flash('Logged out.')
	return redirect(url_for('general.index'))

@bp.route('/contact_us')
@login_required
def contact_us():
	form = ContactForm()
	if form.validate_on_submit():
		return redirect(url_for('general.index'))
	return render_template('contact_us.html', form=form)

