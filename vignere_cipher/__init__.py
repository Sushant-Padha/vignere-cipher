"""
encrypt and decipher messages with vignere cipher

inspired by the movie Imitation Game, 2014 (no, this is not the Enigma cipher)
"""

import argparse

alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]


def normalize(s: str):
    '''Remove non-alphabetic characters

    Args:
        s (str): string to normalize

    Returns:
        str: new string with only alphabetic characters
    '''
    r = ""
    for c in s:
        if c not in alphabet:
            continue
        r += c
    return r


def get_key(text: str, key: str):
    '''Return key with length same as text

    Args:
        text (str): text to expand key for
        key (str): original key

    Returns:
        str: expanded key
    '''
    length = len(text)
    key_len = len(key)
    # repeat
    if key_len < length:
        key *= (length // key_len) + 1
    # slice
    return key[:length]


def encrypt(plaintext: str, key: str):
    encrypted = ""
    plaintext = plaintext.lower()
    for i in range(len(plaintext)):
        t = plaintext[i]
        k = key[i]
        encrypted += alphabet[
            (alphabet.index(t) + alphabet.index(k)) % 26
        ]
    return encrypted


def decrypt(encrypted: str, key: str):
    plaintext = ""
    for i in range(len(encrypted)):
        e = encrypted[i]
        k = key[i]
        plaintext += alphabet[
            (alphabet.index(e) - alphabet.index(k)) % 26
        ]
    return plaintext


def main():
    namespace = parse_args()
    parsed_vars = vars(namespace)
    text = parsed_vars['text']
    key = parsed_vars['key']
    e = parsed_vars['e']
    d = parsed_vars['d']

    text = normalize(text).lower()
    key = get_key(text, normalize(key).lower())

    if e:
        r = encrypt(text, key)
    else:
        r = decrypt(text, key)
    print(r)


def parse_args():
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog="\x1b[3m“Sometimes it’s the people no one " +
        "imagines anything of who do the things " +
        "that no one can imagine.”\x1b[0m (Imitation Game, 2014)"
    )
    parser.add_argument('text', action='store',
                        help="text message to decrypt or encrypt " +
                        "(all non-alphabetic characters will be removed)")
    parser.add_argument('-k', action='store', dest='key', required=True,
                        help="key to use to en/decrypt text " +
                        "(all non-alphabetic characters will be removed)")
    action = parser.add_mutually_exclusive_group()
    action.add_argument('-e', action='store_true', dest='e',
                        help="encrypt text using key")
    action.add_argument('-d', action='store_true', dest='d',
                        help="decrypt text using key")
    return parser.parse_args()


if __name__ == '__main__':
    main()
