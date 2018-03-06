class Development(object):
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///interoute.db'


class Testing(object):
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///interoute.db'


class Production(object):
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///interoute.db'
