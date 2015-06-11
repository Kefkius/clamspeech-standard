import binascii
from scallop.bitcoin import int_to_hex, var_int

current_clamspeech_version = 1

class State(object):

    def __init__(self, app_id, payload):
        """app_id and payload can be a string or a list of strings.

        A list of strings is appropriate when some parts of the data
        are already hex-encoded.
        """
        self.app_id = app_id
        self.payload = payload

    def get_hex(self):
        """Get the hex-encoded app_id and payload."""
        app_id = None
        payload = None

        if isinstance(self.app_id, str):
            try:
                i = int(self.app_id, 16)
                app_id = self.app_id
            except ValueError:
                app_id = self.app_id.encode('hex')
        elif isinstance(self.app_id, list):
            app_id = list(self.app_id)
            for i, part in enumerate(app_id):
                try:
                    i = int(part, 16)
                except ValueError:
                    app_id[i] = app_id[i].encode('hex')
            app_id = ''.join(app_id)

        if isinstance(self.payload, str):
            try:
                i = int(self.payload, 16)
                payload = self.payload
            except ValueError:
                payload = self.payload.encode('hex')
        elif isinstance(self.payload, list):
            payload = list(self.payload)
            for i, part in enumerate(payload):
                try:
                    i = int(part, 16)
                except ValueError:
                    payload[i] = payload[i].encode('hex')
            payload = ''.join(payload)

        return (app_id, payload)

    def get_string(self):
        """Get the app_id and payload as strings if they are lists."""
        app_id = self.app_id
        payload = self.payload
        if isinstance(app_id, list):
            app_id = ''.join(list(app_id))
        if isinstance(payload, list):
            payload = ''.join(list(payload))

        return (app_id, payload)

    def serialize(self):
        """Get the state serialized as ClamSpeech."""
        app_id, payload = self.get_hex()
        s = []
        s.append(int_to_hex(current_clamspeech_version, 2))

        s.append(var_int( len(app_id)/2 ))
        s.append(app_id)

        s.append(var_int( len(payload)/2 ))
        s.append(payload)

        return ''.join(s)

speech_examples = [
    {'Just-Dice (Dice Game) - Recording date, number of rolls, and house profit': [
        ('JSON object',               State('Just-Dice', '{"date": "2015-06-11 13:28:32", "rolls": 368018123, "profit": 100544.70172816}')),
        ('string with delimiter',     State('Just-Dice', '2015-06-11 13:28:32 368018123 100544.70172816')),
        ('serialized hex; unix time', State('Just-Dice', '5579c5400d1c2015ef82cb00000924fd1f8090')),
        ]
    },
    {'Encompass (Lite Wallet) - Recording release tag and commit': [
        ('JSON object',             State('Encompass', '{"tag": "v0.5.0", "commit":"110a4dee78e30a87a7212f26374c3991e887d040"}')),
        ('string with delimiter',   State('Encompass', ['v0.5.0 ', '000500110a4dee78e30a87a7212f26374c3991e887d040'])),
        ('serialized hex',          State('Encompass', '000500110a4dee78e30a87a7212f26374c3991e887d040'))
        ]
    }

]

if __name__ == '__main__':
    print("==== Lengths of application state clamspeech in various formats ====\n")
    print("format of below data:\n<Use Case>\n<format>:                     <app_id:payload>\n  <clamspeech length>\n\n")
    for d in speech_examples:
        name = d.keys()[0]
        print('\n--- {} ---'.format(name))
        for format_, state in d.values()[0]:
    
            s = state.serialize()
            str_app_id, str_payload = state.get_string()
            print("{:30} {}\n  {} bytes".format(''.join([format_,':']), ':'.join([str_app_id, str_payload]), len(s.decode('hex'))))
