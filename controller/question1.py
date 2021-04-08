from flask_restx import Namespace, Resource, fields
from model.question1 import triangle_model as q1_model
from model.question1 import calender_model as q2_model
from service.question1 import question1 as question1_service

ns = Namespace('question1', description='三角形/万年历问题')
q1_model = ns.model('Triangle', model=q1_model)
q2_model = ns.model('Calender', model=q2_model)


@ns.route('/triangle/<method_type>')
@ns.param('method_type', 'boundary | equivalence')
@ns.response(404, 'Method not found')
class Triangle(Resource):
    @ns.doc('Triangle Problem')
    def get(self, method_type):
        """
        三角形问题
        """
        return question1_service.triangle(method_type)


@ns.route('/triangle/<method_type>/<code_version>')
@ns.param('method_type', 'boundary | equivalence')
@ns.param('code_version', 'v1 | v2')
@ns.response(404, 'Method not found')
class Triangle(Resource):
    @ns.doc('Triangle Problem')
    def get(self, method_type, code_version):
        """
        版本-三角形问题
        """
        return question1_service.triangle(method_type, code_version)


@ns.route('/calendar/<method_type>')
@ns.param('method_type',
           'boundary | equivalence-weak-general ｜ equivalence-strong-general ｜ equivalence-weak-robust ｜ equivalence-strong-robust')
@ns.response(404, 'Method not found')
class Calendar(Resource):
    @ns.doc('Calendar Problem')
    def get(self, method_type):
        """
        万年历问题
        """
        return question1_service.calendar(method_type)


@ns.route('/triangle/')
class TriangleBasic(Resource):
    @ns.doc('Triangle Problem Basic Method')
    @ns.expect(q1_model)
    def post(self):
        """
        三角形问题的基础实现
        """
        return question1_service.triangle_method_test(ns.payload)


@ns.route('/triangle/<code_version>')
@ns.param('code_version', 'v1 | v2')
class TriangleBasic(Resource):
    @ns.doc('Triangle Problem Basic Method')
    @ns.expect(q1_model)
    def post(self, code_version):
        """
        版本-三角形问题的基础实现
        """
        return question1_service.triangle_method_test(ns.payload, code_version)


@ns.route('/calendar/')
class CalenderBasic(Resource):
    @ns.doc('Calender Problem Basic Method')
    @ns.expect(q2_model)
    def post(self):
        """
        万年历问题的基础实现
        """
        return question1_service.calendar_method_test(ns.payload)
