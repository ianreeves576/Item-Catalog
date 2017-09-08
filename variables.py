from os import environ

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

google_web = dict(
    client_id=environ.get("google_client_id", "164811221943-tj07cpbse6ch8g3p57lsj81bmgc8sous"),
    project_id=environ.get("google_project_id", "testproject-177317"),
    auth_uri=environ.get("google_auth_uri", "https://accounts.google.com/o/oauth2/auth"),
    token_uri=environ.get("google_token_uri", "https://accounts.google.com/o/oauth2/token"),
    auth_provider_x509_cert_url=environ.get("google_x509", "https://www.googleapis.com/oauth2/v1/certs"),
    client_secret=environ.get("google_client_secret", "pscYUIwzeKJB1bysOX1RK-dg"),
    javascript_origins=[
        "http://localhost:5000"
    ],
    scope='',
    redirect_uris=[
        "https://localhost:5000/callback",
        "http://localhost:5000/callback"
    ]
)

facebook_web = dict(
    app_id=environ.get('facebook_app_id', '339753266465973'),
    app_secret=environ.get('facebook_app_secret', 'c6ba7cc2b738ed33dabd6937e71d027e')
)

main_app = dict(
    secret_key=environ.get('app_secret_key', 'super secret key'),
    debug=environ.get('debug', True)
)
