# full task 101

file{"/data/web_static/releases/test/index.html":
ensure  => "file",
content => "hello world",
owner   => "ubuntu",
group   => "ubuntu",
require => File["/data/web_static/releases/test"],}

# Create all folders
file{"/data/web_static/releases/test":
ensure  => "directory",
owner   => "ubuntu",
group   => "ubuntu",
require => File["/data/web_static/releases"],}

# Create all the folders
file{"/data/web_static":
ensure  => "directory",
owner   => "ubuntu",
group   => "ubuntu",
require => File["/data"],}

# Create all the folders
file{"/data/web_static/releases":
ensure  => "directory",
owner   => "ubuntu",
group   => "ubuntu",
require => File["/data/web_static"],}

# Create all the folders
file{"/data/web_static/shared":
ensure  => "directory",
owner   => "ubuntu",
group   => "ubuntu",
require => File["/data/web_static"],}

# Create all the folders
file{"/data/web_static/current":
ensure  => "link",
owner   => "ubuntu",
group   => "ubuntu",
target  => "/data/web_static/releases/test",
require => File["/data/web_static"],}

# Create a symbolic link
file{"/data":
ensure => "directory",
owner  => "ubuntu",
group  => "ubuntu",}

file{"/etc/nginx/sites-available/default":
  ensure  => "file",
  content => "server {
    listen 80;
    listen [::]:80 default_server;
    server_name anubisproject.tech;
    location /hbnb_static {
        alias /data/web_static/current/;
    }
}",
  require => Package['nginx'],
  notify  => Service['nginx'],
  replace => 'true',
}

#install nginx
package{ 'nginx':
  ensure => 'installed',
}

#start nginx
service{ 'nginx':
  ensure => 'running',
  enable => 'true',
}
