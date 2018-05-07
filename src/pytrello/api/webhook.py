from pytrello.api import decorators


@decorators.basic_api
def get_webhook(webhook_id):
    pass


@decorators.basic_api
def get_webhook_field(webhook_id, field):
    pass


@decorators.basic_api
def update_webhook(webhook_id):
    pass


@decorators.basic_api
def create_webhook(callbackURL, idModel, description=None):
    pass


@decorators.basic_api
def delete_webhook(webhook_id):
    pass
