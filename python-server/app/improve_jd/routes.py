from flask_restx import Resource, Api, fields
from app.improve_jd.improve_jd import ImproveJobDescription
import json

api = Api()
improveJdNS = api.namespace('improveJobDescription', description='Improve Job Description using LLM Model')

job_desc = improveJdNS.parser()
job_desc.add_argument('requestid', type=str, required=True, help='a request id from application')
job_desc.add_argument('job_description', type=str, required=True, help='job description to be improved')

@improveJdNS.route('/')
class ReadResumeNS(Resource):

    @improveJdNS.expect(job_desc)
    def post(self):

        args = job_desc.parse_args()
        requestid = args['requestid']
        job_description = args['job_description']

        improveJobDescription = ImproveJobDescription()
        generated_response = improveJobDescription.improveJobDescription(job_description, requestid)
        print(generated_response)
        return json.loads(improveJobDescription.clean_response(generated_response))