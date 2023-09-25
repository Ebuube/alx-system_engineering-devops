# This manifest manipulates files

file { '/home/vagrant/README.md':
  ensure  => present,
  content => '## PROJECT ON PUPPET MANIFETS'
}
