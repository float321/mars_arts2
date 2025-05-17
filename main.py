from flask import Flask, render_template, request, redirect, url_for
import os


app = Flask(__name__)
filepathh = 'static/images/uploaded'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(url_for('index'))
        file = request.files['file']
        if file.filename == '':
            return redirect(url_for('index'))
        if file:
            filename = file.filename
            file.save(os.path.join(filepathh, filename))
            return redirect(url_for('index'))

    images = [i for i in os.listdir(filepathh)]
    return render_template('index.html', images=images)


if __name__ == '__main__':
    os.makedirs(filepathh, exist_ok=True)
    app.run(host='127.0.0.1', port=8080)
