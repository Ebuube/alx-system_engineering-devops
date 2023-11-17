# Adjust ulimit value
package { 'nginx':
  ensure => installed
}

-> exec { 'adjust ulimit':
  command  => "sudo sed -i 's/-n .*\"/-n 4096\"/g' /etc/default/nginx",
  provider => 'shell',
}

-> exec {'stop nginx':
  command  => 'sudo /usr/sbin/service nginx restart',
  provider => 'shell',
}
