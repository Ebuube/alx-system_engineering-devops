# Conditionals in Puppet

exec {'Test':
  command => '/bin/echo apache2 is installed > ./msg',
  onlyif  => '/bin/which apache2',
}
