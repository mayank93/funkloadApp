# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL('mysql://root:root@localhost/funkLoad')
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore')
    ## store sessions and tickets there
    session.connect(request, response, db = db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db)
crud, service, plugins = Crud(db), Service(), PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail=auth.settings.mailer
mail.settings.server = 'smtp.gmail.com:587'
mail.settings.sender = '93mayankgupta@gmail.com'
mail.settings.login = '93mayankgupta:mayank123'

## configure auth policy
auth.settings.registration_requires_verification = True
auth.messages.verify_email = 'Click on the link http://10.1.33.107:8000' + URL(r=request,c='default',f='user',args=['verify_email'])+'/%(key)s to verify your email'
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True
auth.messages.reset_password = 'Click on the link http://10.1.33.107:8000' + URL(r=request,c='default',f='user',args=['reset_password']) +     '/%(key)s to change password'

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.rpx_account import use_janrain
use_janrain(auth,filename='private/janrain.key')

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################


db.define_table(
	'TestDetails',
	Field('TestName','string',required=True),
	Field('Description','text',required=True),
	Field('UserEmail','string',required=True),
	Field('MailSent','string',default='false'),
	Field('SanityFlag','string',default='false'),
	Field('StressFlag','string',default='false'),
	Field('FunctionalFlag','string',default='false'),
	Field('Status','string',default='0'),
	Field('Url','string',required=True),
	Field('CycleDuration','string'),
	Field('CycleUser','string'),
	Field('CycleSleepTime','string',default='1'),
	Field('RequestPerUser','string'),
	Field('Sanity','string',default='false'),
	Field('Functional','string',default='0'),
	Field('path','string')
	)

db.define_table(
	'FunctionalTesting',
	Field('TestId',db.TestDetails,required=True),
	Field('Url','string',required=True),
	Field('Status','string',required=True)
	)

## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
