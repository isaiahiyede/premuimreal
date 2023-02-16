#!/bin/bash

NAME="cdal-main"
DJANGODIR=/root/cdal-main
SOCKFILE=/root/prc_env/run/gunicorn.sock
USER=root
GROUP=root
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=cdal.settings
DJANGO_WSGI_MODULE=cdal.wsgi
echo "Starting $Name as `whoami`"

cd $DJANGODIR
source /root/prc_env/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

exec gunicorn ${DJANGO_WSGI_MODULE}:application \
	--name $NAME \
	--workers $NUM_WORKERS \
	--user=$USER --group=$GROUP \
	--bind=unix:$SOCKFILE \
	--log-level=debug \
	--log-file=-
