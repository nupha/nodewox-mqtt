Nodewox MQTT Python Client
==========================

A MQTT Client derived from `Eclipse Paho <http://eclipse.org/paho/>`_. nodewox.mqtt.client use module M2Crypto as TLS.

May pass CA certificates, client-side certicicate and private key content as a string to ``tls_set()`` method. You can only pass cafile, certfile, keyfile as filenames with original Paho client.

