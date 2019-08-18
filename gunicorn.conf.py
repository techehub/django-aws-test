bind = "ec2-13-233-173-144.ap-south-1.compute.amazonaws.com:8000"                   # Don't use port 80 becaue nginx occupied it already.
errorlog = '/home/ubuntu/django-aws-test/logs/gunicorn-error.log'  # Make sure you have the log folder create
accesslog = '/home/ubuntu/django-aws-test/logs/gunicorn-access.log'
loglevel = 'debug'
workers = 1     # the number of recommended workers is '2 * number of CPUs + 1'