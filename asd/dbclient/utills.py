def parse_payload(payload):
    return payload['data'],\
        payload['user_id'],\
        payload['datetime'],\
        payload['queue_name']
