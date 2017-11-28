# A simple web server to receive images, transfer style to them, and post them elsewhere.

from flask import Flask, request
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)

# / Root response

class HelloMOD(Resource):
  def get(self):
    return {'hello': 'MOD. says hi hello. x'}

api.add_resource(HelloMOD, '/')

# Simple post - test with $ curl http://localhost:5000/image1 -d "data=Base64_Image_Data" -X PUT

images = {}

def abort_if_image_doesnt_exist(image_id):
  if image_id not in images:
    abort(404, message="Image {} doesn't exist".format(image_id))

class PostImage(Resource):
  def get(self, image_id):
    abort_if_image_doesnt_exist(image_id)
    return {image_id: images[image_id]}

  def put(self, image_id):
    # TODO: handle Base64 image here, and run it through deep dream
    images[image_id] = request.form['data']
    # TODO: return Base64 image back
    return {image_id: images[image_id]}

api.add_resource(PostImage, '/<string:image_id>')

if __name__ == '__main__':
  app.run(debug=True)