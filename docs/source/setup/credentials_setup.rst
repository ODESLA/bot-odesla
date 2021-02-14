.. _credentials_setup:

=================
Credentials Setup
=================

Inside the ``conf/base/`` folder you'll need to create a file called ``credentials.yml``. This file will not be tracked
by git and it will contain all the necessary credentials that the bot needs. You should never share this file!

The structure of the file should be the following: ::

    bot_key:
        key_bot: <bot token>

    drive_key:
        type: service_account
        project_id: <project id>
        private_key_id: <private key id>
        private_key: "<private key>"
        client_email: <client email>
        client_id: <client id>
        auth_uri: <auth uri>
        token_uri: <token uri>
        auth_provider_x509_cert_url: <auth provider certificate url>
        client_x509_cert_url: <client certificate url>

