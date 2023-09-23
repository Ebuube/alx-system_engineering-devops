# Execute a command

exec {'pkill':
  command  => 'pkill ping',
  provider => 'shell',
}
