# Template for Django Wagtail

AWS Tutorial
https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/

```bash
$ django-admin.py startproject --template=https://github.com/linuxluigi/template-django-wagtail/archive/master.zip helloworld
```
change helloworld to your project name


# Local development

Setting up local venv for Python 2

```bash
virtualenv venv
```

And for Python 3

```bash
virtualenv -p python3 venv
```

Install requirements:
```bash
pip install -r requirements.txt 
```


# AWS Settings

todo:
* create a aws user

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
add heroku tool to upload env
https://github.com/heroku/heroku-django-template/blob/master/project_name/settings.py

## Using Python 2.7?

Just update `runtime.txt` to `python-2.7.13` (no trailing spaces or newlines!).

## Zappa - AWS Lamda 

https://github.com/Miserlou/Zappa

1. Create a AWS User with a VPC -> http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_IAM.html
2. generate zappa json
3. deploy your application
4. upload your env to lambda -> http://docs.aws.amazon.com/lambda/latest/dg/env_variables.html
5. Update
6. Use a coustom Domain