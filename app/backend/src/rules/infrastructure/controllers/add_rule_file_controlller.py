from flask import jsonify
from flask.views import MethodView
from injector import inject

from app.backend.src.base.infrastructure.requests.validate_file import validate_file
from app.backend.src.rules.application.command.add_rule_file_handler import AddRuleFileHandler


class AddRuleFileController(MethodView):
    @inject
    def __init__(self, handler: AddRuleFileHandler):
        self.handler = handler

    @validate_file('rules')
    def post(self, rules_file, **kwargs):
        try:
            self.handler.execute(rules_file)
            return jsonify('Archivo guardado'), 201
        except Exception as e:
            print(str(e))
            return "no se han podido guardar los datos", 500

    @staticmethod
    def get():
        return '''
            <!doctype html>
            <title>Upload new File</title>
            <h1>Upload new File</h1>
            <form method=post enctype=multipart/form-data>
              <input type=file name=file>
              <input type=submit value=Upload>
            </form>
            '''
