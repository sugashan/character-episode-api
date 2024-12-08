from marshmallow import Schema, fields


class CharacterResponseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    gender = fields.Str(required=True)
    origin = fields.Str(required=True)
    description = fields.Str()
    image = fields.Str()
    species = fields.Str()
    status = fields.Str()
    episodes = fields.List(fields.Str())


class GetCharactersQueryArgsSchema(Schema):
    page = fields.Int()


class LoginRequestSchema(Schema):
    username = fields.Str(required=True, description="The username of the user to log in.")