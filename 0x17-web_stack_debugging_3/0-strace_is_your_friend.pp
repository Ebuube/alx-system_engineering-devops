# Repair Apache2 server
exec { 'modify_invalid_name':
  command  => " sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
  provider => 'shell'
}
