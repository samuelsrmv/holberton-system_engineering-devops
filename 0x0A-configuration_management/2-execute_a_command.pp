# kill process

exec { 'killmenow':
  path    => '/usr/bin',
  command => 'pkill -f killmenow',
  returns => '0',
}