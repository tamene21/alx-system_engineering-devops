#Increasing trafic twards nginx

exec {'replace':
  provider => shell,
  command => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/"  /etc/default/nginx',
  before   => exec['restart'],
}

#Restart nginx
exec {'restart':
  provider => shell,
  command => 'sudo service nginx restart',
}
