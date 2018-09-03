source activate project1env

export DATABASE_URL=postgres://ethirpnwmtxbql:f0668a03197f40155cf23c753480d0473a921575935d0724335de2a8fb62b78c@ec2-54-217-235-16.eu-west-1.compute.amazonaws.com:5432/d8mvoljn29kt9b
export FLASK_APP=application.py
export FLASK_DEBUG=1
flask run
