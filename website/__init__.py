from flask import Flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hashtaganugotsmeeten'
    app.config['MAX_CONTENT_LENGTH'] = 67_108_864  # Max 2 MB upload
    app.config['MAX_FORM_MEMORY_SIZE'] = 67_108_864

    from .views import views
    from .polaroid import polaroid
    from .sepia import sepia
    from .VHS import VHS

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(polaroid, url_prefix='/')
    app.register_blueprint(sepia, url_prefix='/')
    app.register_blueprint(VHS, url_prefix='/')

    return app