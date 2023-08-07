from flask_restx import Resource, Api, fields
from app.read_resume.read_resume import ReadResume
from werkzeug.datastructures import FileStorage

api = Api()
readResumeNS = api.namespace('readResume', description='Read Resume from PDF, text and word files')

file_parser = readResumeNS.parser()
file_parser.add_argument('file', type=FileStorage, location='files', required=True, help='The file to be processed (pdf, docx, or txt)')

@readResumeNS.route('/')
class ReadResumeNS(Resource):

    @readResumeNS.expect(file_parser)
    def post(self):

        args = file_parser.parse_args()
        file = args['file']

        readResume = ReadResume(file)
        generated_response = readResume.extracted_text
        return generated_response