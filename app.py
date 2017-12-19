# A simple web server to receive images, transfer style to them, and post them elsewhere.

from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse
import base64, subprocess, pdb

app = Flask(__name__)
api = Api(app)

# / Root response

class HelloMOD(Resource):
  def get(self):
    return {'hello': 'MOD. image style transfer server says hi hello. x'}

api.add_resource(HelloMOD, '/')

# Simple post - test with $ curl http://localhost:5000/image1 -d "data=Base64_Image_Data" -X PUT
# Example curl Base64 $ (echo -n '{"ios_data": "'; openssl base64 < file.png; echo '"}') | curl http://localhost:5000/image1 -d @- -H "Content-Type: application/json" -X PUT

images = {}

def abort_if_image_doesnt_exist(image_id):
  if image_id not in images:
    abort(404, message="Image {} doesn't exist".format(image_id))

class PostImage(Resource):
  def get(self, image_id):
    abort_if_image_doesnt_exist(image_id)
    # parser = reqparse.RequestParser()
    # parser.add_argument('Content-Type', location='headers')
    # args = parser.parse_args()
    # request_type = args['Content-Type']
    # pdb.set_trace()
    image_file_out_path = "out/image{}.png".format(image_id)
    encoded_deep_dream_image_string = ""
    try:
      with open(image_file_out_path, "rb") as image_file:
        encoded_deep_dream_image_string = base64.b64encode(image_file.read()).decode('utf-8')
    except Exception as e:
      print("PROBLEM! {}".format(e))
    
    return {image_id: images[image_id], "{}_output".format(image_id): encoded_deep_dream_image_string}

  def put(self, image_id):
    # Decode Base64 image
    # Handle JSON post from Rails

    # Debugging using pdb
    # pdb.set_trace()
    
    images[image_id] = request.get_json()['ios_data']
    decoded_image_data = base64.decodebytes(images[image_id].encode('utf-8'))

    # Save it to the filesystem
    image_file_path = "in/image{}.png".format(image_id)
    image_file_out_path = "out/image{}.png".format(image_id)
    with open(image_file_path, "wb") as f:
      f.write(decoded_image_data)

    # If ever we need the MIME type
    # image_mime_type = subprocess.check_output(['file', '--mime', '-b', image_file_path]).decode('utf-8')

    # Transfer the image style
    print("Starting to dream...")
    try:
      deep_dream_output = subprocess.check_output(['python', 'evaluate.py', '--checkpoint', 'udlf_fst_checkpoints/scream.ckpt', '--in-path', image_file_path, '--out-path', image_file_out_path]).decode('utf-8')
    except Exception as e:
      deep_dream_output = e
      print("PROBLEM!")
    print(deep_dream_output)
    print("I've finished dreaming...")

    # Load the styalised image
    with open(image_file_out_path, "rb") as image_file:
      encoded_deep_dream_image_string = base64.b64encode(image_file.read()).decode('utf-8')

    # Return Base64 image back
    return {image_id: encoded_deep_dream_image_string}

api.add_resource(PostImage, '/<string:image_id>')

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0')