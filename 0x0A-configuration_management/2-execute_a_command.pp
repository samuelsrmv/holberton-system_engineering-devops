# kill process

exec { 'killmenow':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  provider => 'shell'
  command => "pkill -SIGKILL -f killmenow",
}