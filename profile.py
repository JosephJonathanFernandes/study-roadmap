from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db, User
import os
from werkzeug.utils import secure_filename

profile_bp = Blueprint('profile', __name__)
UPLOAD_FOLDER = 'static/avatars'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

@profile_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    avatar_url = None
    if request.method == 'POST':
        new_password = request.form.get('new_password')
        avatar = request.files.get('avatar')
        if new_password:
            current_user.set_password(new_password)
            db.session.commit()
            flash('Password updated successfully!', 'success')
        if avatar and allowed_file(avatar.filename):
            filename = secure_filename(f"{current_user.id}_" + avatar.filename)
            avatar.save(os.path.join(UPLOAD_FOLDER, filename))
            current_user.avatar = filename
            db.session.commit()
            flash('Profile image updated!', 'success')
        return redirect(url_for('profile.profile'))
    if hasattr(current_user, 'avatar') and current_user.avatar:
        avatar_url = url_for('static', filename=f'avatars/{current_user.avatar}')
    return render_template('profile.html', user=current_user, avatar_url=avatar_url)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
