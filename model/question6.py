from flask_restx import fields

model = {
    'command': fields.String(required=True, description='命令串')
}

MODELS = []
