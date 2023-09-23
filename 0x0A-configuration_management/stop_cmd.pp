# Stop a process

exec {'pkill':
  command  => 'pkill console',
  provider => 'shell'
}
