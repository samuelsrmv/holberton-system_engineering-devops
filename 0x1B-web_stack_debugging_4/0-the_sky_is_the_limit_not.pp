# Sky is the limit, let's bring that limit higher
exec { 'task-0':
  provider => 'shell',
  command  => "sed -i 's/15/1000/g' /etc/default/nginx; service nginx restart",
}
