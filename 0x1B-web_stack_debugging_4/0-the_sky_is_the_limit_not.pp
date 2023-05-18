#Increasing trafic twards nginx
exec {'fix--for-nginx':
  commdand => 'seed -i "s/45/4096" /etc/default/nginx',
  path     => '/usr/local/bin/:/bin/'
}->

#Restart nginx
exec {'restart-nginx:
  command => 'nginx restart',
  path    => '/etc/init.d' 
}
