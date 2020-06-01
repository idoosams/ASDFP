source .env/bin/activate

CONFIGPATH="/home/idos/Desktop/ASDFP/asd/localconfig.ini"

python -m asd.server run_server --config_path $CONFIGPATH &
echo "server started"
python -m asd.dbclient run --config_path $CONFIGPATH &
echo "dbclient started"
python -m asd.workers --w users --config_path $CONFIGPATH &
echo "users worker started"
python -m asd.workers --w pose --config_path $CONFIGPATH &
echo "pose worker started"
python -m asd.workers --w feelings --config_path $CONFIGPATH &
echo "feelings worker started"
python -m asd.workers --w depth_image --config_path $CONFIGPATH &
echo "worker started"
python -m asd.workers --w color_image --config_path $CONFIGPATH &
echo "color_image worker started"
python -m asd.api run --config_path $CONFIGPATH &
echo "api started"

