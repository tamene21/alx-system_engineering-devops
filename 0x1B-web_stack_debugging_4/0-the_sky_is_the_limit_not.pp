#Increasing trafic twards nginx

exec {'fix--for-nginx':
  provider => shell,
  commdand => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/"  /etc/default/nginx',
  path     => '/usr/bin/env/'
}

#Restart nginx
exec {'restart-nginx':
  provider => shell,
  command => 'sudo nginx restart',
}
