from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from project.models.user import User, Role
from project.models import db, Files
from flask import redirect, url_for, request, flash, abort
from flask_user import current_user
from flask_admin.menu import MenuLink
from project.models import Ticket, Emotion, Text, ActivityStreak


class AdminModelView(ModelView):
    column_exclude_list = ['password', ]

    def is_accessible(self):
        return current_user.has_role("Admin")

    def inaccessible_callback(self, name, **kwargs):
        return abort(403)


class HomeAdminView(AdminIndexView):
    column_exclude_list = ['password', ]

    def is_accessible(self):
        return current_user.has_role('Admin')

    def inaccessible_callback(self, name, **kwargs):
        return abort(403)


admin = Admin(name='Panel', template_mode='bootstrap4', url='/', index_view=HomeAdminView(name='home'))

admin.add_view(AdminModelView(User, db.session, category="User Managements"))
admin.add_view(AdminModelView(Role, db.session, name="User Roles", category="User Managements"))
admin.add_view(AdminModelView(Emotion, db.session))
admin.add_view(AdminModelView(Files, db.session))
admin.add_view(AdminModelView(Text, db.session))
admin.add_view(AdminModelView(Ticket, db.session))
admin.add_view(AdminModelView(ActivityStreak, db.session))


admin.add_link(MenuLink(name="Logout", endpoint='user.logout'))
