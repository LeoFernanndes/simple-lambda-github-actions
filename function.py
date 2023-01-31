import datetime

def lambda_handler(event, context):
    return {'response': f'resposta {datetime.datetime.now()}'}