from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init,pre_save,pre_delete,post_init,post_save,post_delete,pre_migrate,post_migrate
from django.core.signals import request_started,request_finished,got_request_exception
from django.db.backends.signals import connection_created

@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
    print("------------------------------")
    print("Logged-in signal..Run Intro..")
    print("sender:",sender)
    print("Request:",request)
    print("User Password:",user.password)
    print(f'kwargs: {kwargs}')

# user_logged_in.connect(login_success,sender=User)
    
@receiver(user_logged_out,sender=User)
def log_out(sender,request,user,**kwargs):
    print("------------------------------")
    print("Logged-in signal..Run Outro..")
    print("sender:",sender)
    print("Request:",request)
    print(f'kwargs: {kwargs}')
#user_logged_out.connect(log_out,sender=User)
    
@receiver(user_login_failed)
def login_failed(sender,credentials,request,user,**kwargs):
    print("------------------------------")
    print("Login Failed signal..")
    print("credentials:",credentials)
    print("Request:",request)
    print(f'kwargs: {kwargs}')
#user_login_failed.connect(login_failed)


@receiver(pre_save,sender=User)
def at_beginning_save(sender,instance,**kwargs):
    print("------------------------------")
    print("Pre save Signal..")
    print("sender:",sender)
    print("Instance:",instance)
    print(f'kwargs: {kwargs}')
#pre_save.connect(at_beginnig_save,sender=sender)

@receiver(post_save,sender=User)
def at_ending_save(sender,instance,created,**kwargs):
    if created:
        print("------------------------------")
        print("Post save Signal..")
        print("New Record")
        print("sender:",sender)
        print("Instance:",instance)
        print("Created:",created)
        print(f'kwargs: {kwargs}')
    else:
        print("------------------------------")
        print("Post save Signal..")
        print("Update")
        print("New Record")
        print("sender:",sender)
        print("Instance:",instance)
        print("Created:",created)
        print(f'kwargs: {kwargs}')

#pre_save.connect(at_beginnig_save,sender=sender)

@receiver (pre_delete,sender=User)
def at_ending_delete(sender,instance,**kwargs):
    print("------------------------------")
    print("Pre delete Signal....")
    print("sender:",sender)
    print("Instance:",instance)
    print(f'kwargs: {kwargs}')
#pre_delete.connect(at_ending_delete,sender=User)


@receiver (post_delete,sender=User)
def at_ending_delete(sender,instance,**kwargs):
    print("------------------------------")
    print("Post Ending Delete....")
    print("sender:",sender)
    print("Instance:",instance)
    print(f'kwargs: {kwargs}')
#at_delete.connect(at_ending_delete,sender=User)
    

@receiver (pre_init,sender=User)
def at_beginnig_init(sender,*args,**kwargs):
    print("------------------------------")
    print("Pre Init Signals ...")
    print("sender:",sender)
    print(f'Args:{args}')
    print(f'kwargs: {kwargs}')
#pre_init.connect(at_beginnig_init,sender=User)
    

@receiver (post_init,sender=User)
def at_ending_init(sender,*args,**kwargs):
    print("------------------------------")
    print("Post Init Signals ...")
    print("sender:",sender)
    print(f'Args:{args}')
    print(f'kwargs: {kwargs}')
#post_init.connect(at_ending_init,sender=User)
    
@receiver(request_started)
def at_beginnig_request(sender,environ,**kwargs):
    print("--------------")
    print("At Beginning Request....")
    print('Sender:',sender)
    print("Environ:",environ)
    print(f'kwargs:{kwargs}')
#request_started.connect(at_beginning_request)
    

@receiver(request_finished)
def at_ending_request(sender,**kwargs):
    print("--------------")
    print("At Ending Request....")
    print('Sender:',sender)
    print(f'kwargs:{kwargs}')
#request_finished.connect(at_ending_request_request)
    

@receiver(got_request_exception)
def at_req_exception(sender,request,**kwargs):
    print("--------------")
    print("At Request Exception....")
    print('Sender:',sender)
    print('Request:',request)
    print(f'kwargs:{kwargs}')
#got_request_exception.connect(at_req_exception)
    

@receiver(pre_migrate)
def before_install_app(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print("--------------------")
    print("before_install_app")
    print("sender:",sender)
    print("App_confing:", app_config)
    print("Verbosity:",verbosity)
    print("Using:",using)
    print("Plan:",plan)
    print("App:",apps)
    print(f'kwargs:,{kwargs}')
# pre_migrate.connect(before_install_app)
    
@receiver(post_migrate)
def at_end_migrate_flush(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print("--------------------")
    print("at_end_migrate_flush")
    print("sender:",sender)
    print("App_confing:", app_config)
    print("Verbosity:",verbosity)
    print("Using:",using)
    print("Plan:",plan)
    print("App:",apps)
    print(f'kwargs:,{kwargs}')
# post_migrate.connect(at_end_migrate_flush)

@receiver(connection_created)
def conn_db(sender,connection,**kwargs):
    print("--------")
    print("Initial connection to the database....")
    print("sender:",sender)
    print("Connection:",connection)
    print(f'kwargs:,{kwargs}')
#connection_created.connect(conn_db)