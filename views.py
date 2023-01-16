from flask.views import MethodView
from flask import jsonify, request
from database import AdsModel, Session



class AdsView(MethodView):
    def get(self,user_id : int):
        with Session() as session:
            ads = session.query(AdsModel).get(user_id)

            return jsonify({
                'id': ads.id,
                'heading': ads.heading,
                'description': ads.description,
                'date_creation': ads.date_creation,
                'owner': ads.owner
            })
    def post(self):
        ads_data = request.json
        with Session() as session:
            new_ads = AdsModel(**ads_data)
            session.add(new_ads)
            session.commit()
            return jsonify({'heading':new_ads.heading,
                            'description': new_ads.description,
                            'date_creation': new_ads.date_creation,
                            'owner': new_ads.owner
                            })

    def patch(self,user_id : int):
        ads_data = request.json
        with Session() as session:
          ads_patch = session.query(AdsModel).get(user_id)
          for field, value in ads_data.items():
              setattr(ads_patch,field, value )
          session.add(ads_patch)
          session.commit()
          return jsonify({'heading': ads_patch.heading,
                          'description': ads_patch.description,
                          'date_creation': ads_patch.date_creation,
                          'owner': ads_patch.owner
                          })

    def delete(self, user_id: int):
        with Session() as session:
          ads_delete = session.query(AdsModel).get(user_id)
          session.delete(ads_delete)
          session.commit()
          return jsonify({'status':'deleted'})
