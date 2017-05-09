# Template for Django Wagtail

AWS Tutorial
https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/
https://github.com/jpadilla/django-project-template

```bash
$ django-admin.py startproject --template=https://github.com/linuxluigi/template-django-wagtail/archive/master.zip helloworld
```
change helloworld to your project name

todo: add placeholder
* .idea
* settings
* project name

```bash
virtualenv venv
pip install -r requirements.txt 
```

# AWS Settings

todo:
* create a aws user
* add sns
* add RDS
* add cloudflare support

## S3 - CORS

Example Cors

```xml
<CORSConfiguration>
    <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <MaxAgeSeconds>3000</MaxAgeSeconds>
        <AllowedHeader>Authorization</AllowedHeader>
    </CORSRule>
</CORSConfiguration>
```


# Deployment

## Heroku

todo: update settings for heroku
https://github.com/heroku/heroku-django-template/blob/master/project_name/settings.py

## Using Python 2.7?

Just update `runtime.txt` to `python-2.7.13` (no trailing spaces or newlines!).

## Zappa - AWS Lamda 