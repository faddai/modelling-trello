'''
A collection of helper functions
'''

def get_class_representation(klass):
    '''Get a meaningful representation for a given class instance'''
    return '<{} {}>'.format(klass.__class__.__name__, klass.__dict__)
