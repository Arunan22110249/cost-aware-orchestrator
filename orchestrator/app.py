# Simple Flask front-end to trigger orchestration actions (demo)
from flask import Flask, jsonify, request
from terraform_driver import write_tfvars, terraform_apply
from predictor.prophet_predict import run_predict
from optimizer import pick_instances
import os

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # In practice you'd fetch metrics from Prometheus. Here we run a saved predictor.
    forecast = run_predict()
    return jsonify({'forecast_rows': len(forecast)})

@app.route('/apply', methods=['POST'])
def apply():
    data = request.json or {}
    tfvars = data.get('tfvars', {'desired_capacity': 2, 'instance_type': 't3.small'})
    write_tfvars('/workspace/terraform/aws/terraform.tfvars.json', tfvars)
    # CAUTION: terraform_apply() will attempt to run terraform in the container's workspace
    # For safety, this demo returns plan content instead of applying.
    return jsonify({'status': 'tfvars written', 'tfvars': tfvars})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
