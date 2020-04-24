# maldetect

A web application built using django to detect malicious URL(s) which include phishing/social engineering/malware infected URL(s).


# To run 

```bash

$ cd maldetect
$ echo "export API_KEY='[SECERT]'" > .env
$ echo "export SECRET_KEY='[SECERT]'" > .env
$ source maldetect/bin/activate 
(maldetect) $ source .env
(maldetect) $ python manage.py runserver

```