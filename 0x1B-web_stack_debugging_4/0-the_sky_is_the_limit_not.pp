# Adjust ulimit value
exec { 'adjust ulimit':
  command  => "sudo sed -i 's/-n .*\"/-n 4096\"/g' /etc/default/nginx",
  provider => 'shell'
}

exec { 'restart nginx':
  command  => 'sudo service nginx restart',
  provider => 'shell'
}
