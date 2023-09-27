# Install and configure an Nginx server

$server = 'nginx'

# Update packages
exec { 'apt-update':
  command  => 'apt-get -y update',
  provider => 'shell',
}

# Install nginx package
package { $server:
  ensure  => installed,
  require => Exec['apt-update'],
}

# ensure service is running
service { $server:
  ensure  => running,
  require => Package[$server],
}

# Set firewall
exec {'set_firewall':
  require  => Service[$server],
  command  => 'ufw allow "Nginx HTTP"',
  provider => 'shell',
}

# Permit user
$user = 'ubuntu'
$site = '/var/www/html'
$home = "/home/${user}/work"

file {'set_site_owner':
  ensure  => directory,
  path    => $site,
  require => Service[$server],
  owner   => $user,
  group   => $user,
  mode    => 'ugo=rwx',
}

$index_dest = "${site}/index.html"
$index_src = "${home}/index.html"
file { 'landing_page':
  ensure  => present,
  require => File['set_site_owner'],
  path    => $index_dest,
  source  => $index_src,
  owner   => $user,
  group   => $user,
}

$err_page_dest = "${site}/404.html"
$err_page_src = "${home}/404.html"
file { 'error_page':
  ensure  => present,
  path    => $err_page_dest,
  require => File['set_site_owner'],
  source  => $err_page_src,
  owner   => $user,
  group   => $user,
}

# Set pages for website
$dummy_file = "${home}/dummy_file"
File {'set_pages':
  path    => $dummy_file,
  ensure  => absent,
  require => [File['landing_page'], File['error_page']],
}

# Configure server
$available_site = '/etc/nginx/sites-available/default'
$enabled_site = '/etc/nginx/sites-enabled/default'
$config_src = "${home}/server_config_4"
file { 'server_config':
  ensure  => present,
  path    => $available_site,
  require => Service[$server],
  source  => $config_src,
}

file { 'enabled_site':
  ensure  => link,
  path    => $enabled_site,
  target  => $available_site,
  require => File['server_config']
}

exec { 'nginx_restart':
  command  => "service ${server} restart",
  require  => [Service[$server], File['set_pages'], File['enabled_site']],
  provider => 'shell',
}
