import binascii
from scallop.bitcoin import int_to_hex, var_int

current_clamspeech_version = 1

hex_to_bin = lambda s: binascii.a2b_hex(s)

def serialize(state):
    app_id = state[0]
    payload = state[1]

    s = []
    s.append(int_to_hex(current_clamspeech_version, 2))
    
    s.append(var_int( len(app_id)/2 ))
    s.append(app_id)

    s.append(var_int( len(payload)/2 ))
    s.append(payload)

    return ''.join(s)

speech_examples = [
    {'Just-Dice (Dice Game) - Recording date, number of rolls, and house profit': [
        ('JSON object',               'Just-Dice', '{"date": "2015-06-11 13:28:32", "rolls": 368018123, "profit": 100544.70172816}'),
        ('string with delimiter',     'Just-Dice', '2015-06-11 13:28:32 368018123 100544.70172816'),
        ('serialized hex; unix time',    'Just-Dice', '5579c5400d1c2015ef82cb00000924fd1f8090'),
        ]
    },
    {'Encompass (Lite Wallet) - Recording release tag and commit': [
        ('JSON object',             'Encompass', '{"tag": "v0.5.0", "commit":"110a4dee78e30a87a7212f26374c3991e887d040"}'),
        ('serialized hex',          'Encompass', '000500110a4dee78e30a87a7212f26374c3991e887d040')
        ]
    }

]

if __name__ == '__main__':
    print("==== Lengths of application state clamspeech in various formats ====\n")
    print("format of below data:\n<Use Case>\n<format>:                     <app_id:payload>\n  <clamspeech length>\n\n")
    for d in speech_examples:
        name = d.keys()[0]
        print('\n--- {} ---'.format(name))
        for format_, app_id, payload in d.values()[0]:
            # convert to hex string if not already hex
            try:
                i = int(app_id, 16)
                ser_app_id = app_id
            except ValueError:
                ser_app_id = app_id.encode('hex')
            try:
                i = int(payload, 16)
                ser_payload = payload
            except ValueError:
                ser_payload = payload.encode('hex')
    
            s = serialize((ser_app_id, ser_payload))
            print("{:30} {}\n  {} bytes".format(''.join([format_,':']), ':'.join([app_id, payload]), len(s.decode('hex'))))
