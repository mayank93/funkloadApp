# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations
import os
#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################


#-----------------------Error Page-----------------------------------
#if java script dissabled
def error():
	        return dict()

#-----------------------Home Page------------------------------------
@auth.requires_login()
def index():
    	session.email=auth.user.email
    	print session.email
    	return dict()


@auth.requires_login()
def test():
	tid=request.args[0]
	print tid
    	session.email=auth.user.email
    	print session.email
	details=db(db.TestDetails.id == tid).select()[0]
	print details
	functionalDetails=db(db.FunctionalTesting.TestId == tid).select()
	stressDetails=str(tid)+'/index.html'
    	return dict(details=details,stressDetails=stressDetails,functionalDetails=functionalDetails)

@auth.requires_login()
def testDetails():
    	session.email=auth.user.email
    	print session.email
	details=db(db.TestDetails.UserEmail == session.email).select() 
	print details
	return dict(details=details)

@auth.requires_login()
def addTest():
    	session.email=auth.user.email
    	print session.email
	if request.vars.Submit=='Submit' :
		TestName=request.vars.TestName
		UrlName=request.vars.UrlName
		CycleUser=request.vars.CycleUser
		CycleDuration=request.vars.CycleDuration
		RequestPerUser=request.vars.RequestPerUser
		Description=request.vars.Description
		SanityFlag=request.vars.Sanity
		StressFlag=request.vars.Stress
		FunctionalFlag=request.vars.Functional
		if not Description:
			Description=UrlName
		if not SanityFlag=='true':
		   SanityFlag='false'
		if not StressFlag=='true':
		   StressFlag='false'
		if not FunctionalFlag=='true':
		   FunctionalFlag='false'
		print TestName
		print UrlName
		print CycleUser
		print CycleDuration
		print RequestPerUser
		print SanityFlag
#		m=''
#		mail.send(auth.user.email,subject=' Received your Updated Response"',message=m)
		tid=db.TestDetails.insert(TestName=TestName,UserEmail=session.email,Url=UrlName,CycleDuration=CycleDuration,CycleUser=CycleUser,RequestPerUser=RequestPerUser,Description=Description,SanityFlag=SanityFlag,StressFlag=StressFlag,FunctionalFlag=FunctionalFlag)
		db.commit()
#		a=os.getcwd()+'/applications/FunkLoad/static/'+str(tid)
#		os.mkdir(a)
		redirect(URL(r=request, f='testDetails'))
	return dict()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
