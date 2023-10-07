# Install and configure an Nginx server

$server = 'nginx'

# Update packages
exec { 'apt-update':
  command  => 'apt-get --assume-yes update',
  provider => 'shell',
}

# Install nginx package
-> package { $server:
  ensure  => installed,
}

# ensure service is running
-> service { $server:
  ensure  => running,
}

# Set firewall
-> exec {'set_firewall':
  command  => 'ufw allow "Nginx HTTP"',
  provider => 'shell',
}

# Permit user
$user = 'ubuntu'
$site = '/var/www/html'
$home = "/home/${user}/work"

-> file {'set_site_owner':
  ensure => directory,
  path   => $site,
  owner  => $user,
  group  => $user,
  mode   => 'ugo=rwx',
}

$index_dest = "${site}/index.html"
# $index_src = "${home}/index.html"
-> file { 'landing_page':
  ensure  => present,
  path    => $index_dest,
  content => "Hello World!\n",
  owner   => $user,
  group   => $user,
}

$err_page_dest = "${site}/404.html"
# $err_page_src = "${home}/404.html"
-> file { 'error_page':
  ensure  => present,
  path    => $err_page_dest,
  content => "Ceci n'est pas une page\n\n",
  owner   => $user,
  group   => $user,
}

# Set pages for website
$dummy_file = "${home}/dummy_file"
-> File {'set_pages':
  path    => $dummy_file,
  ensure  => absent,
}

# Configure server
$available_site = '/etc/nginx/sites-available/default'
$enabled_site = '/etc/nginx/sites-enabled/default'
# $config_src = "${home}/server_config_4"
-> file { 'server_config':
  ensure  => present,
  path    => $available_site,
  content => @(END_OF_CONTENT)
# Configuration for server - ONWUTA EBUBE GIDEON
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;

	# Include header in responses
	add_header X-Served-By $hostname;

	# Add index
	index index.html

	server_name _;

	location / {
		# First attempt to serve a request as file, then
		# as directiory, then fall back to dispalying a 404 ERROR.
		try_files $uri $uri/ =404;
	}

	location /redirect_me {
		# Have fun with redirection
		rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
	}

	# Create a custom 404 error page
	error_page 404 /404.html;
	location = /404.html {
		# to ensure it cannot be accessed directly by clients
		internal;
	}
}
  END_OF_CONTENT
}

-> file { 'enabled_site':
  ensure => link,
  path   => $enabled_site,
  target => $available_site,
}

-> exec { 'nginx_restart':
  command  => "service ${server} restart",
  provider => 'shell',
}
