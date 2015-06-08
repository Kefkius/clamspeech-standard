"""Example of ClamSpeech serialization."""

### Some needed functions are imported from scallop, a CLAM-compatible 
### electrum fork: https://github.com/Kefkius/scallop

# var_int returns a hex-encoded string according to rules specified
# at https://en.bitcoin.it/wiki/Protocol_specification#Variable_length_integer
from scallop.bitcoin import var_int

# int_to_hex takes an int and a length argument, and returns a little-endian
# hex-encoded string of the int in the given length.
from scallop.bitcoin import int_to_hex

current_clamspeech_version = 1


def serialize_application_state(state):
    """Returns the serialized application state that one would see in a raw transaction.

    Args:
        state (tuple): A 2-tuple of (application_id, payload).

    Returns:
        A hex-encoded string.

    """

    app_id = state[0]
    payload = state[1]

    s = ''
    s += int_to_hex(current_clamspeech_version, 2)

    s += var_int(len(app_id))
    s += app_id.encode('hex')

    s += var_int(len(payload))
    s += payload.encode('hex')

    return s

def serialize_regular_clamspeech(speech):
    """Returns the serialized clamspeech that one would see in a raw transaction.

    Args:
        speech (str): ClamSpeech.

    Returns:
        A hex-encoded string.

    """

    s = ''
    # append version 0 for regular clamspeech
    s += int_to_hex(0, 2)

    s += var_int(len(speech))
    s += speech.encode('hex')
    return s

if __name__ == '__main__':
    app_id = 'Test App'
    payload = 'There are 5 users online.'
    state = (app_id, payload)
    s = serialize_application_state(state)

    regular_speech = '777'
    c = serialize_regular_clamspeech(regular_speech)

    print('--- Serialize Application State ---')
    print('Application ID: {}'.format(app_id))
    print('Payload       : {}'.format(payload))
    print('In raw transactions, the ClamSpeech will appear as follows:')
    print(s)

    print('\n--- Serialize Regular ClamSpeech ---')
    print('ClamSpeech: {}'.format(regular_speech))
    print('In raw transactions, the ClamSpeech will appear as follows:')
    print(c)
