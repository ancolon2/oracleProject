# =============================================================================
# Created By  : Andrew Colon
# Created Date: Mon October 1st 2019
# =============================================================================

import dns.resolver
from dns.resolver import NXDOMAIN
from flask import Flask, render_template, request
import json

app = Flask(__name__ , template_folder="templates")  # '__main__'
app.secret_key = "andrew"

#Route to homepage - http://127.0.0.1:5000/
@app.route('/')
def home_template():
    return render_template('home.html')

@app.route('/api/domain', methods=['POST'])
def post_domain(domain=None):
    domain = request.form['domain']
    try:
        mxquery = dns.resolver.query(domain, 'MX')
    except NXDOMAIN:
        return render_template('error.html', domain=domain)
    mxrecords = {str(data): str(data.exchange) for data in mxquery}
    json_data = json.dumps(mxrecords, sort_keys=True)
    return render_template('domain.html', domain=domain, mxrecords=json_data), 200

@app.route('/api/domain/<string:domain>', methods=['GET'])
def get_domain(domain=None):
    if domain is not None:
        try:
            mxquery = dns.resolver.query(domain, 'MX')
        except NXDOMAIN:
            return render_template('error.html', domain=domain), 500
    else:
        return render_template('error.html', domain=domain), 500
    mxrecords = {str(data): str(data.exchange) for data in mxquery}
    json_data = json.dumps(mxrecords, sort_keys=True)
    return render_template('domain.html', domain=domain, mxrecords=json_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0")