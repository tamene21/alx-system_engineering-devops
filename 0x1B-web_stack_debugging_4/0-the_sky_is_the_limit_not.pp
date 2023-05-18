#Increasing trafic twards nginx
exec {'fix--for-nginx':
  commdand => 'seed -i "s/15/4096" /etc/default/nginx',
  path     => '/usr/bin/env/'
}

#Restart nginx
exec {'restart-nginx:
  command => 'nginx restart',
  path    => '/etc/init.d' 
}
