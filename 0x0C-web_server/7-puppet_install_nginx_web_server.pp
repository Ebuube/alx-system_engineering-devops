# Install Nginx web server (w/Puppet)

package { 'nginx':
  ensure => installed,
}

exec { 'ufw':
  command  => 'ufw allow "Nginx HTTP"',
  provider => 'shell',
  require  => Package['nginx'],
}

exec { 'chown':
  command  => 'chown -R $USER:$USER /var/www/html',
  provider => 'shell',
  require  => Exec['ufw'],
}

exec { 'echo_index':
  command  => 'echo Hello World! > /var/www/html/index.html',
  provider => 'shell',
  require  => Exec['chown'],
}

exec { 'configure_server':
  command  => 'cp ./server_config_4 /etc/nginx/sites-enabled/default',
  provider => 'shell',
  require  => Exec['echo_index'],
}

exec { 'restart_exam':
  command  => 'service nginx restart',
  provider => 'shell',
  require  => Exec['configure_server'],
}
