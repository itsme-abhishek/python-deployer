import base64
import os
import sys

from Crypto.Cipher import AES


def main():
    # Because kubernetes expects the values in secrets to be base64 encoded
    #b64_encodedtext = base64.b64encode(sys.argv[1])
    b64_encodedtext = str(sys.argv[1])

    key = os.environ["EGOV_SECRET_PASSCODE"]
    encryptor = AES.new(key, AES.MODE_ECB)
    print base64.b64encode(encryptor.encrypt(b64_encodedtext.rjust(16000)))


if __name__ == "__main__":
    main()
