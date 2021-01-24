from flask import Flask, render_template, send_from_directory, jsonify, request
import math

DEBUG = True

app = Flask(__name__, static_folder='client/dist/',
            template_folder='client/dist/')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<path:filename>')
def send_file(filename):
    return send_from_directory(app.static_folder, filename)


@app.route('/upload', methods=['POST'])
def upload():
    file_content = request.get_json()
    column = file_content['column']
    lines = file_content['fileContent'].split('\n')
    table = list(map(lambda line: line.split('\t'), lines))

    bl = parser(column, table)

    return jsonify({
        'status': 0 if len(set(bl)) == 1 and bl[0] == 0 else 1,
        'bl': bl
    })


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


def parser(column, table):
    headers = table[:1]
    data = table[1:]
    total = len(data)
    count = [0] * 10

    for i in range(total):
        try:
            num = int(data[i][column])

            if len(data[i]) >= column:
                count[int(data[i][column][0])] += 1
        except:
            continue

    # count = list(map(lambda p: math.ceil((p / total) * 100), count))
    count = list(map(lambda p: round((p / total) * 100, 1), count))

    return count[1:]
