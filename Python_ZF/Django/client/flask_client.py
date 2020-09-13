from flask import Flask, send_file

app = Flask(__name__)


@app.route('/index')
def index():
    return send_file('templates/index.html')


@app.route('/login')
def login():
    return send_file('templates/login.html')


@app.route('/register')
def register():
    return send_file('templates/register.html')


@app.route('/<username>/info')
def info(username):
    # 个人信息
    return send_file('templates/about.html')


@app.route('/<username>/change_info')
def change_info(username):
    # 修改个人信息
    return send_file('templates/change_info.html')


@app.route('/<username>/topic/release')
def topic_release(username):
    # 发表 blog
    return send_file('templates/release.html')


@app.route('/<username>/topics')
def topic_release(username):
    # 个人 blog 列表
    return send_file('templates/list.html')


@app.route('/<username>/topics/detail/<t_id>')
def topic_detail(username, t_id):
    # blog 内容详情
    return send_file('templates/detail.html')


if __name__ == '__main__':
    app.run(debug=True)
