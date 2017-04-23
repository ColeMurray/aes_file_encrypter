Utility Module for Encrypting with AES
--------------------------------------

Encrypt:
^^^^^^
To encrypt files::

    aes-encrypter \
    -–file plaintext_file  \
    -–dest encrypted_file \
    -–encrypt \
    -–b64key ‘b64-encoded 32 byte key’ \


*Note: If no key is provided, a key will be generated and printed to console.*


Decrypt:
^^^^^^^^
Decrypt Files::

    aes-encrypter \
    -–file encrypted_file \
    --dest decrypted_readme \
    -–decrypt \
    -–b64key ‘b64-encoded 32 byte key’
