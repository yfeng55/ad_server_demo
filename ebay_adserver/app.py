import os
import uuid
import time
from ad import Ad
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

### setup/settings ###

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
api = Api(app)

### In-Memory Stores ###

store = {}

### Endpoints ###

# /show_store
class ShowStore(Resource):
    def get(self):
        output = {}
        for adid in store:
            output[adid] = store[adid].toJson()
        return output
        

# /get_ad/<ad_id>
class GetAd(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        try:
            parser.add_argument('ad_id', type=int)
            args = parser.parse_args()
            return store[args['ad_id']].toJson()    
        except:
            return {"args": args, "status": "error"}

# /create_ad/
# <width>, <height>, <creative>
class CreateAd(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        try:
            parser.add_argument('width', type=int)
            parser.add_argument('height', type=int)
            parser.add_argument('creative', type=str)
            args = parser.parse_args()
            adid = str(uuid.uuid4())
            newad = Ad(adid, args['width'], args['height'], args['creative'])
            store[adid] = newad
            return {"args": args, "status": "success"}
        except:
            return {"args": args, "status": "error"}

# /delete_ad
# <ad_id>
class DeleteAd(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('ad_id', type=int)
            args = parser.parse_args()
            del store[args[ad_id]]
            return {"args": args, "status": "success"}
        except:
            return {"args": args, "status": "error"}

# /register_impression
# <ad_id>
class RegisterImpression(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('ad_id', type=int)
            args = parser.parse_args()
            store[args['ad_id']].incImpressions()
            return {"args": args, "status": "success"}
        except:
            return {"args": args, "status": "error"}

# /register_click
# <ad_id>
class RegisterClick(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('ad_id', type=int)
            args = parser.parse_args()
            store[args['ad_id']].incClicks()
            return {"args": args, "status": "success"}
        except:
            return {"args": args, "status": "error"}


# /serve_ad
'''
strategy:
    - for each ad, we have the # of clicks and impressions
    - we'll select an ad based on 'popularity' which we'll define as:
         ((5.0 * num_clicks) + (1.0 * num_impressions)) / (time since creation)

strategy2:
    - select based on click rate (num_clicks) / (num_impressions)
    - ties go to newer ads

strategy3:
    - try to a get a "fair" distribution of ad serves
    - select the ad with the lowest number of serves; ties go to older ads
'''
def getPopularity():
    currtime = time.time()
    timediff = (curr_time - ad.getCreateTime())
    return (5.0 * ad.getClicks() + 1.0 * ad.getImpressions()) / timediff

class ServeAd(Resource):
    def get(self):
        try:
            ads = sorted(store.values(), key=lambda x: getPopularity) 
            return ads[0].toJson()
        except Exception as e:
            print e
            return {"status": "error"}


api.add_resource(ShowStore, '/show_store', endpoint='show_store')
api.add_resource(GetAd, '/get_ad', endpoint='get_ad')
api.add_resource(CreateAd, '/create_ad', endpoint='create_ad')
api.add_resource(DeleteAd, '/delete_ad', endpoint='delete_ad')
api.add_resource(RegisterImpression, '/inc_impressions', endpoint='inc_impressions')
api.add_resource(RegisterClick, '/inc_clicks', endpoint='inc_clicks')
api.add_resource(ServeAd, '/serve_ad', endpoint='serve_ad')


if __name__ == '__main__':
    app.run(debug=True)

