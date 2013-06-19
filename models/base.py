from sqlalchemy import desc
from sqlalchemy.orm import class_mapper
#local
from databases.database import *
class BaseMixin(object):
    def __init__(self):
        pass
    def serialize(self,model,*args):
        if len(args)==0:args=class_mapper(model.__class__).columns
        columns=[c.key for c in args]
        return dict((c,getattr(model,c)) for c in columns)
    def serialize_all(self,models,*args):
        return [self.serialize(m,*args) for m in models]
    def filter_limit_offset(self,rc,**kewargs):
        if kewargs.has_key('limit') and kewargs.has_key('offset'):
            rc=rc.offset(kewargs['offset']).limit(kewargs['limit'])
        return rc

class UserMixin(BaseMixin):
    def create_user(self,user):
        self.db.add(user)
        self.db.commit()
        return ""
    def get_user_count(self):
		count=self.db.query(User).count()
		return count
    def get_user_list(self,*args,**kwargs):
        rc=self.db.query(User).order_by(desc(User.id))
        rc=self.filter_limit_offset(rc,**kwargs)
        return rc.all()
    def get_user_detial(self):
		rc=self.db.query(User)
		#rc=self.db.query(User.id,User.username,Company.name).join(Company,User.cid==Company.id)
		#rc=self.db.query(User.id,User.username,Company.name).outerjoin(Company,User.cid==Company.id)
		#rc.self.db.query(test)
		return rc.all()

