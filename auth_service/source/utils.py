import os
from datetime import datetime
from config.extentions import MEDIA_ROOT
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_file(file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename) 
        file_name, file_ext = os.path.splitext(filename)
        unique_filename = file_name + '_' + datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f') + file_ext
        file_path = os.path.join(MEDIA_ROOT, unique_filename) 
        file.save(file_path)
        return filename
    else:
        return False
