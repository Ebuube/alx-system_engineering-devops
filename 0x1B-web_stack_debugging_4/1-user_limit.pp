# Increase the permitted number of open files for a user

exec {'increase hard nofile':
  command  => "sudo sed -i 's/^holberton hard nofile .*$/holberton hard nofile 4096/g' /etc/security/limits.conf",
  provider => 'shell',
}

-> exec { 'increase soft nofile':
  command  => "sudo sed -i 's/^holberton soft nofile .*$/holberton soft nofile 4096/g' /etc/security/limits.conf",
  provider => 'shell'
}
