# kill process

exec { 'killmenow':
  command  => "to_kill=$(pgrep -f killmenow) | pkill $to_kill",
}