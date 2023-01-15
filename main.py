from flask import Flask
from flask import jsonify
from views import AdsView



app = Flask('app')
def hello_world():
 return jsonify({'hello':'world'})

app.add_url_rule('/a/<int:user_id>', view_func=AdsView.as_view('ads'), methods=['GET','PATCH'])
app.add_url_rule('/a/create/', view_func=AdsView.as_view('ads_create'), methods=['POST'])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)