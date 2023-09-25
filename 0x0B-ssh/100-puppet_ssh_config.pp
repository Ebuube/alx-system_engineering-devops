# Client configuration file

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => '# Client-side configuration
Host *
	PasswordAuthentication no
	IdentityFile ~/.ssh/school'
}
